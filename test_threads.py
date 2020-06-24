#!/usr/bin/python3

import time
import threading
from printer import Printer
printer = Printer()

def print_time(threadName, delay):
   count = 0
   while count < 5:
    time.sleep(delay)
    count += 1
    print ("%s: %s" % ( threadName, time.ctime(time.time()) ))
    printer.print_write("%s: %s" % ( threadName, time.ctime(time.time())))
    printer.close_write()

try:
    thr1 = threading.Thread(target=print_time, args=("Thread-1", 2, ), daemon=True)
    thr2 = threading.Thread(target=print_time, args=("Thread-2", 3, ), daemon=True)
    
    thr1.start()
    thr2.start()

    thr1.join()
    thr2.join()

    print('All finished')

except:
   print ("Error: unable to start thread")