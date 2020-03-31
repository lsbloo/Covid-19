from csv_import.csv import ReaderCSV
from csv_import.csv import Generator
from database.covid19db import Database
from database.covid19db import OperatorDatabase
from database.covid19dbm import DatabaseM
from database.covid19dbm import OperatorDatabaseM
from plot.plotter import Pandas
from models.model import Covid
from models.model import Metric
from generator_arch.manipulatorfile import ManipulatorFile
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

import os
import time
import timeit
import sys


def check_arch():
    sub = os.environ.get('HOME')
    sub += "/"
    sub += 'objects_mongo.txt'
    if os.path.exists(sub):
        pass
    else:
        ManipulatorFile.create_file('objects_mongo.txt')
check_arch()


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
    minutos = seconds/60 
    return minutos


def get_all_metrics_collected():
    db = Database(os.environ.get('DATABASE_NAME'),os.environ.get('DATABASE_HOST'),os.environ.get('DATABASE_USER'),os.environ.get('DATABASE_PASSWORD'),os.environ.get('DATABASE_PORT'))
    operador_db = OperatorDatabase(db)
    result_collects = operador_db.get_all_metrics()
    if result_collects != None:
        generator = Generator(os.environ.get('HOME'))
        generator.gerenate('metrics.csv',result_collects)
        return result_collects
    return None


def drop_table_psql_schemas01():
    try:
        db = Database(os.environ.get('DATABASE_NAME'),os.environ.get('DATABASE_HOST'),os.environ.get('DATABASE_USER'),os.environ.get('DATABASE_PASSWORD'),os.environ.get('DATABASE_PORT'))
        operador_db = OperatorDatabase(db)
        operador_db.drop_table_schemas_01()
        return True

    except Exception as e:
        print('Error drop table psql schemas-01', e)
        return False
def recovery_data_psql(quantity_line):
    try:
        db = Database(os.environ.get('DATABASE_NAME'),os.environ.get('DATABASE_HOST'),os.environ.get('DATABASE_USER'),os.environ.get('DATABASE_PASSWORD'),os.environ.get('DATABASE_PORT'))
        operador_db = OperatorDatabase(db)
        re = operador_db.get_by_qnt(quantity_line)
        spliter=[]
        for k in re:
            spliter.append(k[0])
        operador_db.get_by_split(spliter)

        print('Size Recovery dataset psql', len(re))
        return re

    except Exception as e:
        print('Error Recovery data set psql', e)


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

def drop_collection_mong():
    db = DatabaseM(os.environ.get('URL_MONGO_DB'))
    operador_db = OperatorDatabaseM(db,'covid19')
    if db.get_instance()!=None:
        operador_db.drop_collection()
        return True
    return False


def recovery_data_mongo():
    db = DatabaseM(os.environ.get('URL_MONGO_DB'))
    operador_db = OperatorDatabaseM(db,'covid19')
    if db.get_instance() != None:
        names_collection =  operador_db.list_collections()
        s =[]
        for i in operador_db.get_collection(names_collection[0]):
            s.append(i)
        print("Size: Recovery Data Mongo DB: "  , len(s))
        return s


def recovery_data_mongo_one_one():
    db = DatabaseM(os.environ.get('URL_MONGO_DB'))
    operador_db = OperatorDatabaseM(db,'covid19')
    manipulator = ManipulatorFile('objects_mongo.txt')

    if db.get_instance() != None:
        names_collection =  operador_db.list_collections()
        q = operador_db.get_collection_hash(manipulator.reader_file())
        print("Size: Recovery Data Mongo DB:" , len(q))
        return q

        
    
def insert_data_mongo(result_data_set,quantity_data_insert):
    try:
        if result_data_set != None:
            manipulator = ManipulatorFile('objects_mongo.txt')
            db = DatabaseM(os.environ.get('URL_MONGO_DB'))
            operador_db = OperatorDatabaseM(db,'covid19')
            if db.get_instance_collection() != None:
                print("SIZE RECOVERY DATASET:" ,  len(result_data_set[0][0].attendant_csv(result_data_set[0][1])))
                recovery_data_set = result_data_set[0][0].attendant_csv(result_data_set[0][1])
                for i in range(quantity_data_insert):
                    obj = operador_db.insert(recovery_data_set[i])
                    manipulator.write_file(obj)


    except Exception as e:
        print('error inserting dataset in mongodb', e)

def time_insert_data(init,fi):
    s = fi - init
    print('duração em segundos : %f' % (s))
    print('duração em minutos: ' , conversor(s))
    return [s,conversor(s)]


