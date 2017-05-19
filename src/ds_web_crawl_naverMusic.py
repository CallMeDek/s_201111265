
 # -*- coding: utf-8 -*-

import urllib
import lxml.html
import lxml.etree
import re
from lxml.cssselect import CSSSelector
import requests
import sys


def getString():
    keyword = "비오는"
    url = "http://music.naver.com/search/search.nhn?query={0}&x=0&y=0".format(keyword)
    my_header = { "User-Agent" : "Mozilla/5.0"}

    uResponse = urllib.urlopen(url, None ,my_header)
    html_str = uResponse.read()
    
    return html_str

def with_Regex():
    html_str = getString()
    front = html_str.find('트랙 리스트')
    back = html_str.find('곡 더보기')

    html_str = html_str[front:back]

    pattern = re.compile('title="(.*비.*오.*는.*?)"')

    for node in pattern.findall(html_str):
        print node
        
def with_CSSSelector():
    #html_str = getString()
    keyword = input("insert>>")
    url = "http://music.naver.com/search/search.nhn?query={0}&x=0&y=0".format(keyword)
    html_str = requests.get(url).text
    
    tree = lxml.html.fromstring(html_str)
    select = CSSSelector('table[summary] .name > a[title]')
    
    nodes = select(tree)
    
    for node in nodes:
        print node.text_content()
        
def with_CSSSelctor_all():
    keyword = "비오는"
    url = "http://music.naver.com/search/search.nhn?query={0}&x=0&y=0".format(keyword)
    html_str = requests.get(url).text
    
    tree = lxml.html.fromstring(html_str)
    title = CSSSelector('table[summary] .name > a[title]')
    artist = CSSSelector('table[summary] ._artist.artist > a[title] > span')
    artist_speical = CSSSelector('table[summary] ._artist.artist.no_ell2 > a ')
    album = CSSSelector('table[summary] .album > a[title]')
    popular = CSSSelector('table[summary] .popular em')
    
    nodes_title = title(tree)
    nodes_artist = artist(tree)
    nodes_artist_special = artist_speical(tree)
    nodes_album = album(tree)
    nodes_pop = popular(tree)
        
    for i in range(0, len(nodes_title)):
        print nodes_title[i].text_content()," ",
        if i == 2:
            print nodes_artist_special[0].text_content().strip()," ",
        elif (i >= 3):
            print nodes_artist[i-1].text_content().strip()," ",
        else:
            print nodes_artist[i].text_content().strip()," ",
        print nodes_album[i].text_content()," ",
        print nodes_pop[i].text_content(), " ", "\n"
    
def main():
    print u"\n\n 정규식으로 하기 \n\n"
    with_Regex()
    print u"\n\n CSS 선택자로 하기 \n\n"
    with_CSSSelector()
    print u"\n\n CSS 선택자로 모두 출력하기 \n\n"
    with_CSSSelctor_all()
    
if __name__=="__main__":
        main()