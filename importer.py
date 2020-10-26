import time
import numpy as np
from random import seed
from random import randint

def load_csv(src, delimiter=','):
    data_text = np.genfromtxt(src, delimiter=delimiter)
    return data_text

def import_all(src):
    return load_csv(src)

def import_all_separately(src):

    datas_dict = {}
    datas_result = []
    
    print('Loading dataset...')
    start = time.time()
    data_import = load_csv(src)
    end = time.time()
    print("Dataset imported in: %.2f seconds" % (end - start))
    
    print('Filtering dataset...')
    start = time.time()
    for data in data_import:
        data_label = int(data[-1])
        if(data_label in datas_dict): datas_dict[data_label].append(data)
        else: 
            datas_dict[data_label] = []
            datas_dict[data_label].append(data)

    end = time.time()
    print("Finshed in: %.2f seconds" % (end - start))

    for key in datas_dict:
        datas_result.append(np.array(datas_dict[key]))
    
    return datas_result

def import_only_from(src, target):
    target = int(target)
    data_target = []
    
    print('Loading dataset...')
    start = time.time()
    data_import = load_csv(src)
    end = time.time()
    print("Dataset imported in: %.2f seconds" % (end - start))
    
    print('Filtering dataset...')
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
    data_import = load_csv(src)
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