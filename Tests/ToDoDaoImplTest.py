import pymongo
import sys
from datetime import datetime
from DBUtil import GetDBUtil

class ToDoDaoImpl:
    def __init__(self):
        getDb = GetDBUtil("todolist")
        self.db = getDb.getDB()
        self.collection_todo = self.db['todo']

    def add(self, task):
        self.collection_todo.insert_one(task)

    def rem(self, task):
        return self.collection_todo.delete_one({ "task": task})

    def view(self):
        return self.collection_todo.find()
    
    def get(self, task):
        return self.collection_todo.find_one({"task": task})


todoDaoImpl = ToDoDaoImpl()

# content = "Go to sleep"

# todoDaoImpl.add({"task": content, "dateCreated": datetime.utcnow()})



# tasks = todoDaoImpl.view()
# print(type(tasks))

# for task in tasks:
#     print(task)

x = todoDaoImpl.rem(4)

print(x.deleted_count)

# x = todoDaoImpl.get("code")
# print(x)

