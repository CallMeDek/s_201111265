import urllib
import os
import oauth2 as oauth
import json

def getApiKey(keyPath):
    d=dict()
    f=open(keyPath,'r')
    for line in f.readlines():
        row=line.split('=')
        if(row[0]!='debug'):
            row0=row[0].split('.')
            d[row0[1].upper()]=row[1].strip()
    return d

# 1. key
keyPath=os.path.join(os.path.expanduser("~"),'Code/git/sd','twitter4j.properties')
key=getApiKey(keyPath)
# 2. oauth client
consumer = oauth.Consumer(key=key['CONSUMERKEY'], secret=key['CONSUMERSECRET'])
token=oauth.Token(key=key['ACCESSTOKEN'], secret=key['ACCESSTOKENSECRET'])
client = oauth.Client(consumer, token)

# 3. pymongo
from pymongo import MongoClient
Client = MongoClient('localhost:27017')
_db=Client.ds_twitter
_collection=_db.seoul
def saveDB(_data):
    _collection.insert(_data)

def readDB():
    for tweet in _collection.find():
        print tweet['id'],tweet['text']

# 4. file: NOTE to cast into string
_fname='src/ds_twitter_seoul_3.txt'
def saveFile(_fname,_data):
    fp=open(_fname,'a')
    fp.write(str(_data))
    #fp.write(_data+"\n")

# 5. json
_jfname='src/ds_twitter_seoul_3.json'
def saveJson(_fname,_data):
    import io
    with io.open(_fname, 'a', encoding='utf8') as json_file:
        _j=json.dumps(_data, json_file, ensure_ascii=False, encoding='utf8')
        json_file.write(_j+"\n")
def readJson(_fname):
    for line in open(_fname, 'r').readlines():
        _j=json.loads(line)
        #print _j['id'],_j['text']
        print _j['id']

# 6. twitter search
url = "https://api.twitter.com/1.1/search/tweets.json"
_ids=list()
_max_id=None
#_since_id=None
_count=200
_maxIter=20
_iter=0
while _iter<_maxIter:
    myparam={'q':'seoul','count':_count,'max_id':_max_id}
    #myparam={'q':'seoul','count':_count,'since_id':_since_id}
    mybody=urllib.urlencode(myparam)
    response, content = client.request(url+"?"+mybody, method="GET")
    tsearch_json = json.loads(content)
    print len(tsearch_json)
    for i,tweet in enumerate(tsearch_json['statuses']):
            #print tweet['id'],tweet['text']
            if(i%10==0):
                print i,tweet['id']
            saveJson(_jfname,tweet) # with quotes, this does not work!!
            saveFile(_fname,tweet)
            saveDB(tweet)
    _max_id=tweet['id']
    #_since_id=tweet['id']
    _ids.append(tweet['id'])
    _iter+=1

#print "-----reading back"
#readJson(_jfname)
#readDB()
print _ids