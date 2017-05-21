
#coding: utf-8

import os, urllib, mylib, urlparse, requests, url_encode_problem_sol

def dolt():
    SERVICE='ArpltnInforInqireSvc'
    OPERATION_NAME='getMinuDustFrcstDspth'
    params1 = os.path.join(SERVICE, OPERATION_NAME) 
    _d = dict()
    params2 = urllib.urlencode(_d)
    keyPath = os.path.join(os.getcwd(), 'src', 'key.properties')
    key = mylib.getKey(keyPath)
    keygokr = key['gokr']
    _d['serviceKey'] = keygokr
    _d['dataTerm'] = 'month'
    params = params1 + '?' + url_encode_problem_sol.convert_urllib_urlencode(urllib.urlencode(_d))
    _url = 'http://openapi.airkorea.or.kr/openapi/services/rest/ArpltnInforInqireSvc'
    url = urlparse.urljoin(_url, params)
    url_c = url_encode_problem_sol.convert_url_os_path_join(url)
    data = requests.get(url_c).text
    print data[:500]
    
if __name__=="__main__":
    dolt()