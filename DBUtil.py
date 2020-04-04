import pymongo

class GetDB:
    def __init__(self, dbName):
        self.dbName = dbName
    
    def getDatabase(self):
        client = pymongo.MongoClient("mongodb://localhost:27017/")
        db = client[dbName]
        if db:
            print('Connection Successful')
            return db
    