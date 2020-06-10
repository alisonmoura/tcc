import time
import os
current_milli_time = lambda: int(round(time.time() * 1000))

class Printer:
    
    def __init__(self):
        self.buffer = []

    def print_write(self,message):
        print(message)
        self.buffer.append(message)

    def close_write(self):
        file_name = str(current_milli_time())
        file_path = "results/" + file_name + ".txt"
        file_stream = open(file_path,"a") 
        for line in self.buffer:
            file_stream.writelines(line) 
        file_stream.close() 
        print("Result saved on {0}".format(os.getcwd() + '/' + file_path))
