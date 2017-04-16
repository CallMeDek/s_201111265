
# -*- coding: utf-8 -*-

from lxml.cssselect import CSSSelector
import requests
import lxml.html

def crawling_IEEE():
    rResponse = requests.get('http://www.ieee.org/conferences_events/conferences/search/index.html')
    html_str = rResponse.text
    
    tree = lxml.html.fromstring(html_str)
    
    select_header = CSSSelector('.nogrid-nopad > tbody .bold')
    nodes_header = select_header(tree)
    
    for node in nodes_header:
        print node.text_content().strip()," "*45,
        
    print "\n\n"
        
    select_content = CSSSelector('.nogrid-nopad .pad10 a[href]')
    nodes_content = select_content(tree)
    
    i = 0;
    while(i <= len(nodes_content)-3):
        print nodes_content[i].text_content().strip(),"   ",
        print nodes_content[i+1].text_content().strip(),"   ",
        print nodes_content[i+2].text_content().strip(),"   ",
        print "\n"
        i += 3
        
def main():
    crawling_IEEE()
    
if __name__ == "__main__":
    main()