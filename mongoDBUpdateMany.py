import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")

#database
database = client["employeeDB"]

#collection
collection = database["employeesDB"]

filter = {"LastName":"Smith"}
newvalues = { "$set": { "Department": "Computer Science" } }


collection.update_many(filter, newvalues)

employeeCursor = collection.find()

for employee in employeeCursor:

    print(employee)
