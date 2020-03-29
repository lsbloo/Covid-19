import psycopg2
import time


query_create_tables = [

    ('CREATE TABLE IF NOT EXISTS covid19 (id SERIAL PRIMARY KEY, province_state varchar(255), country_region varchar(255), latitude varchar(255), longitude varchar(255), date varchar(255), number_cases varchar(255), status_cases_type varchar(255))')
]


class Database(object):

    def __init__(self,database_name,database_host,database_user,database_password,database_port):
        self.database_name=database_name
        self.database_host=database_host
        self.database_user=database_user
        self.database_password=database_password
        self.database_port=database_port
    
    def get_instance(self):
        self.instance = psycopg2.connect(host=self.database_host,dbname=self.database_name,
        user=self.database_user,password=self.database_password,port=self.database_port)

        self.instance.autocommit=True

        if self.instance != None:
    
            return self.instance

        
        return None
    
class OperatorDatabase(object):

    def __init__(self,Database):
        self.database=Database
    

    def create_tables(self):
        cursor = self.database.get_instance().cursor()
        for i in range(len(query_create_tables)):
            result = cursor.execute(query_create_tables[i])
        cursor.close()
    
    def insert(self,covid):
        cursor = self.database.get_instance().cursor()
        data = [covid.province_state,covid.country_region,covid.latitude,covid.longitude,covid.date,covid.number_cases,covid.status_cases_type]
        sql_ = ("INSERT INTO covid19 (province_state,country_region,latitude,longitude,date,number_cases,status_cases_type) VALUES ('%s','%s','%s','%s','%s','%s','%s')"%(
            data[0],data[1],data[2],data[3],data[4],data[5],data[6]
        ))

        cursor.execute(sql_)
        cursor.close()
    
    

    