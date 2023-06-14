import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")

#database
database = client["employeeDB"]

#collection
collection = database["employeesDB"]

employeeCursor = collection.find({"LastName":"Smith"})

for employee in employeeCursor:
    print(employee)