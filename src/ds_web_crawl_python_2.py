
# coding: utf-8

import re
import requests
from bs4 import BeautifulSoup

def getURLString():
    response = requests.get("http://www.naver.com")
    html_string = response.text
    #print response.headers
    return html_string

def method1_regex():
    regex = 'href="(.*?)"'
    text = getURLString()
    print u"href 속성은 몇개?"
    count = 0
    for count,element in enumerate(re.compile(regex).findall(text)):
        if count < 20:
            print count+1, element
    print u"\n\nhref 속성은 = {0}개 입니다.".format(count)

def method2_regex():
    print u"a 태그는 몇개?"
    regex2 = "<a .+?>.*?</a>" #a 태그에 무슨 속성이 들어가있는지 패턴이 정해져 있지 않으므로
    pattern = re.compile(regex2)
    text = getURLString()
    count = 0
    for count,element in enumerate(pattern.findall(text)):
        if count < 20:
            print count+1
            print element
    print u"\n\na 태그는 = {0}개 입니다.".format(count)
    
    
if __name__ == "__main__":
    method1_regex()
    print "\n\n"
    method2_regex()
    print "\n\n"