# coding: utf-8
import os
import urllib
import urlparse
import requests
import mylib

def doIt():
    _d=dict()
    _d['title']='도둑' 
    _d['manageCd']='MA'
    _d['numOfRows']='5'
    _d['pageNo']='2'
    params2 = urllib.urlencode(_d)

    keyPath=os.path.join(os.getcwd(), 'src', 'key.properties')
    key=mylib.getKey(keyPath)
    print key['gokr'] + '\n'
    params='?'+'serviceKey='+key['gokr']+'&'+params2

    _url = 'http://openapi-lib.sen.go.kr/openapi/service/lib/openApi'
    url=urlparse.urljoin(_url,params)
    _url_f = _url
    _url = ''
    for i in _url_f:
        if i == ('\\'):
            _url += '/'
        else:
            _url += i
    data=requests.get(url).text
    print data

if __name__ == "__main__":
    doIt()