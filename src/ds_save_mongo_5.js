use myDB
show dbs
show tables
#db.myCol.insert({"Persons":[{"id":"405", u"이름":"js1"}, {"id":"406", u"이름":"js2"}]})
db.myCol.find({"Persons.이름":"js1"})
#db.myCol.remove({u"Persons.이름":"js1"})