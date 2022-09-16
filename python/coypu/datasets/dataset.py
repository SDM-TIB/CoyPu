import multiprocessing as mp
import joblib as jb
from tqdm import tqdm
from tqdm.contrib.concurrent import process_map

class Dataset():
    """Class for Dataset
    """

    def __init__(self, name, *args, **kwrgs):
        self.name = name

    def download(self, *args, **kwargs):
        pass

    def transform(self, *args, **kwargs):
        pass

    def get_sample(self, *args, **kwargs):
        pass

    def fix_error():
        pass

    def print_sample(self, *args, **kwargs):
        pass


class FastArrayProcessing():
    def __init__(self, func, array):
        self.n_workers = 2 * mp.cpu_count()
        self.func = func
        self.array = array
            
    def get_no_workers(self):
        return self.n_workers
    
    def set_no_workers(self, n):
        if n <= 2 * mp.cpu_count():
            self.n_workers = n
        print('No of workers more than 2*cpu_count, can not be set')
    
    def do_multiprocessing(self):
        p = mp.Pool(self.n_workers)
        return p.map(self.func, tqdm(self.array))
    
    def do_parallel_processing(self):
        result = jb.Parallel(n_jobs=self.n_workers, backend="multiprocessing")\
                 (jb.delayed(self.func)(value) for value in tqdm(self.array))
        return result
    
    def proc_batch(self, batch):
            return [self.func(value) for value in batch]
        
    def do_batch_processing(self):
        file_len = len(self.array)
        batch_size = round(file_len/self.n_workers)
        batches = [self.array[ix:ix+batch_size] for ix in tqdm(range(0, file_len, batch_size))]
        batch_outputs = jb.Parallel(self.n_workers, backend="multiprocessing")\
                       (jb.delayed(self.proc_batch)(batch) for batch in tqdm(batches))
        return [value for batch_output in batch_outputs for value in batch_output]
    
    def do_concurrent(self):
        batch_size = round(len(self.array)/self.n_workers)
        return process_map(self.func, self.array, max_workers=self.n_workers, chunksize=batch_size)


def main():
    pass

if __name__ == "__main__":
    main()
    

        
            
        
    
    
    
    
    
    
    
    
    
        
    
    
    