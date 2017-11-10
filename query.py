from pymongo import MongoClient
from datetime import datetime
import time

client = MongoClient('10.10.10.5', 27017)
db = client.mongodb
numberCol = db.numbers

def getData():
    getFirst = int(round(time.time() * 1000))
    numbers = numberCol.find({"number": 10})
    numbersAll = numberCol.find({}).count()
    getSecond = int(round(time.time() * 1000))

#    def printDoc():
#        for document in numbers:
#            print (document)

    print ("Query time:", getSecond - getFirst,"ms")
#    print ("Documents with query:", printDoc() )
    print ("Total documents:", numbersAll, "\n")

while True:
    getData()
    time.sleep(1)
