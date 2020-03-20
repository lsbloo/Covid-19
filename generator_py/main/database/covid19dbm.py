import pymongo


## Define o object database mongo db
## Define o object operador do mongo db

class DatabaseM(object):
    def __init__(self, URL_MONGO_DB):
        self.url = URL_MONGO_DB
    
    def get_instance(self):
        if self.url != None:
            self.client_instance = pymongo.MongoClient(self.url)
            print(self.client_instance.test)

            return self.client_instance
        
        return None
    



