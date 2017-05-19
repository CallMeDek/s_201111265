
import requests

def get_jsonData_url():
    _url = "https://raw.githubusercontent.com/jokecamp/FootballData/master/World%20Cups/all-world-cup-players.json"
    rResponse = requests.get(_url)
    my_json = ""
    if rResponse.status_code == 200:
        my_json = rResponse.json()
    return my_json

def save_data_into_MongoDB(data):
    import pymongo
    from pymongo import MongoClient
    
    client = MongoClient('localhost:27017')
    db = client.myDB
    
    my_dict = {}
    my_list = []
    for i in range(0, len(data)):
        key_list = data[i].keys()
        for j in range(0, len(key_list)):
            key = key_list[j]
            value = data[i].get(key)
            my_dict[key] = value
            my_list.append(my_dict)
            my_dict = {}
        db.myDek.insert_one({
            ('%s'%(i)) : my_list
        })
        my_list = []

def main():
    _json = get_jsonData_url()
    save_data_into_MongoDB(_json)

if __name__=="__main__":
    print "\n\nIt uses functions of itself\n\n"
    main()
else:
    print "\n\nModule is attached\n\n"