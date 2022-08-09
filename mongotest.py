import pymongo
client = pymongo.MongoClient("mongodb+srv://lucifer:qwerty1234@cluster0.gvrg76u.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)

d = {
    'name' : 'tanmay',
    'email' : 'tanmay@gmail.com',
    'surname' : 'biswas'
}
db1 = client['mongo_db']
coll = db1['test']
coll.insert_one(d)