# coding: utf-8
import lxml.html
import requests
from lxml.cssselect import CSSSelector

rResponse = requests.get('http://www.ieee.org/conferences_events/conferences/search/index.html')
html = lxml.html.fromstring(rResponse.text)

sel = CSSSelector('div.content-r-full table.nogrid-nopad tr p>a[href]')
nodes = sel(html)

for i, node in enumerate(nodes):
    print i, node.text
# coding: utf-8
import lxml.html
import requests
from lxml.cssselect import CSSSelector

rResponse = requests.get('http://www.ieee.org/conferences_events/conferences/search/index.html')
html = lxml.html.fromstring(rResponse.text)

sel = CSSSelector('div.content-r-full table.nogrid-nopad tr p>a[href]')
nodes = sel(html)

for i, node in enumerate(nodes):
    print i, node.text
    print "--------------"
