import time
import numpy as np
import importer
import scipy.stats as stats
from sklearn.model_selection import KFold
from sklearn.svm import OneClassSVM
from sklearn.model_selection import RandomizedSearchCV
from sklearn.metrics import f1_score

start = time.time()

data_class = importer.import_only_from('datas/review_polarity.csv', 1)

X = np.delete(data_class, -1, axis=1)
y = data_class[:,-1]

print(data_class.shape, X.shape, y.shape)
# print(X[:,-1], y)
# exit()

clf = OneClassSVM(gamma='scale', nu=0.01)
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

    # n_error_train = y_pred_train[y_pred_train == -1].size
    # n_error_test = y_pred_test[y_pred_test == -1].size

    n_error_train = (y_pred_train != y_train).sum()
    n_error_test = (y_pred_test != y_test).sum()
    f1_train_score = f1_score(y_train, y_pred_train, pos_label=-1)
    f1_test_score = f1_score(y_test, y_pred_test, pos_label=-1)

    print("Train error: {:d}".format(n_error_train))
    print("Test error: {:d}".format(n_error_test))
    print('Train F1 Score: %.3f' % f1_train_score)
    print('Test F1 Score: %.3f' % f1_test_score)

end = time.time()

print("It took: %.2f seconds" % (end - start))