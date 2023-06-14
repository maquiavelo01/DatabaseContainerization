import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")

#database
database = client["employeeDB"]

#collection
collection = database["employeesDB"]

employee = collection.find_one({"LastName":"Rigby"})

print(employee)