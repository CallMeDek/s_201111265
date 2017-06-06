#coding: utf-8
from pymongo import MongoClient
import mylib
import os
import sys
import requests
import findspark
import pyspark

client = MongoClient('localhost:27017')
db = client.bigData

os.environ["SPARK_HOME"]='C:\Users\Code\s-201111265\spark-2.0.0-bin-hadoop2.6'
findspark.init(os.environ["SPARK_HOME"])
myConf=pyspark.SparkConf()
spark = pyspark.sql.SparkSession.builder.master("local")\
    .appName("myApp").config("spark.sql.warehouse.dir", os.path.join(os.environ['SPARK_HOME'], 'data', 'data_warehouse'))\
    .getOrCreate()

# 코스피 지수와 날짜를 네이버 금융 메뉴에서 파싱해 옵니다. 
# 날짜별로, 전 날짜와 비교하여 상승했으면 1, 하강했으면 0이라는 값을 추가하고 
# (날짜, 상승/하강)을  'data', 'kospi.txt'에 저장하고 몽고DB는 bigData db의 kospi라는 document에 저장합니다.
def save_kospi_data():
    import urllib
    
    count=22 #마지막 거래일로부터 몇 거래일의 주가지수를 가져올지 입력
    url="http://fchart.stock.naver.com/sise.nhn?symbol=KOSPI&timeframe=day&count=%d&requestType=0"%(count)
    urltext=urllib.urlopen(url).read().decode('latin-1')

    KOSPI=[]
    stocklist=urltext.split("\"")
    stocklist_selection=stocklist[17:]

    i=0
    while i<=(len(stocklist_selection)-1):
        KOSPI.append(stocklist_selection[i])
        i=i+2

    KOSPI=str(KOSPI).split("|")
    KOSPI[0]=KOSPI[0][2:]
    KOSPI[len(KOSPI)-1]=KOSPI[len(KOSPI)-1][:7]
    #중간에 수치에 붙어있는 군더더기 제거

    date=[KOSPI[0]]
    price=[]
    volumn=[]

    j=5
    while j<=(len(KOSPI)-5):
        date.append(KOSPI[j][10:])
        volumn.append(KOSPI[j][:7])
        j=j+5
    volumn.append(KOSPI[len(KOSPI)-1])

    r=0
    while r<=(len(volumn)-2):
        volumn[r]=volumn[r][:(len(volumn[r])-1)]
        r=r+1
    #거래량 끝에 붙어있는 ' 제거
    k=4
    while k<=(len(KOSPI)-1):
        price.append(KOSPI[k])
        k=k+5

    kospi_dict = dict()

    for i in range(len(date)):
        temp = float(price[i])
        temp_date = int(date[i][1:len(date[i])])
        kospi_dict[temp_date] = temp

    keys = kospi_dict.keys()   

    for i in range(len(kospi_dict)-1, 0, -1):
        if(kospi_dict[keys[i]] > kospi_dict[keys[i-1]]):
            kospi_dict[keys[i]] = 1 #1이면 상승
        else:
            kospi_dict[keys[i]] = 0 #0이면 하락

    kospi_dict = kospi_dict.items()

    big_str = ""
    
    for i in range(1, len(kospi_dict)):
        big_str = big_str + str(kospi_dict[i][0]) + ' '
        big_str = big_str + str(kospi_dict[i][1]) + '\n'
    
    f = open(os.path.join('data', 'kospi.txt'),'w')
    f.write(big_str)
    f.close()

    sorted_kospi_list = list()
    sorted_kospi_list.append(big_str)
    #db.kospiData.insert_one({
    #   "kospi": sorted_kospi_list
    #})

