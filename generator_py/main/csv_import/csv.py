## Generator csv;
import os
import sys
import csv
from models.model import Covid


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

