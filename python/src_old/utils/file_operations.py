from random import random
import pandas as pd
from requests import head  

def remove_quotes_csv(file, updated_file, header=False, index=False):
    df = pd.read_csv(file, header=None, encoding='utf-8')
    df.replace({'\'': ''}, regex=True, inplace=True)
    columns = df.iloc[0].to_list()
    print(columns)
    df.to_csv(updated_file, index=index, header=header)
    print (df.head(2))
    

def get_sample_data(file, updated_file, index=False):
    chunks = pd.read_csv(file, encoding='utf-8', chunksize=100000, low_memory=False)
    for chunk in chunks:
        df = chunk.sample(20000, random_state=1)
        # df = df.dropna(axis=1, how='all')
        break
    df.to_csv(updated_file, index=index)
    

  