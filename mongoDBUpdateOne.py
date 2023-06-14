import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")

#database
database = client["employeeDB"]

#collection
collection = database["employeesDB"]

filter = {"LastName":"Rose"}
newvalues = { "$set": { "Age": 32 } }


collection.update_one(filter, newvalues)

employeeCursor = collection.find()

for employee in employeeCursor:

    print(employee)
