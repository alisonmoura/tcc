import time
import numpy as np
from printer import Printer
from random import seed
from random import randint
from progress.spinner import Spinner

def import_all(src):
    return np.genfromtxt(src, delimiter=',')

def import_all_separately(src, printer=Printer()):
    pos = 1
    neg = -1
    
    data_pos = []
    data_neg = []
    
    printer.print_write('Loading dataset...')
    start = time.time()
    data_import = np.genfromtxt(src, delimiter=',')
    end = time.time()
    printer.print_write("Dataset imported in: %.2f seconds" % (end - start))
    
    printer.print_write('Filtering only positive datas...')
    start = time.time()
    for data in data_import:
        if(int(data[-1]) == pos): data_pos.append(data)
    end = time.time()
    printer.print_write("Finshed in: %.2f seconds" % (end - start))

    printer.print_write('Filtering only negative datas...')
    start = time.time()
    for data in data_import:
        if(int(data[-1]) == neg): data_neg.append(data)
    end = time.time()
    printer.print_write("Finshed in: %.2f seconds" % (end - start))
    
    return [np.array(data_pos), np.array(data_neg)]

def import_only_from(src, target, printer=Printer()):
    target = int(target)
    data_target = []
    
    # spinner = Spinner('Loading dataset ')
    # spinner.next()
    printer.print_write('Loading dataset...')
    start = time.time()
    data_import = np.genfromtxt(src, delimiter=',')
    end = time.time()
    printer.print_write("Dataset imported in: %.2f seconds" % (end - start))
    
    printer.print_write('Filtering only target datas...')
    start = time.time()
    for data in data_import:
        if(int(data[-1]) == target): data_target.append(data)
    end = time.time()
    printer.print_write("Finshed in: %.2f seconds" % (end - start))
    
    return np.array(data_target)

def import_major_and_minor_from(src, major_target, minor_target, printer=Printer()):
    major_target = int(major_target)
    minor_target = int(minor_target)
    data_target = []
    data_nontarget = []
    random_pos = set()
    
    printer.print_write('Loading dataset...')
    start = time.time()
    data_import = np.genfromtxt(src, delimiter=',')
    end = time.time()
    printer.print_write("Dataset imported in: %.2f seconds" % (end - start))
    
    printer.print_write('Filtering only target datas...')
    start = time.time()
    for data in data_import:
        if(int(data[-1]) == major_target): data_target.append(data)
    end = time.time()
    printer.print_write("Finshed in: %.2f seconds" % (end - start))

    printer.print_write('Filtering some non-target datas...')
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
    printer.print_write("Finshed in: %.2f seconds" % (end - start))
    
    return [np.array(data_target), np.array(data_nontarget)]