# 검색어로 네이버 블로그의 제목, 포스팅 날짜를 가져옵니다. 오픈 api를 사용합니다.
# 날짜별로, 전 날짜와 비교하여 상승했으면 1, 하강했으면 0이라는 값을 추가하고 
# (날짜, 제목)을  'data', 'blog.txt'에 저장하고 몽고DB는 bigData db의 blogData라는 document에 저장합니다.
def save_blog_data(keyword):
    #블로그
    key_path = os.path.join('src', 'key.properties')
    keys = mylib.getKey(key_path)

    info = keys['naver'].split(',')

    client_id = info[0]
    client_secret = info[1]

    #https://openapi.naver.com/v1/search/news.json - 뉴스
    #https://openapi.naver.com/v1/search/kin.json - 지식IN (날짜 없음)
    #https://openapi.naver.com/v1/search/cafearticle.json - 카페글 (날짜 없음)
    #https://openapi.naver.com/v1/search/webkr.json - 웹문서
    
    start = 1
    client = MongoClient('localhost:27017')
    db = client.bigData
    count = 0
    
    big_str = ''
    while(start < 1000):
        # json 결과, start -> 시작위치(최대 1000), dispaly -> 출력갯수(최대 100)
        blog_str = ''
        url = "https://openapi.naver.com/v1/search/blog?query=" + keyword + '&display=50' + '&start=' + str(start)
        start = start + 100
        headers_info = {"X-Naver-Client-Id": client_id,  "X-Naver-Client-Secret":client_secret}
        response = requests.get(url, headers=headers_info)
        result_json = response.json()
        for ele in result_json['items']:
            blog_str = blog_str + ele['postdate'] +  ele['title'] + '\n'
        big_str = big_str + blog_str + '\n'
        count = count+1
    big_list = []
    big_list.append(big_str)
    #db.blogData.insert_one({
    #    "entire": big_list
    #})
    
    f = open(os.path.join('data', 'blog.txt'), 'w')
    f.write(big_str.encode('utf8'))
    f.close()
    

def sub_str(str):
    return str[8:]

def exetract(str):
    boolean = str.find(unicode('<b>'))
    if(boolean == -1):
        boolean2 = str.find('2017')
        if(boolean2 == -1):
            boolean3 = str.find('2016')
            if(boolean3 == -1):
                return str
            else:
                return "-1"
        else:
            return "-1"
    else:
        return "-1"

# stop_word 라는 한글 불용어 리스트를 필터에 사용하며, blog.txt에서 제목만 가지고 제일 많이 사용한 단어
# 20개를 추출해냅니다.
def find_most_used_word():
    stop_word = list()
    f = open(os.path.join('data', 'stopwords.txt'))
    entire_word = f.readlines()
    for ele in entire_word:
        word = ele.strip() 
        stop_word.append(word)
    f.close()
    stop_word.append(u'및')
    stop_word.append(u'-')

    rdd = spark.sparkContext.textFile(os.path.join('data','blog.txt'))
    lines = rdd.flatMap(lambda x:x.split('\n')).map(sub_str).flatMap(lambda x:x.split())\
            .map(exetract).filter(lambda x : x not in stop_word).map(lambda x:(x,1))\
            .reduceByKey(lambda x,y: x+y).map(lambda x:(x[1],x[0])).sortByKey(False)

    most_word_list = list()
    for element in lines.take(20):
        if element[1] == '-1':
            continue
        else:
            most_word_list.append(element[1])
    
    return most_word_list

def sub_split(str):
    back = sub_str(str)+" "
    front = str[:8]
    temp = list()
    temp.append(front)
    temp.append(back)
    return tuple(temp)

# blog.txt와 kospi.txt의 날짜를 비교하여 같은 날짜면 새로운 리스트에 추가하는 식으로 진행하고,
# 합병한 리스트를 반환합니다.

