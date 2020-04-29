import time
import arff
import numpy as np
import scipy.stats as stats
from sklearn.model_selection import KFold
from sklearn.svm import OneClassSVM
from sklearn.model_selection import RandomizedSearchCV

start = time.time()

arff_file = arff.load('datas/review_polarity.arff')
data_class = np.array(list(arff_file))

print(data_class[:,-1])
data_class[:,-1] = np.char.replace(data_class[:,-1], 'pos', '1')
data_class[:,-1] = np.char.replace(data_class[:,-1], 'neg', '-1')
data_class[:,-1] = data_class[:,-1].astype(np.int)
print(data_class[:,-1])

X = np.delete(data_class, -1, axis=1)
y = data_class[:,-1]

print(data_class.shape, X.shape, y.shape)

clf = OneClassSVM(gamma='scale')
kf = KFold(n_splits=5)
kf.get_n_splits(X)

param_dist = {
    'kernel': ['linear', 'poly', 'rbf', 'sigmoid'],
    'gamma': ['scale', 'auto'],
    'nu': stats.uniform(.0, .99),
    'shrinking': [True, False]
    }

n_inter = 20
# clf = RandomizedSearchCV(clf, param_distributions=param_dist, n_iter=n_inter, cv=5, scoring="accuracy")

print(kf)
for train_index, test_index in kf.split(X):
    print("Rodada")
    X_train, X_test = X[train_index], X[test_index]
    y_train, y_test = y[train_index], y[test_index]

    clf = clf.fit(X_train, y_train)
    y_pred_train = clf.predict(X_train)
    y_pred_test = clf.predict(X_test)

    n_error_train = y_pred_train[y_pred_train == -1].size
    n_error_test = y_pred_test[y_pred_test == -1].size

    print("Train error: {:d}".format(n_error_train))
    print("Test error: {:d}".format(n_error_test))

end = time.time()

print("It took: %.2f seconds" % (end - start))