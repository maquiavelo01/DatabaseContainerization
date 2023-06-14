import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")

#database
database = client["employeeDB"]

#collection
collection = database["employeesDB"]

filter = {"LastName":"Rose"}


collection.delete_one(filter)

employeeCursor = collection.find()

for employee in employeeCursor:

    print(employee)