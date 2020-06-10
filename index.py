import time
import importer
import osvm
from printer import Printer

start = time.time()
printer = Printer()

# # OSVM POSITVE ONLY
# print("\n============================================")
# print("=============OSVM POSITIVE ONLY=============")
# print("============================================\n")
# data_class = importer.import_only_from('datas/review_polarity.csv', 1)
# osvm.run(data_class)

# # OSVM NEGATIVE ONLY
# print("\n============================================")
# print("=============OSVM NEGATIVE ONLY=============")
# print("============================================\n")
# data_class = importer.import_only_from('datas/review_polarity.csv', -1)
# osvm.run(data_class)

printer.print_write("\n============================================")
printer.print_write("==================OSVM MIX==================")
printer.print_write("============================================\n")
[data_class, out_class] = importer.import_all_separately('datas/review_polarity.csv', printer)
# print('data_class', data_class[:, -1])
# print('out_class', out_class[:, -1])
osvm.run(data_class, out_class, printer)

end = time.time()
printer.print_write("It took: %.2f seconds" % (end - start))
printer.close_write()