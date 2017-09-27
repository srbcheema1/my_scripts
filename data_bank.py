import pickle
import os

class filer:
    def __init__(self,file_name):
        self.file_name = file_name
        if not os.path.exists(file_name):
            fout = open(file_name,'wb')
            self.data = dict()
            pickle.dump(self.data,fout)
            fout.close()
        self.load()

    def load(self):
        self.data = pickle.load(open(self.file_name,'rb'))
        return self.data

    def __getitem__(self,index):
        if(index in self.data):
            return self.data[index]
        else:
            return False
    def __setitem__(self,index,value):
        self.data[index]=value

    def __contains__(self,value):
        return value in self.data

    def get(self):
       return True

    def save(self):
        pickle.dump(self.data,open(self.file_name,'wb'))
    

