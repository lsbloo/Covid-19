## Generator csv;
import os
import sys
import csv


class ReaderCSV(object):
    def __init__(self,PATH_CSV):
        self.path=PATH_CSV
    def get_transform(self,row):
        return row[0].split(",")
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
                    res.append(self.get_transform(row))
        
        if res != None:
            return res
        
        return None

