
# coding: utf-8

import requests
import lxml.html
import lxml.etree

def sangmyungNoticCrawl():
    rResponse2 = requests.get('https://www.smu.ac.kr/mbs/smu/jsp/board/list.jsp?boardId=14446&id=smu_040100000000')
    _html2 = lxml.etree.HTML(rResponse2.text)

    th_info = _html2.xpath('//*[@id="subContents"]/form[2]/table/tbody/tr[1]/th')
    for node in th_info:
        print node.text,"            ", \

    print "\n"
    td_tr = _html2.xpath('//*[@id="subContents"]/form[2]/table/tbody/tr')
    for j in range(0, len(td_tr)):
        td_info = td_tr[j].xpath('.//td')
        for i in range(0, len(td_info)):
            if((i == 0)and(td_info[i].xpath('.//img'))):
                print "\n",u"공지".strip(), " / ", 
            elif ((i == len(td_info)-1)and(td_info[i].xpath('.//img'))):
                print u"파일 있음".strip()
            elif (td_info[i].xpath('.//a/text()')):
                print unicode(td_info[i].xpath('.//a/text()')[0]).strip(), " / ", 
            else:
                print td_info[i].text.strip(), " / ", 
                
def main():
    sangmyungNoticCrawl()
    
if __name__ == "__main__":
    main()