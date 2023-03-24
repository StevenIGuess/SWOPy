from pymongo import MongoClient
import matplotlib.pyplot as plt
import urllib
import seaborn as sns

def create_plot(path, options):
    plt.switch_backend('agg')
    client = MongoClient(f"mongodb+srv://SwopyBot:{urllib.parse.quote(options['mongopassword'].encode('utf8'))}@swopy.hmzniu6.mongodb.net/?retryWrites=true&w=majority")
    db = client["swopy"]
    collection = db["homework"]
    cursor = collection.find({})
    count = {}
    for doc in cursor:
        if doc['name'].strip() in count.keys():
            count[doc['name'].strip()] += 1
        else:
            count[doc['name'].strip()] = 1
    data = count.values()
    labels = count.keys()

    colors = sns.color_palette('pastel')

    plt.pie(data, labels=labels, colors=colors, autopct='%.0f%%')
    plt.title("Verteilung der Hausaufgaben seit 24/03/2023")
    plt.savefig(path)


