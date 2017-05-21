
#coding : utf-8

import os, mylib, urlparse, requests

def dolt():
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
    url_c = ''
    for char in url:
        if char == '\\':
            url_c += '/'
        else:
            url_c += char
    #print url_c
    #print url
    data=requests.get(url_c).text
    print data[:300]
    
if __name__ == "__main__":
    dolt()