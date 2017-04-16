
# -*- coding: utf-8 -*-

import requests
import re
import lxml.html
import lxml.etree

def getString():
    rResponse = requests.get('http://www.kbreport.com/leader/main?rows=20&order=oWAR&orderType=DESC&teamId=1&defense_no=2&year_from=2015&year_to=2015&split01=&split02_1=&split02_2=&r_tpa_count=&tpa_count=0')
    html_str = rResponse.text
    return html_str

def win_or_lose():
    htmlStr = getString()
    front = htmlStr.find('top-score-box')
    back = htmlStr.find('top-score end')
    htmlStr = htmlStr[front:back]
    #print htmlStr
    
    myPattern = re.compile(u'(.승.*?)</p>')
    for element in myPattern.findall(htmlStr):
        print element
   
def get_main_information():
    htmlStr = requests.get('http://www.kbreport.com/main').text
    tree = lxml.etree.HTML(htmlStr)
    
    pattern = tree.xpath('//div[@class="team-rank-box"]/table//tr/th')
    for node in pattern:
        print node.xpath('.//text()')[0]," "*2,
    
    print "\n"
    pattern = tree.xpath('//div[@class="team-rank-box"]/table//tr')
    for i in range(1, len(pattern)):
        element = pattern[i].xpath('.//td')
        for j in range(0, len(element)):
            if(j == 1):
                print element[j].xpath('.//a/text()')[0].strip()," "*3,
            else:
                print element[j].xpath('./text()')[0].strip()," "*3,
        print "\n"
        
    
def main():
    print"\n\n Win and Lose \n\n"
    win_or_lose();
    print"\n\n Main page Information \n\n"
    get_main_information()
    
if __name__=='__main__':
    main()