def insert_metrics(metric):
    db = Database(os.environ.get('DATABASE_NAME'),os.environ.get('DATABASE_HOST'),os.environ.get('DATABASE_USER'),os.environ.get('DATABASE_PASSWORD'),os.environ.get('DATABASE_PORT'))
    operador_db = OperatorDatabase(db)
    inserted = operador_db.insert_metrics(metric)
    return inserted


def quot_insert(times_mb,times_psql,lines_mb,lines_psql):
    quot = {
        "SGBD":['mongo','psql'],
        "times": [times_mb,times_psql],
        "lines": [lines_mb,lines_psql] 
    }
    return quot


def drop_metrics():
    db = Database(os.environ.get('DATABASE_NAME'),os.environ.get('DATABASE_HOST'),os.environ.get('DATABASE_USER'),os.environ.get('DATABASE_PASSWORD'),os.environ.get('DATABASE_PORT'))
    operador_db = OperatorDatabase(db)
    return operador_db.drop_table_schemas_02()


def main():
    args = []
    for parameter in sys.argv[1:]:
        args.append(parameter)

    if args[0] == 'collect':
        print('collect size', len(get_all_metrics_collected()))

        if args[1] == 'drop':
            print("Drop Table Schema-2", drop_metrics())
            

    if args[0] == 'plot':
        if args[1] == 'insert':
            q = Generator.get_dataset_insert_operation(os.environ.get('HOME'),'metrics.csv')
            mPandas = Pandas(os.environ.get('HOME'),'metrics.csv')

            data_set= q[1:]
            times_mb=[]
            times_psql=[]
            lines_mb =[]
            lines_psql=[]

            for i in data_set:
                if i[0] == 'mongo':
                    times_mb.append(i[2])
                    lines_mb.append(i[4])
                elif i[0] == 'psql':
                    times_psql.append(i[2])
                    lines_psql.append(i[4])
            
            quot = quot_insert(times_mb,times_psql,lines_mb,lines_psql)
            df = mPandas.data_frame(quot)
            
            print(df)

            time_and_mongo= [quot.get('times')[0],quot.get('lines')[0]]
            time_and_psql = [quot.get('times')[1], quot.get('lines')[1]]

            time_mong_x = time_and_mongo[0]
            line_mongo_y = time_and_mongo[1]
            
            time_psql_x = time_and_psql[0]
            line_psql_y = time_and_psql[1]

            plt.bar( time_mong_x, line_mongo_y, label = 'MongoDB', color = 'r')
            plt.bar( time_psql_x, line_psql_y , label = 'Postgres-SQL', color = 'b')
            plt.legend()
            plt.title('Desempenho de Inserção')
            plt.savefig(os.environ.get('HOME')+"/metric_insert.pdf")
            plt.show()

        elif args[1] == 'recovery':
            q = Generator.get_dataset_recovery_operation(os.environ.get('HOME'),'metrics.csv')
            mPandas = Pandas(os.environ.get('HOME'),'metrics.csv')

            data_set = q
            times_mb=[]
            times_psql=[]
            lines_mb =[]
            lines_psql=[]

            for i in data_set:
                if i[0] == 'mongo':
                    times_mb.append(i[2])
                    lines_mb.append(i[4])
                elif i[0] == 'psql':
                    times_psql.append(i[2])
                    lines_psql.append(i[4])
            
            quot = quot_insert(times_mb,times_psql,lines_mb,lines_psql)
            df = mPandas.data_frame(quot)
            
            print(df)

            time_and_mongo= [quot.get('times')[0],quot.get('lines')[0]]
            time_and_psql = [quot.get('times')[1], quot.get('lines')[1]]

            time_mong_x = time_and_mongo[0]
            line_mongo_y = time_and_mongo[1]
            
            time_psql_x = time_and_psql[0]
            line_psql_y = time_and_psql[1]

            plt.bar( time_mong_x, line_mongo_y, label = 'MongoDB', color = 'r')
            plt.bar( time_psql_x, line_psql_y , label = 'Postgres-SQL', color = 'b')
            plt.legend()
            plt.title('Desempenho de Leitura')
            plt.savefig(os.environ.get('HOME')+"/metric_recovery.pdf")
            plt.show()
        elif args[1] == 'recovery-all':
            q = Generator.get_dataset_recovery_all_operation(os.environ.get('HOME'),'metrics.csv')
            mPandas = Pandas(os.environ.get('HOME'),'metrics.csv')
            data_set = q
            times_mb=[]
            times_psql=[]
            lines_mb =[]
            lines_psql=[]
            for i in data_set:
                if i[0] == 'mongo':
                    times_mb.append(i[2])
                    lines_mb.append(i[4])
                elif i[0] == 'psql':
                    times_psql.append(i[2])
                    lines_psql.append(i[4])
            
            quot = quot_insert(times_mb,times_psql,lines_mb,lines_psql)
            df = mPandas.data_frame(quot)
            
            print(df)

            time_and_mongo= [quot.get('times')[0],quot.get('lines')[0]]
            time_and_psql = [quot.get('times')[1], quot.get('lines')[1]]

            time_mong_x = time_and_mongo[0]
            line_mongo_y = time_and_mongo[1]
            
            time_psql_x = time_and_psql[0]
            line_psql_y = time_and_psql[1]

            plt.bar( time_mong_x, line_mongo_y, label = 'MongoDB', color = 'r')
            plt.bar( time_psql_x, line_psql_y , label = 'Postgres-SQL', color = 'b')
            plt.legend()
            plt.title('Desempenho de Leitura')
            plt.savefig(os.environ.get('HOME')+"/metric_recovery_all.pdf")
            plt.show()



    if args[0] == 'psql':
        if args[1] == 'insert':
            result_data_set = get_data_csv()
            if args[2].isnumeric:
                time_cal_psql_init = timeit.default_timer()
                insert_data_psql(result_data_set,int(args[2]))
                time_cal_psql_fim = timeit.default_timer()
                metrics_time = time_insert_data(time_cal_psql_init,time_cal_psql_fim)
                obj_m = Metric(args[0],args[1],metrics_time[0],metrics_time[1],args[2])
                result = insert_metrics(obj_m)
                print('Metric Insertd: ', result)


    if args[0] == "psql":
        if args[1] == 'recovery':
            time_cal_psql_init = timeit.default_timer()
            re = recovery_data_psql(int(args[2]))
            time_cal_psql_fim = timeit.default_timer()
            metrics_time = time_insert_data(time_cal_psql_init,time_cal_psql_fim)
            obj_m = Metric(args[0],args[1],metrics_time[0],metrics_time[1],len(re))
            result = insert_metrics(obj_m)
            print('Metric Insertd: ', result)
        
        if args[1] == 'drop':
            re = drop_table_psql_schemas01()
            print('Drop Table Schema-1: ', re )

    

    if args[0] == 'mongo':
        if args[1] == 'insert':
            result_data_set = get_data_csv()
            if args[2].isnumeric:
                time_cal_mongo_init = timeit.default_timer()
                insert_data_mongo(result_data_set,int(args[2]))
                time_cal_mongo_fim = timeit.default_timer()
                metrics_time = time_insert_data(time_cal_mongo_init,time_cal_mongo_fim)
                obj_m = Metric(args[0],args[1],metrics_time[0],metrics_time[1],args[2])
                result = insert_metrics(obj_m)

        elif args[1] == 'recovery-all-fast':
            time_cal_mongo_init = timeit.default_timer()
            q = recovery_data_mongo()
            time_cal_mongo_fim = timeit.default_timer()
            time_insert_data(time_cal_mongo_init,time_cal_mongo_fim)
            metrics_time = time_insert_data(time_cal_mongo_init,time_cal_mongo_fim)
            obj_m = Metric(args[0],args[1],metrics_time[0],metrics_time[1],len(q))
            result = insert_metrics(obj_m)

        elif args[1] == 'recovery':
            time_cal_mongo_init = timeit.default_timer()
            q = recovery_data_mongo_one_one()
            time_cal_mongo_fim = timeit.default_timer()
            time_insert_data(time_cal_mongo_init,time_cal_mongo_fim)
            metrics_time = time_insert_data(time_cal_mongo_init,time_cal_mongo_fim)
            obj_m = Metric(args[0],args[1],metrics_time[0],metrics_time[1],len(q))
            result = insert_metrics(obj_m)

        elif args[1] == 'drop':
            print("Drop Collection: ", drop_collection_mong())

def show_menu():
    print("---------------------------------------------------------------------------")
    print(" Operations: ")
    print()
    print("Insert Mongo DB or PSQL")
    print()
    print("python3 generate_data.py psql insert <number_lines>")
    print("python3 generate_data.py psql mongo <number_lines>")
    print()
    print("Recovery")
    print()
    print("python3 generate_data.py mongo recovery")
    print("python3 generate_data.py psql recovery <number_lines>")
    print()
    print("Drop")
    print("python3 generate_data.py psql drop")
    print("python3 generate_data.py mongo drop")
    print()
    print("Collect")
    print("python3 generate_data.py collect")
    print("python3 generate_data.py collect drop")
    print()
    print("Ploting")
    print("python3 generate_data.py plot insert")
    print("python3 generate_data.py plot recovery")
    print("python3 generate_data.py plot recovery-all")
    print()
    print()
    print("---------------------------------------------------------------------------")

    print("Scripter: lsbloo")



try:
    show_menu()

    main()
    
except Exception as e:
    print('Error Input Param', e)

        









