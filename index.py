import time
import importer
import osvm
import iforest
import mcd
import threading
from printer import Printer


def run_osvm_reviews_polarity_target():
    print('Iniciando thread 1')
    printer = Printer(prefix="osvm-target-")
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
    [data_class, out_class] = importer.import_all_separately(
        'datas/review_polarity.csv')
    print('OSVM Thread 1: dataset importado')
    osvm.run(data_class, out_class, printer)
    end = time.time()
    printer.print_write("\nFinalizado em: %.2f segundos" % (end - start))
    printer.close_write()


def run_osvm_reviews_polarity_all():
    print('Iniciando thread 2')
    printer = Printer(prefix="osvm-all-")
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


def run_iforest_reviews_polarity_all():
    print('Iniciando thread 2')
    printer = Printer(prefix="iforest-")
    start = time.time()
    printer.print_write("\n============================================")
    printer.print_write("Algoritmo: Isolation Forest (iForest)")
    printer.print_write("Dataset: Reviews Polarity")
    printer.print_write("# total de atributos: 15.697")
    printer.print_write("# total de exemplos: 2.000")
    printer.print_write("# de exemplos positivos: 1.000")
    printer.print_write("# de exemplos negativos: 1.000")
    printer.print_write("Treino: Apenas com exemplos da classe de interese")
    printer.print_write("Teste: Com todos os exemplos")
    printer.print_write("============================================\n")
    [data_class, out_class] = importer.import_all_separately(
        'datas/review_polarity.csv')
    print('iForest Thread: dataset importado')
    iforest.run(data_class, out_class, printer)
    end = time.time()
    printer.print_write("\nFinalizado em: %.2f segundos" % (end - start))
    printer.close_write()

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


thread_osvm_reviews_polarity_target = threading.Thread(
    target=run_osvm_reviews_polarity_target, args=(), daemon=True)
thread_osvm_reviews_polarity_all = threading.Thread(
    target=run_osvm_reviews_polarity_all, args=(), daemon=True)
thread_iforest_reviews_polarity_all = threading.Thread(
    target=run_iforest_reviews_polarity_all, args=(), daemon=True)

thread_osvm_reviews_polarity_target.start()
thread_osvm_reviews_polarity_all.start()
thread_iforest_reviews_polarity_all.start()

thread_osvm_reviews_polarity_target.join()
thread_osvm_reviews_polarity_all.join()
thread_iforest_reviews_polarity_all.join()
