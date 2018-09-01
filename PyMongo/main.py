import pymongo
import  datetime

from pymongo import MongoClient

current_date = datetime.datetime.now()

print(current_date)

# Create instantiation of MongoClient
client = MongoClient()

#client = MongoClient("localhost", 27017)     both are same

db = client.mydb

users = db.users

#uid = users.insert_one({"username": "abc", "Date": current_date})

old_date = datetime.datetime(2016, 9, 30)




# Finding data in mydb database
#print(users.find({"Date": {"$lte": old_date}}).count())
print(users.find({"Date": {"$exists": False}}).count())

"""
$lte = less than or equal to
$lt = less than
$gte = greater than or equal to
$gt = greater than
$exists = exists or not
$ne = not equal to

"""

# Entering Data in mydb database

#user1 = {"username": "Vikash", "password": "myverysecurepassword", "Hobbies": ["python", "games", "pizza"]}

#user_id = users.insert_one(user1).inserted_id