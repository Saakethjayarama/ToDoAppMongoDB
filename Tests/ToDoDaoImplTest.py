import pymongo
import sys
from datetime import datetime
from DBUtil import GetDBUtil
from bson.objectid import ObjectId


class ToDoDaoImpl:
    def __init__(self):
        getDb = GetDBUtil("todolist")
        self.db = getDb.getDB()
        self.collection_todo = self.db['todo']
        self.id = 0

    def add(self, task):
        self.collection_todo.insert_one(task)

    def rem(self, id):
        self.collection_todo.delete_one({ "_id": id })

    def view(self):
        return self.collection_todo.find()

    def view_one(self, task):
        return self.collection_todo.find_one(task)

    def get(self, task):
        return self.collection_todo.find_one({"task": task})


todoDaoImpl = ToDoDaoImpl()

x = todoDaoImpl.view_one({'_id': ObjectId('5e897325956849bb3ecae67d')})
print(x)


# content = "Go to sleep"

# todoDaoImpl.add({"task": content, "dateCreated": datetime.utcnow()})



# tasks = todoDaoImpl.view()
# print(type(tasks))

# for task in tasks:
#     print(task)

# x = todoDaoImpl.rem()

# print(x.deleted_count)

# x = todoDaoImpl.get("code")
# print(x)




# x = col.find_one({'_id': objectid('5e897325956849bb3ecae67d')})
# print(x)