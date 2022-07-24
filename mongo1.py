import pymongo
client = pymongo.MongoClient("mongodb+srv://rishcool:Rishcool#8691@cluster0.h5d5h.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)

d={
    "NAME":"rishabh"
    "email" : "urishabh6@gmail.com"
    "surname": "upadhyay"
}
db1 = client['mongotest']
coll=db1['test1']
coll.insert_one(d )