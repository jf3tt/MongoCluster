from pymongo import MongoClient
import datetime
import time
import random

client = MongoClient('10.10.10.5', 27017)
db = client.mongodb
numberCol = db.numbers

def insertData(): 
    genNumber = random.randint(0, 9)
    data = {"number": genNumber}
    getFirst = int(round(time.time() * 1000))
    singleRandom = numberCol.insert_one(data).inserted_id
    getSecond = int(round(time.time() * 1000))
    print ("Insert time:", getSecond - getFirst,"ms")
    print (data)

while True:
    insertData()
    time.sleep(0)