def reduce_and_merge():
    rdd = spark.sparkContext.textFile(os.path.join('data','blog.txt'))
    lines = rdd.flatMap(lambda x:x.split('\n')).map(sub_split)\
        .reduceByKey(lambda x, y: x+y).sortByKey(False)
    lines_list = list()
    lines_list.append(lines.collect())
    rdd2 = spark.sparkContext.textFile(os.path.join('data','kospi.txt'))
    lines2 = rdd2.flatMap(lambda x:x.split('\n')).map(lambda x:x.split())
    lines_list2 = list()
    lines_list2.append(lines2.collect())
    for i in range(len(lines_list[0])):
    for j in range(len(lines_list2[0])):
        if(lines_list[0][i][0] == lines_list2[0][j][0]):
            lines_list2[0][j][1] = lines_list2[0][j][1] + '|' + lines_list[0][i][1]
            break
    return lines_list2
    
    
## 날짜별로 합병한 데이터를 상승/하강 별로 나눕니다.    
def upper_data(my_list):
    upper = list()
    for i in range(len(my_list[0])):
        temp = my_list[0][i][1].split('|')
        if(temp[0] == '1'):
            upper.append(my_list[0][i])
            
def lower_data(my_list):
    lower = list()
    for i in range(len(my_list[0])):
        temp = my_list[0][i][1].split('|')
        if(temp[0] == '0'):
            upper.append(my_list[0][i])

# 상승 / 하강 별로, 전에 뽑아두었던 가장 많이 쓰이는 
#단어가 몇번 사용되었는지 계산
def freq_calculate(my_list): 
    most = find_most_used_word()
    frequency = dict()

    for i in range(len(my_list)):
        temp = list()
        check_list = list()
        temp = my_list[i][1].split('|')
        check_list = temp[1].split()
        for ele_j in check_list:
            for ele_k in most:
                if(ele_j == ele_k):
                    if ele_k in frequency:
                        frequency[ele_k] += 1
                    else:
                        frequency[ele_k] = 1
    return frequency

# 위에서 구한 상승과 하강 데이터의 출현 빈도수, 가장 많이 출현한 단어 20개 
# 데이터를 인자로 받아서 dataFrame 생성
def make_dataFrame(my_dict1, my_dict2, most_list):
    fre_keys = my_dict1.keys()
    index_list = list()

    for i in range(len(most_list)):
        for j in range(len(fre_keys)):
            if most_list[i] == fre_keys[j]:
                index_list.append(i)
            
    fre_keys2 = my_dict2.keys()
    index_list2 = list()

    for i in range(len(most_list)):
        for j in range(len(fre_keys2)):
            if most_list[i] == fre_keys2[j]:
                index_list2.append(i)

    #print index_list
    #print index_list2

    from pyspark.mllib.regression import LabeledPoint
    from pyspark.mllib.linalg import Vectors

    tmp_dict = dict()
    for i in range(len(index_list)):
        tmp_dict[index_list[i]] = my_dict1[most_list[index_list[i]]]

    tmp_dict2 = dict()
    for i in range(len(index_list2)):
        tmp_dict2[index_list2[i]] = my_dict2[most_list[index_list2[i]]]

    p = [
        LabeledPoint(1, Vectors.sparse(20, tmp_dict )),
        LabeledPoint(0, Vectors.sparse(20, tmp_dict2 ))
    ]

    trainDf = spark.createDataFrame(p)
    trainDf.show()
    
def draw_graph(freq_diction):
    import matplotlib.pyplot as plt
    count = freq_diction.values()
    word = freq_diction.keys()
    plt.barh(range(len(count)), count, color='red')
    plt.yticks(range(len(count)), word)
    plt.show()

def execute():
    #save_kospi_data()
    #save_blog_data('경제')
    most_list = find_most_used_word()
    merged_list  =  reduce_and_merge()
    upper_list = upper_data(merged_list)
    lower_list = lower_data(merged_list)
    upper_most_freq = freq_calculate(upper_list)
    lower_most_freq = freq_calculate(lower_list)
    make_dataFrame(upper_most_freq, lower_most_freq, most_list)
    print "-------------상승-------------"
    draw_graph(upper_most_freq)
    print "-------------하강-------------"
    draw_graph(lower_most_freq)
        
if __name__ == "__main__":
    execute()