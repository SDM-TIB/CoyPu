from random import random
import pandas as pd



class CsvData():
    def __init__(self, file_inpath:str, *args, **kwargs):
        self.file_inpath = file_inpath
        
    def replace(self, updated_file:str, replace:dict={'\'': ''}, header:bool=False, index=False):
        df = pd.read_csv(self.file_inpath, encoding='utf-8')
        df.replace(replace, regex=True, inplace=True)
        df.to_csv(updated_file, index=index, header=header)
        print('preview data after removig quotes')
        print (df.head(2))
        del df
        
    
    def get_sample_data(self, updated_file:str, sample_rows:int=20000, chunksize:int=100000, random_state:int=1, index:bool=False):
        chunks = pd.read_csv(self.file_inpath, chunksize=chunksize, encoding='utf-8', low_memory=False)
        for chunk in chunks:
            df = chunk.sample(sample_rows, random_state=random_state)
            break
        df.to_csv(updated_file, index=index)
        del df
        
    

  