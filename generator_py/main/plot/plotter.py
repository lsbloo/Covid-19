import pandas as pd



class Pandas(object):

    def __init__(self,PATH_CSV,NAME_CSV):
        self.q= PATH_CSV+"/"+NAME_CSV
        self.metrics = pd.read_csv(self.q,names=['sgbd_name','operation','time_duration_seconds','time_duration_min','quantity_lines'])
    
    def print(self):
        print(self.metrics.head())

    def columns(self):
        return self.metrics.columns
    
    def header(self,param):
        return self.metrics.head(param)
    
    

