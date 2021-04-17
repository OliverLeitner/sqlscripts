#!/usr/bin/env python
from pymongo import MongoClient
mongo_client = MongoClient()

#print(mongo_client)

db = mongo_client.test
col = db.test

n = 1000000

myarr = []

sum = 1
for counter in range(1,n):
    doc = {}
    doc["value"] = sum + counter
    myarr += [doc]

col.insert_many(myarr)

# get the total numbers of docs inserted
total_docs = len(result.inserted_ids)

print ("total inserted:", total_docs)
print ("inserted IDs:", result.inserted_ids, "\n\n")
