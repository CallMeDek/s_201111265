
#coding: utf-8

import os, json

def write_json_1(filename, contents):
    with open(os.path.join('data', filename), 'w') as json_file:
        json.dump(contents, json_file )

def write_json_2(filename, contents):
    import io
    with io.open(os.path.join('data', filename), 'w', encoding='utf8') as json_file:
        data = json.dumps(contents, json_file, ensure_ascii=False ,encoding="utf8")
        json_file.write(data)
        
def read_json_1(filename):
    with open(os.path.join('data', filename), 'r') as json_file:
        my_dict = json.loads(json_file.read())
    for key in my_dict.keys():
        my_list = my_dict[key]
        for item in my_list:
            key_list = item.keys()
            print key_list[0].encode('euc-kr'),item.get(key_list[0]),'  ',
    print '\n'
  
def read_json_2(filename):
    with open(os.path.join('data', filename), 'r') as json_file:
        my_dict = json.load(json_file)
    for key in my_dict.keys():
        my_list = my_dict[key]
        for item in my_list:
            key_list = item.keys()
            print key_list[0].encode('euc-kr'),item.get(key_list[0]),'  ',
    print '\n'

def read_json_url():
    import requests
    _url = "https://health.data.ny.gov/api/views/jxy9-yhdk/rows.json?accessType=DOWNLOAD"
    rResponse = requests.get(_url)
    if rResponse.status_code == 200:
        url_json = rResponse.json()
    return url_json


def read_json_url2():
    import urllib2
    url = 'http://archive.ics.uci.edu/ml/machine-learning-databases/horse-colic/horse-colic.data'
    uResponse = urllib2.urlopen(url)
    html = uResponse.read()
    uResponse.close()
    
    lines = html.splitlines()
    data = []
    for line in lines:
        data.append(line.split())
    return data

def data_check(mylist):
    sum=0
    cnt=0
    min=float(mylist[0][3])
    max=float(mylist[0][3])
    
    for i in range(0, 20):
        val = mylist[i][3]
        if val is '?':
            print i, "None"
        else:
            if(val > max):
                max = val
            if(val < min):
                min = val
            sum += float(val)
            cnt += 1
            print i, val, sum
    average = float(sum/cnt)
    print "Count={0} Sum={1} Average={2:2.2f} Max={3} Min={4}".format(cnt, sum , average, max, min)
    
    
def read_csv(filename, limit):
    import csv
    file_obj = open(os.path.join('data', filename), 'rb')
    reader = csv.reader(file_obj)
    
    rownum = 0
    for row in reader:
        if(rownum == limit):
            break
        for col in row:
            print unicode(('%s' % (col)), 'euc-kr')
        print
        rownum += 1
    file_obj.close()

def main():
    p = {"Persons":[
        {"id":"405", u"이름":"js1"},
        {"id":"406", u"이름":"js2"},
        {"id":"407", u"이름":"js3"}
    ]}
    write_json_1("ds_save_persons.json", p)
    write_json_2("ds_save_persons2.json", p)
    read_json_1("ds_save_persons.json")
    read_json_2("ds_save_persons2.json")
    #p = read_json_url() 실행은 되지만 데이터가 너무 큽니다. 
    #write_json_1("ds_save_url.json",p)
    #read_csv("companyList.csv", 20)
    _list = read_json_url2()
    data_check(_list)
    
if __name__=="__main__":
    print "\n\nIt uses functions of itself\n\n"
    main()
else:
    print "\n\nModule is attached\n\n"