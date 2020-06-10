import time
import importer
import osvm
from printer import Printer

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
osvm.run(data_class, out_class, printer)
end = time.time()
printer.print_write("Finalizado em: %.2f segundos" % (end - start))
printer.close_write()