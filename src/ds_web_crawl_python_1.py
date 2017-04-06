# coding: utf-8

from bs4 import BeautifulSoup
import requests
import re

def python_crawl():
    response = requests.get("https://www.python.org/")
    nodes = BeautifulSoup(response.content, "html.parser")

    for i,node in enumerate(nodes.findAll('a')):
        if 'href' in node.attrs:
            print i," Element: ", node,"   ",
            print "\n\nhref-value: ", node.attrs['href'],"   ",
            print "\n\ntext: ", node.text
            print "\n\n"
            
def main():
    python_crawl()
    
if __name__ == "__main__":
    main()