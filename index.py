import time
import importer
import osvm
import iforest
import mcd
import threading
from printer import Printer

def run_osvm_1():
    print('Iniciando thread 1')
    printer = Printer()
    start = time.time()
    printer.print_write("\n============================================")
    printer.print_write("Algoritmo: One-Class Support Vector Machine (OSVM)")
    printer.print_write("Dataset: Reviews Polarity")
    printer.print_write("# total de atributos: 15.697")
    printer.print_write("# total de exemplos: 2.000")
    printer.print_write("# de exemplos positivos: 1.000")
    printer.print_write("# de exemplos negativos: 1.000")
    printer.print_write("Treino: Apenas com exemplos da classe de interese")
    printer.print_write("Teste: Com todos os exemplos")
    printer.print_write("============================================\n")
    [data_class, out_class] = importer.import_all_separately('datas/review_polarity.csv')
    print('OSVM Thread 1: dataset importado')
    osvm.run(data_class, out_class, printer)
    end = time.time()
    printer.print_write("\nFinalizado em: %.2f segundos" % (end - start))
    printer.close_write()
    

def run_osvm_2():
    print('Iniciando thread 2')
    printer = Printer()
    start = time.time()
    printer.print_write("\n============================================")
    printer.print_write("Algoritmo: One-Class Support Vector Machine (OSVM)")
    printer.print_write("Dataset: Reviews Polarity")
    printer.print_write("# total de atributos: 15.697")
    printer.print_write("# total de exemplos: 2.000")
    printer.print_write("# de exemplos positivos: 1.000")
    printer.print_write("# de exemplos negativos: 1.000")
    printer.print_write("Treino: Com todos os exemplos")
    printer.print_write("Teste: Com todos os exemplos")
    printer.print_write("============================================\n")
    data_class = importer.import_all('datas/review_polarity.csv')
    print('OSVM Thread 2: dataset importado')
    osvm.run(data_class, [], printer)
    end = time.time()
    printer.print_write("\nFinalizado em: %.2f segundos" % (end - start))
    printer.close_write()

# # The model is probably best trained on examples that exclude outliers. 
# # In this case, we fit the model on the input features for examples from the majority class only.
# printer.print_write("\n============================================")
# printer.print_write("Algoritmo: Isolation Forest (iForest)")
# printer.print_write("Dataset: Reviews Polarity")
# printer.print_write("# total de atributos: 15.697")
# printer.print_write("# total de exemplos: 2.000")
# printer.print_write("# de exemplos positivos: 1.000")
# printer.print_write("# de exemplos negativos: 1.000")
# printer.print_write("Treino: Apenas com exemplos da classe de interese")
# printer.print_write("Teste: Com todos os exemplos")
# printer.print_write("============================================\n")
# [data_class, out_class] = importer.import_all_separately('datas/review_polarity.csv')
# iforest.run(data_class, out_class, printer)

# # If the input variables have a Gaussian distribution, 
# # then simple statistical methods can be used to detect outliers.
# # It is unusual to have such well-behaved data, but if this is the case for your dataset, 
# # or you can use power transforms to make the variables Gaussian, 
# # then this approach might be appropriate.
# # The model can be fit on the input data from the majority class only 
# # in order to estimate the distribution of “normal” data in an unsupervised manner.
# printer.print_write("\n============================================")
# printer.print_write("Algoritmo: Minimum Covariance Determinant (MCD)")
# printer.print_write("Dataset: Reviews Polarity")
# printer.print_write("# total de atributos: 15.697")
# printer.print_write("# total de exemplos: 2.000")
# printer.print_write("# de exemplos positivos: 1.000")
# printer.print_write("# de exemplos negativos: 1.000")
# printer.print_write("Treino: Apenas com exemplos da classe de interese")
# printer.print_write("Teste: Com todos os exemplos")
# printer.print_write("============================================\n")
# [data_class, out_class] = importer.import_all_separately('datas/review_polarity.csv')
# mcd.run(data_class, out_class, printer)


thr_osvm_1 = threading.Thread(target=run_osvm_1, args=(), daemon=True)
thr_osvm_2 = threading.Thread(target=run_osvm_2, args=(), daemon=True)

thr_osvm_1.start()
thr_osvm_2.start()

thr_osvm_1.join()
thr_osvm_2.join()