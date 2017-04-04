# coding: utf-8
import lxml.html
import requests
from lxml.cssselect import CSSSelector

keyword='비오는'
rResponse = requests.get("http://music.naver.com/search/search.nhn?query="+keyword+"&x=0&y=0")
_html = lxml.html.fromstring(rResponse.text)

sel = CSSSelector('table[summary] > tbody > ._tracklist_move')
nodes = sel(_html)

_selName = CSSSelector('.name > a.title')
_selArtist = CSSSelector('.artist.artist')
_selAlbum = CSSSelector('.album > a')
for node in nodes:
    _name = _selName(node)
    _artist = _selArtist(node)
    _album = _selAlbum(node)
    if _name:
        print _artist[0].text_content().strip(),
        print "---",
        print _name[0].text_content(),
        print "---",
# coding: utf-8
import lxml.html
import requests
from lxml.cssselect import CSSSelector

keyword='비오는'
rResponse = requests.get("http://music.naver.com/search/search.nhn?query="+keyword+"&x=0&y=0")
_html = lxml.html.fromstring(rResponse.text)

sel = CSSSelector('table[summary] > tbody > ._tracklist_move')
nodes = sel(_html)

_selName = CSSSelector('.name > a.title')
_selArtist = CSSSelector('.artist.artist')
_selAlbum = CSSSelector('.album > a')
for node in nodes:
    _name = _selName(node)
    _artist = _selArtist(node)
    _album = _selAlbum(node)
    if _name:
        print _artist[0].text_content().strip(),
        print "---",
        print _name[0].text_content(),
        print "---",
        print _album[0].text_content()
