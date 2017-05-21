
#coding: utf8
'''
    사용API 주소: http://data.seoul.go.kr/openinf/openapiview.jsp?infId=OA-12914
    사용 예시 : http://openapi.seoul.go.kr:8088/(인증키)/xml/CardSubwayStatsNew/1/5/20151101
'''
import os

def make_url(START_INDEX, END_INDEX):
    import mylib, url_encode_problem_sol
    basic_url = 'http://openapi.seoul.go.kr:8088'
    key_path = os.path.join(os.getcwd(), 'src', 'key.properties')
    key_dict = mylib.getKey(key_path)
    my_key = key_dict['subject7']
    TYPE = 'json'
    SERVICE = 'CardSubwayStatsNew'
    USE_DT = '20170518'

    url = os.path.join(basic_url, my_key, TYPE, SERVICE, str(START_INDEX), str(END_INDEX), USE_DT)
    url_c = url_encode_problem_sol.convert_url_os_path_join(url)
    
    return url_c

def get_json(start, end):
    import requests
    url = make_url(start, end)
    rResponse = requests.get(url)
    rResponse_json = ''
    if(rResponse.status_code == 200):
        rResponse_json = rResponse.json()
    return rResponse_json

def saveJson(filename, data):
    import io, json
    with io.open(filename, 'a') as json_file:
        _j=json.dumps(data, json_file, ensure_ascii=False, encoding='utf8')
        json_file.write(_j+"\n")
        
def saveMongo(data):
    import pymongo
    from pymongo import MongoClient
    
    client = MongoClient('localhost:27017')
    db = client.myDB
    
    table = db['db_open_subwayTable']
    table.insert_one(data)

def main():
    start_index = 1
    end_index = 5
    iterator = 0
    max_iterator = 5
    f_name = 'src\\ds_open_subwayPassengers.json'
    while(iterator < max_iterator):
        json = get_json(start_index, end_index)
        #print json, "\n\n"
        saveJson(f_name, json)
        saveMongo(json)
        start_index += 5
        end_index += 5
        iterator += 1

if __name__=="__main__":
    main()