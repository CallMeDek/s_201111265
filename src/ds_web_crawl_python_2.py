
# coding: utf-8

import re
import requests
import lxml.etree
import lxml.html
import StringIO
import sys
from bs4 import BeautifulSoup
from lxml.cssselect import CSSSelector

def getURLString():
    response = requests.get("http://www.python.org")
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
    print "\n\n"

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
    print "\n\n"
    
def method3_xpath():
    print u"h1태그의 문자열을 읽어보자."
    html_str = getURLString()
    
    tree = lxml.etree.HTML(html_str)
    xpath_list = tree.xpath("//h1")
    for i , e in enumerate(xpath_list):
        if i < 20:
            print e.xpath(".//text()")[0] 
    print "\n\n"
    
def method4_cssselctor():
    print u"img 태그의 src 속성을 알아보자"
    my_string = getURLString()
    parser = lxml.etree.HTMLParser()
    tree = lxml.html.parse(StringIO.StringIO(my_string), parser)
    
    select = CSSSelector('img[src]')
    nodes = select(tree)
    for i,e in enumerate(nodes):
        if i < 20:
            print i, e.get('src')
    print "\n\n"
    
def main():
    print "\n\n----------------------\n\n"
    print "Welcome!!"
    print "\n\n----------------------\n\n"
    while(True):
        print "1.method1_regex()\n","2.method2_regex()\n","3.method3_xpath()\n","4.method4_cssselctor()\n","5.EXIT\n"
        num = input("Insert Number>> ")
        if (num==1):
            method1_regex()
        elif (num==2):
            method2_regex()
        elif (num==3):
            method3_xpath()
        elif (num==4):
            method4_cssselctor()
        elif (num==5):
            print u"종료합니다.\n\n"
            sys.exit()
        else:
            print u"잘못된 번호입니다.\n\n"
    
if __name__ == "__main__":
    main()