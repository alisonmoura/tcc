import time
import importer
import osvm

start = time.time()

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

# OSVM NEGATIVE ONLY
print("\n============================================")
print("==================OSVM MIX==================")
print("============================================\n")
[data_class, out_class] = importer.import_all_separately('datas/review_polarity.csv')
# print('data_class', data_class[:, -1])
# print('out_class', out_class[:, -1])
osvm.run(data_class, out_class)

end = time.time()
print("It took: %.2f seconds" % (end - start))