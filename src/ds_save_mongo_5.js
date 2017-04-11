use myDB;
show dbs;
show tables;
db.myCol.insert({"Ps":[{"id":"405", "이름":"js1"},{"id":"406", "이름":"js2"}]});
db.myCol.find({ "Ps.이름": "js1" });