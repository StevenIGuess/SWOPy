from pymongo import MongoClient
import urllib


def initdb(options):
    client = MongoClient("mongodb+srv://cezarst42:" + urllib.parse.quote(options['mongopassword'].encode('utf8')) + "@cluster0.zp5lk.mongodb.net/?authSource=admin")
    print(urllib.parse.quote(options['mongopassword'].encode('utf8')))
    db = client.test
    collection = db.test_collection
    posts = collection.posts
    post = {"Teacher" : "ich", "text": "mogus"}
    post_id = posts.insert_one(post).inserted_id
    print(post_id)


