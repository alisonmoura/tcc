import time
import numpy as np

def import_all(src):
    return np.genfromtxt(src, delimiter=',')

def import_only_from(src, target):
    target = int(target)
    data_target = []
    
    print('Loading dataset...')
    start = time.time()
    data_import = np.genfromtxt(src, delimiter=',')
    end = time.time()
    print("Dataset imported in: %.2f seconds" % (end - start))
    
    print('Getting only target datas...')
    start = time.time()
    for data in data_import:
        if(int(data[-1]) == target): data_target.append(data)
    end = time.time()
    print("Finshed in: %.2f seconds" % (end - start))
    
    return np.array(data_target)