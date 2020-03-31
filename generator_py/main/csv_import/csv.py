## Generator csv;
import os
import sys
import csv
from models.model import Covid
from models.model import Metric
import csv



class ReaderCSV(object):
    def __init__(self,PATH_CSV):
        self.path=PATH_CSV
        
    def get_transform(self,row):
        return row[0].split(",")

    """
    retorna a lista de objetos validados do data_set;
    """
    @staticmethod
    def attendant_csv(result_data_set):
        list_covids = []
        for i in range(len(result_data_set)):
            param = result_data_set[i]
            if param[1] == "Cote d'Ivoire":
                param[1] = "Cote dIvoire"
            
            list_covids.append(Covid(param[0],param[1],param[2],param[3],param[4],param[5],param[6]))
        return list_covids


    def get_dataset(self,NAME_CSV):
        if self.path != None:
            archive_path = self.path +"/" + NAME_CSV
            archive = open(archive_path,'r')
            reader = csv.reader(archive)
            head = True
            res = []
            for row in reader:
                if head:
                    head = False
                else:
                    res.append(row)
    
        if res != None:
            return res
        
        return None

class Generator(object):

    def __init__(self,PATH_CSV):
        self.path = PATH_CSV

    def create_file(NAME_CSV):
        arc = self.path+"/"+NAME_CSV
        if os.path.exists(arc):
            return True
        else:
            a = open(arc,'w')
            a.clos()

    def validate_time_seconds(self,param):
        #print(param)
        return round(float(param),2)

    def gerenate(self,NAME_CSV,data_set):
        arc = self.path + "/" + NAME_CSV
        with open(arc,'w') as csvfile:
            filewriter = csv.writer(csvfile,delimiter=',',quotechar='|', quoting=csv.QUOTE_MINIMAL)
            filewriter.writerow(['sgbd_name','operation','time_duration_seconds','time_duration_min','quantity_lines'])
            for i in data_set:
                filewriter.writerow([i[1],i[2],self.validate_time_seconds(i[3]),self.validate_time_seconds(i[4]),i[5]])
        
    def get_dataset_csv(self,NAME_CSV):
        pass
    
    @staticmethod
    def get_dataset_recovery_operation(PATH_CSV,NAME_CSV):
        arc = PATH_CSV + "/" + NAME_CSV
        arquivo = open(arc)
        q=[]
        for i in csv.reader(arquivo):
            q.append(i)
        cont=0
        re = [] 
        for k in q[1:]:
            if k[1]=="recovery":
                re.append(k)
        return re

    @staticmethod
    def get_dataset_recovery_all_operation(PATH_CSV,NAME_CSV):
        arc = PATH_CSV + "/" + NAME_CSV
        arquivo = open(arc)
        q=[]
        for i in csv.reader(arquivo):
            q.append(i)
        cont=0
        re = [] 
        for k in q[1:]:
            if k[1]=="recovery-all-fast":
                re.append(k)
            if k[1]=="recovery" and k[0]=="psql":
                re.append(k)
        
        return re
    

    @staticmethod
    def get_dataset_insert_operation(PATH_CSV, NAME_CSV):
        arc = PATH_CSV + "/" + NAME_CSV
        arquivo = open(arc)
        q=[]
        for i in csv.reader(arquivo):
            q.append(i)
        cont=0
        for k in q[1:]:
            if k[1] == "recovery":
                q.remove(k)
            elif k[1] == "recovery-all-fast" and k[0] == 'mongo':
                q.remove(k)
        
        return q
    
    @staticmethod
    def get_len_type_csv(PATH_CSV, NAME_CSV):
        arc = PATH_CSV + "/" + NAME_CSV
        arquivo = open(arc)
        q=[]
        for i in csv.reader(arquivo):
            q.append(i)
        return len(q)

            





    
    