import pymongo


## Define o object database mongo db
## Define o object operador do mongo db

class DatabaseM(object):
    def __init__(self, URL_MONGO_DB):
        self.url = URL_MONGO_DB

    def get_info(self):
        self.get_instance().test

    
    def get_instance(self):
        if self.url != None:
            self.client_instance = pymongo.MongoClient(self.url)
            return self.client_instance.python
        return None


    def get_instance_collection(self):
        if self.url != None:
            self.client_instance = pymongo.MongoClient(self.url)
            db = self.client_instance.python
            collection = db.covid
            return collection
        
        return None
    def lists(self):
        return self.get_instance_collection().list_indexes()



class OperatorDatabaseM(object):

    def __init__(self,DatabaseM,collection_name):
        self.collection_name=collection_name
        self.db = DatabaseM
    
    def insert(self,covid):
        post_insert = {
            "province_state": covid.province_state,
            "country_region": covid.country_region,
            "latitude": covid.latitude,
            "longitude:": covid.longitude,
            "date:": covid.date,
            "number_cases:": covid.number_cases,
            "status_case_type: ": covid.status_cases_type,
            "collection_name: ": self.collection_name
        }
        id_ = self.db.get_instance_collection().insert_one(post_insert).inserted_id
        

        return id_

    def get_collection(self,q):
        collection = self.db.get_instance_collection().find({})
        return collection
    
    def list_collections(self):
        return self.db.get_instance().list_collection_names()
    





    



