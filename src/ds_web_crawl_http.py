
# coding: utf-8

import sys
import os
import urllib2

def main():
    print "\n\n------------------------\n\n"
    print "             Welcome!"
    print "\n\n------------------------\n\n"
    while(True):
        url = ""
        print u"""(1)네이버\n(2)다음\n(3)파이썬\n(4)구글\n(5)EXIT\n"""
        num = input(">>")
        if(num==1):
            #url = "https://www.naver.com/" + "search.naver?query=python"
            print u"\n\n방화벽으로 막혀있음 확인...\n\n"
            continue
        elif(num==2):
            #url = "https://www.daum.net/" + "search?w=tot&q=python"
            print u"\n\n방화벽으로 막혀있음 확인...\n\n"
            continue
        elif(num==3):
            url = "http://www.python.org/" + "search/?q=python"
        elif(num==4):
            url = "https://www.google.co.kr/" + "#q=python"
        elif(num==5):
            break;
        else:
            printf(u"\n잘못된 번호 입니다.\n")
        request_headers = {
            "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36"
        }
        uRequest = urllib2.Request(url, None, request_headers)
        uResponse = urllib2.urlopen(uRequest)
        
        text = "\n\n" + uResponse.read()
        
        f = open(os.path.join('src', 'myPage.html'), "w")
        f.write(text)
        print "\n\n", os.getcwd() + os.path.join('src', 'mypage.html'), u"저장되었습니다\n\n"
        f.close()
        
    sys.exit()
    
if __name__=="__main__":
    main()