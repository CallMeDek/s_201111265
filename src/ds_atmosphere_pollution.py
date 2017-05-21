
#coding: utf-8

import urllib, url_encode_problem_sol, os, mylib, requests

def save_file(data):
    import io, json
    with io.open(os.path.join('src', 'ds_atmosphere_pollution.json'), 'a') as json_file:
        j_data = json.dumps(data, json_file, ensure_ascii = False, encoding="utf8")
        json_file.write(j_data + '\n')

def save_mongo(data):
    import pymongo
    from pymongo import MongoClient
    client = MongoClient('localhost:27017')
    db = client['myDB']
    collection = db['db_open_atmosphereTable']
    collection.insert_one(data)
    
def main():
    basic_url = 'http://openapi.airkorea.or.kr/openapi/services/rest/ArpltnInforInqireSvc'
    service = 'getMsrstnAcctoRltmMesureDnsty'

    param_dict = dict()

    pageNum = 1
    param_dict['numOfRows'] = '5'

    param_dict['stationName'] = '종로구'
    param_dict['dataTerm'] = 'MONTH'
    keyPath = os.path.join('src', 'key.properties')
    key_dict = mylib.getKey(keyPath)
    mykey = key_dict['gokr']
    param_dict['ServiceKey'] = mykey
    param_dict['_returnType'] = 'json'


    while(pageNum < 20):
        param_dict['pageNo'] = "%s"%pageNum
        params = urllib.urlencode(param_dict)
        url = basic_url + '/' + service + '?'+'&' + url_encode_problem_sol.convert_urllib_urlencode(params)
        json_data = requests.get(url).json()
        save_file(json_data)
        save_mongo(json_data)
        pageNum += 1
    
    
if __name__=="__main__":
    main()