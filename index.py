import time
import importer
import osvm
import iforest
import mcd
import threading
import numpy as np
from printer import Printer
from functools import reduce

print('Importando datasets')
start = time.time()
print('reviews_polarity...')
reviews_polarity = importer.import_all_separately('datas/review_polarity.csv')
print('multi_domain_sentiment...')
multi_domain_sentiment = importer.import_all_separately('datas/multi-domain-sentiment.csv')
print('irish_economic_sentiment...')
irish_economic_sentiment = importer.import_all_separately('datas/irish-economic-sentiment.csv')
end = time.time()
print("\nImportação do dataset finalizada em: %.2f segundos" % (end - start))

# print(irish_economic_sentiment[0][:,-1])
# print(irish_economic_sentiment[1][:,-1])
# print(irish_economic_sentiment[2][:,-1])
# exit()

def sum_instances(a, b):
    result = a.shape[0] + b.shape[0]
    return result

def sum_attrs(a, b):
    result = a.shape[1] + b.shape[1]
    return result

def run_osvm_ova(chunks, dataset_name='unnamed_dataset'):
    print('OSVM ONE VERSUS ALL: %s' % dataset_name)
    printer = Printer(prefix="osvm_target_%s_" % dataset_name)
    start = time.time()
    printer.print_write("\n============================================")
    printer.print_write("============================================")
    printer.print_write("Algoritmo: One-Class Support Vector Machine (OSVM)")
    printer.print_write("Dataset: %s" % dataset_name)
    printer.print_write("# total de atributos: %d" % reduce(sum_attrs, chunks))
    printer.print_write("# total de exemplos: %d" % reduce(sum_instances, chunks))
    printer.print_write("Treino: Apenas com exemplos da classe de interese, estratégia One Versus All")
    printer.print_write("Teste: Com todos os exemplos")
    printer.print_write("============================================")
    printer.print_write("============================================\n")
    for i in range(len(chunks)):
        ova_start = time.time()
        printer.print_write("\n============================================")
        printer.print_write("Rodada %d do OVA" % i)
        printer.print_write("# total de atributos: %d" % chunks[i].shape[1])
        printer.print_write("# total de exemplos: %d" % chunks[i].shape[0])
        printer.print_write("============================================\n")
        osvm.run(chunks[i], np.concatenate([[elem for elem in chunk] for chunk in chunks]), printer)
        ova_end = time.time()
        printer.print_write("\nRodada %d do OVA finalizado em: %.2f segundos" % (i, (ova_end - ova_start)))
    end = time.time()
    printer.print_write("\nFinalizado em: %.2f segundos" % (end - start))
    printer.close_write()

thread_osvm_reviews_polarity = threading.Thread(
    target=run_osvm_ova, args=(reviews_polarity, 'reviews_polarity'), daemon=True)

thread_osvm_multi_domain_sentiment = threading.Thread(
    target=run_osvm_ova, args=(multi_domain_sentiment, 'multi_domain_sentiment'), daemon=True)

thread_irish_economic_sentiment = threading.Thread(
    target=run_osvm_ova, args=(irish_economic_sentiment, 'irish_economic_sentiment'), daemon=True)


thread_osvm_reviews_polarity.start()
thread_osvm_multi_domain_sentiment.start()
thread_irish_economic_sentiment.start()

thread_osvm_reviews_polarity.join()
thread_osvm_multi_domain_sentiment.join()
thread_irish_economic_sentiment.join()