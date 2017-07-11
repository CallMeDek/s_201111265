#coding: utf-8

def getHtml():
    import requests
    url = 'http://edition.cnn.com/2017/02/28/politics/donald-trump-speech-transcript-full-text/index.html'
    try:
        response = requests.get(url)
        _html = response.text
        return _html
    except requests.HTTPError, e:
        print e.code, e.reason

def bs4Parsing(html):
    from bs4 import BeautifulSoup
    soup = BeautifulSoup(html, 'html.parser')
    return soup;
    

def printContents(soup):
    print soup.find('span',{'class':'el__storyelement__header'}).contents[0],
    print " : ", soup.find('span',{'class':'el__storyelement__gray'}).contents[0]
    print soup.find('p',{'class':'zn-body__paragraph speakable'}).contents[0]
    for counter,i in enumerate(soup.find_all('div',{'class':'zn-body__paragraph'})):
        if(counter >=  6):
            print counter-5,". ".lstrip(),i.contents[0].encode('utf-8').lstrip()
            print '\n'
        else:
            print i.contents[0].encode('utf-8').lstrip()

    
def main():
    html = getHtml()
    #print html[:500]
    soup = bs4Parsing(html)
    printContents(soup)
    
if __name__=="__main__":
        main()