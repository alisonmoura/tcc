from scipy.io import arff
import pandas as pd
import time

current_milli_time = lambda: int(round(time.time() * 1000))

now = current_milli_time()

[data, headers] = arff.loadarff('datas/review_polarity.arff')
df = pd.DataFrame(data)

ended = current_milli_time()

print("It took: {:f} secounds".format(ended/1000))

print(df.head())