from random import random
import pandas as pd
import requests
import base64
import time
import functools

def replace(self, updated_file: str, replace: dict = {'\'': ''},
            header: bool = False, index=False):
    df = pd.read_csv(self.file_inpath, encoding='utf-8')
    df.replace(replace, regex=True, inplace=True)
    df.to_csv(updated_file, index=index, header=header)
    print('preview data after removig quotes')
    print(df.head(2))
    del df


def get_auth(func):
    def wrapper(self,  query, ret_format):
        return func(self,  query, ret_format)
    return wrapper

def get_sample_data(self, updated_file: str, sample_rows: int = 20000,
                    chunksize: int = 100000, random_state: int = 1,
                    index: bool = False):
    chunks = pd.read_csv(self.file_inpath, chunksize=chunksize,
                         encoding='utf-8', low_memory=False)
    for chunk in chunks:
        df = chunk.sample(sample_rows, random_state=random_state)
        break
    df.to_csv(updated_file, index=index)
    del df

def get_auth_os2(func):
    @functools.wraps(func)
    def wrapper(self, *args, **kwargs):
        url = self.url + "/auth/realms/cmem/protocol/openid-connect/token"
        payload = 'grant_type=client_credentials&client_id={}&client_secret={}'\
            .format(self.id_or_user, self.pass_or_secret)

        headers = {
                    'Content-Type': 'application/x-www-form-urlencoded'
                }

        response = requests.request("POST", url, headers=headers, data=payload)

        if response.status_code == 200:
            self.auth = 'Bearer ' + response.json()['access_token']
        
        return func(self, *args, **kwargs)
    return wrapper

def get_auth_basic(func):
    @functools.wraps(func)
    def wrapper(self, *args, **kwargs):
        usr_pass = self.id_or_user + ':' + self.pass_or_secret
        self.auth =  "Basic {}".format(base64.b64encode(usr_pass.encode()).decode())
        return func(self, *args, **kwargs)
    return wrapper

def timer(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        time_pre = time.time()
        ret = func(*args, **kwargs)
        print('Total time taken by {} function: {}'.format(func.__name__,time.time()-time_pre))
        return ret
    return wrapper

