import psycopg2
import time

tables_name = [
     {'schemas-1' : 'covid19'},
     {'schemas-2': 'metrics_generator'}
    ]

query_create_tables = [

    ('CREATE TABLE IF NOT EXISTS covid19 (id SERIAL PRIMARY KEY, province_state varchar(255), country_region varchar(255), latitude varchar(255), longitude varchar(255), date varchar(255), number_cases varchar(255), status_cases_type varchar(255))'),
    ('CREATE TABLE IF NOT EXISTS metrics_generator (id SERIAL PRIMARY KEY, sgbd_name varchar(255), operation varchar(255), time_duration_seconds varchar(255), time_duration_min varchar(255), quantity_lines varchar(255))')
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
    

    def validate_insert_metrics(self,metric):
        cursor = self.database.get_instance().cursor()
    
        sql_ = "SELECT * FROM metrics_generator where operation='%s' and sgbd_name='%s' and quantity_lines='%s'"%(metric.operation,metric.sgbd_name,metric.quantity_lines)
        cursor.execute(sql_)
        q= []
        result = []
        for i in cursor.fetchall():
            q.append(i)

        if len(q) == 0:
            result.append([True,0])
            
        else:
            result.append([False,q[0][0]])
        
        
        return result


    def insert_metrics(self,metric):
        q = self.validate_insert_metrics(metric)
        if q[0][0]:
            cursor = self.database.get_instance().cursor()
            data= [metric.sgbd_name, metric.operation, metric.time_duration_seconds, metric.time_duration_min,metric.quantity_lines]
            sql_ =("INSERT INTO metrics_generator (sgbd_name,operation,time_duration_seconds,time_duration_min,quantity_lines) VALUES ('%s','%s','%s','%s','%s')")%(
                data[0],data[1],data[2],data[3],data[4]
            )
            cursor.execute(sql_)
            cursor.close()
            return True
        else:
            # update metrics
            cursor = self.database.get_instance().cursor()
            data= [metric.sgbd_name, metric.operation, metric.time_duration_seconds, metric.time_duration_min,metric.quantity_lines]
            sql_update_query_insert = "update metrics_generator set time_duration_seconds=%s,time_duration_min=%s,quantity_lines=%s where id=%s"
            cursor.execute(sql_update_query_insert,(metric.time_duration_seconds,metric.time_duration_min,metric.quantity_lines, q[0][1]))
            cursor.close()
            return True

        return False

    def get_all_metrics(self):
        cursor = self.database.get_instance().cursor()
        sql_ = ('SELECT * FROM metrics_generator')
        cursor.execute(sql_)
        resul = []
        for i in cursor.fetchall():
            resul.append(i)
        if len(resul) >= 1:
            return resul
        return None
    
    def get_by_qnt(self,qnt):
        cursor = self.database.get_instance().cursor()
        sql_ = ('SELECT * FROM covid19')
        cursor.execute(sql_)
        re = []
        cont=0
        for i in cursor.fetchall():
            cont+=1
            re.append(i)
            if cont == qnt:
                break
        
        cursor.close()

        return re
    
    def get_by_split(self,split):
        cursor = self.database.get_instance().cursor()
        q=[]
        for i in split:
            sql_ = "SELECT * FROM covid19 where id=%s"%(i)
            cursor.execute(sql_)
            for k in cursor.fetchall():
                q.append(k)
        

    def get_obj_by(self):
        pass

    def drop_table_schemas_01(self):
        cursor = self.database.get_instance().cursor()
        table_name = tables_name[0].get('schemas-1')
        sql_ = "DROP TABLE %s"%(table_name)
        cursor.execute(sql_)
        cursor.close()
        return True

    def drop_table_schemas_02(self):
        cursor = self.database.get_instance().cursor()
        table_name = tables_name[1].get('schemas-2')
        sql_ = "DROP TABLE %s" %(table_name)
        cursor.execute(sql_)
        cursor.close()
        return True

        




    
    

    