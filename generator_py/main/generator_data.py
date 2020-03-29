from csv_import.csv import ReaderCSV
from database.covid19db import Database
from database.covid19db import OperatorDatabase
from database.covid19dbm import DatabaseM
from database.covid19dbm import OperatorDatabaseM


from models.model import Covid

import os
import time
import timeit
import sys




def get_data_csv():
    try:
        list_result = []
        reader = ReaderCSV(os.environ.get('PATH_CSV'))
        result = reader.get_dataset(os.environ.get('NAME_CSV'))
        if result != None:
            list_result.append([reader,result])
            return list_result
    except Exception:
        print('error generate list csv dataset')
    finally:
        list_result.append([reader,result])
        return list_result

def choose_quantity_insert_psql(quantity_inserts):
    pass
def conversor(seconds):
    minutos = 'minutos: %f' %(seconds/60) 
    return minutos


def insert_data_psql(result_data_set,quantity_data_insert):
    try:
        if result_data_set != None:
            db = Database(os.environ.get('DATABASE_NAME'),os.environ.get('DATABASE_HOST'),os.environ.get('DATABASE_USER'),os.environ.get('DATABASE_PASSWORD'),os.environ.get('DATABASE_PORT'))
            operador_db = OperatorDatabase(db)
            operador_db.create_tables()
            if db.get_instance() != None:
                print("SIZE RECOVERY DATASET:" ,  len(result_data_set[0][0].attendant_csv(result_data_set[0][1])))
                recovery_data_set = result_data_set[0][0].attendant_csv(result_data_set[0][1])
                for i in range(quantity_data_insert):
                    operador_db.insert(recovery_data_set[i])

                
    except Exception as e:
        print('error inserting dataset in psql', e)

def recovery_data_mongo():
    db = DatabaseM(os.environ.get('URL_MONGO_DB'))
    operador_db = OperatorDatabaseM(db,'covid19')
    if db.get_instance() != None:
        names_collection =  operador_db.list_collections()
        return operador_db.get_collection(names_collection[0])

def insert_data_mongo(result_data_set,quantity_data_insert):
    try:
        if result_data_set != None:
            db = DatabaseM(os.environ.get('URL_MONGO_DB'))
            operador_db = OperatorDatabaseM(db,'covid19')
            if db.get_instance_collection() != None:
                print("SIZE RECOVERY DATASET:" ,  len(result_data_set[0][0].attendant_csv(result_data_set[0][1])))
                recovery_data_set = result_data_set[0][0].attendant_csv(result_data_set[0][1])
                for i in range(quantity_data_insert):
                    operador_db.insert(recovery_data_set[i])

    except Exception as e:
        print('error inserting dataset in mongodb', e)

def time_insert_data(init,fi):
    s = fi - init
    print('duração em segundos : %f' % (s))
    print('duração em  ' , conversor(s))


args = []
for parameter in sys.argv[1:]:
    args.append(parameter)

if args[0] == 'psql':
    if args[1] == 'insert':
        result_data_set = get_data_csv()
        if args[2].isnumeric:
            time_cal_psql_init = timeit.default_timer()
            insert_data_psql(result_data_set,int(args[2]))
            time_cal_psql_fim = timeit.default_timer()
            time_insert_data(time_cal_psql_init,time_cal_psql_fim)

if args[0] == "psql":
    if args[1] == 'recovery':
        pass


if args[0] == 'mongo':
    if args[1] == 'insert':
        result_data_set = get_data_csv()
        if args[2].isnumeric:
            time_cal_mongo_init = timeit.default_timer()
            insert_data_mongo(result_data_set,int(args[2]))
            time_cal_mongo_fim = timeit.default_timer()
            time_insert_data(time_cal_mongo_init,time_cal_mongo_fim)
    elif args[1] == 'recovery':
        time_cal_mongo_init = timeit.default_timer()
        recovery_data_mongo()
        time_cal_mongo_fim = timeit.default_timer()
        time_insert_data(time_cal_mongo_init,time_cal_mongo_fim)









