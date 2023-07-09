from pymongo import MongoClient

db_connection = input("Enter db connection: ")

client = MongoClient(db_connection)
db = client['forum_example']  
collection = db['forum_posts'] 

db.drop_collection(collection)

client.close()