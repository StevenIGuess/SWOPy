from pymongo import MongoClient
import urllib


def push_to_db(options, name, text, subject):
    client = MongoClient(f"mongodb+srv://SwopyBot:{urllib.parse.quote(options['mongopassword'].encode('utf8'))}@swopy.hmzniu6.mongodb.net/?retryWrites=true&w=majority")
    db = client["swopy"]
    collection = db["homework"]
    post = {"name": name, "text": text, "class": subject}
    collection.insert_one(post)


