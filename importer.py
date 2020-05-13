import time
import numpy as np
from random import seed
from random import randint
from progress.spinner import Spinner

def import_all(src):
    return np.genfromtxt(src, delimiter=',')

def import_only_from(src, target):
    target = int(target)
    data_target = []
    
    # spinner = Spinner('Loading dataset ')
    # spinner.next()
    print('Loading dataset...')
    start = time.time()
    data_import = np.genfromtxt(src, delimiter=',')
    end = time.time()
    print("Dataset imported in: %.2f seconds" % (end - start))
    
    print('Filtering only target datas...')
    start = time.time()
    for data in data_import:
        if(int(data[-1]) == target): data_target.append(data)
    end = time.time()
    print("Finshed in: %.2f seconds" % (end - start))
    
    return np.array(data_target)

def import_major_and_minor_from(src, major_target, minor_target):
    major_target = int(major_target)
    minor_target = int(minor_target)
    data_target = []
    data_nontarget = []
    random_pos = set()
    
    print('Loading dataset...')
    start = time.time()
    data_import = np.genfromtxt(src, delimiter=',')
    end = time.time()
    print("Dataset imported in: %.2f seconds" % (end - start))
    
    print('Filtering only target datas...')
    start = time.time()
    for data in data_import:
        if(int(data[-1]) == major_target): data_target.append(data)
    end = time.time()
    print("Finshed in: %.2f seconds" % (end - start))

    print('Filtering some non-target datas...')
    start = time.time()
    seed(1)
    while len(data_nontarget) < len(data_import)/10:
        # sortea posição
        pos = randint(0, len(data_import)-1)
        data = data_import[pos]
        if(int(data[-1]) == minor_target and not pos in random_pos): 
            data_nontarget.append(data)
            random_pos.add(pos)
    end = time.time()
    print("Finshed in: %.2f seconds" % (end - start))
    
    return [np.array(data_target), np.array(data_nontarget)]