# coding: utf-8
import os
import requests
import urlparse
import mylib

def doIt():
    keyPath=os.path.join(os.getcwd(), 'src', 'key.properties')
    key=mylib.getKey(keyPath)
    # (1) make params with resource IDs
    KEY=key['dataseoul']
    TYPE='json'
    SERVICE='SearchSTNBySubwayLineService'
    START_INDEX=str(1)
    END_INDEX=str(10)
    LINE_NUM=str(2)
    params=os.path.join(KEY,TYPE,SERVICE,START_INDEX,END_INDEX,LINE_NUM)
    # (2) make a full url
    _url='http://openAPI.seoul.go.kr:8088/'
    
    url=urlparse.urljoin(_url,params)
    url_real = ''
    for i in url:
        if i == '\\':
            url_real += '/'
        else:
            url_real += i
    # (3) get data
    data=requests.get(url_real).text
    print data[:300]

if __name__ == "__main__":
    doIt()