#!/usr/bin/env python
import sys
from cassandra.cluster import Cluster
clstr=Cluster()

def printf(format, *args):
    sys.stdout.write(format % args)

session=clstr.connect()
#session.execute("create keyspace mykeyspace with replication={'class': 'SimpleStrategy', 'replication_factor' : 3};")

session=clstr.connect('mykeyspace')
qry= '''
create table students (
   studentID int,
   name text,
   age int,
   marks int,
   primary key(studentID)
);'''
#session.execute(qry)

nquery = 'DESC tables;'
#session.execute(nquery)

# insert some data
n = 1000000

insert_query = "INSERT INTO mykeyspace.students(studentID,name,age,marks) values()"

sum = 1
for counter in range(2,n):
    doc = {}
    doc["studentID"] = sum + counter
    doc["name"] = "oliver leitner"
    doc["age"] = doc["studentID"]
    doc["marks"] = 5
    values = "{id},'{name}',{age},{marks}".format(id = doc["studentID"], name = doc["name"], age = doc["age"], marks = doc["marks"])
    session.execute("INSERT INTO mykeyspace.students(studentID,name,age,marks) values({val})".format(val = values))




