
import os
# create files for object hashmap saves in mongo db;



class ManipulatorFile(object):

    def __init__(self,name_txt):
        self.name=name_txt
    
    def create(self):
        sub = os.environ.get('HOME')
        sub+="/"
        sub += self.name
        arch = open(sub,'w')
        arch.close()


    @staticmethod
    def create_file(name):

        sub = os.environ.get('HOME')
        sub+="/"
        sub += name
        arch = open(sub,'w')
        arch.close()

    
    def write_file(self,object_id):
        sub = os.environ.get('HOME')
        sub+="/"
        sub += self.name
        arch = open(sub,'a')
        arch.write(str(object_id) + "\n" )
        arch.close()

        
    def reader_file(self):
        sub = os.environ.get('HOME')
        sub+="/"
        sub += self.name
        
        arch = open(sub,'r')
        ids = []
        for linha in arch:
            
            linha = linha.rstrip()
            ids.append(linha)
        arch.close()
        return ids

