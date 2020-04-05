import pymongo

class GetDBUtil:
    def __init__(self, dbName):
        self.dbName = dbName
    
    def getDB(self):
        client = pymongo.MongoClient("mongodb://localhost:27017/")
        db = client[self.dbName]
        if db:
            # print('Connection Successful')
            return db
    