import pandas as pd
from requests import head

def remove_quotes_csv(file, updated_file):
    df = pd.read_csv(file, header=None)
    df.replace({'\'': ''}, regex=True, inplace=True)
    columns = df.iloc[0].to_list()
    print(columns)
    df.to_csv(updated_file, index=False, header=False)
    print (df.head(2))
    
def check
    
remove_quotes_csv('./data/minix.csv', './data/minix_updated.csv')
print (pd.read_csv('./data/minix_updated.csv').columns)
    