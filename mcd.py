import warnings
warnings.filterwarnings('always')

import time
import numpy as np
import scipy.stats as stats
from printer import Printer
from sklearn.model_selection import KFold
from sklearn.covariance import EllipticEnvelope
from sklearn.model_selection import RandomizedSearchCV
from sklearn.metrics import f1_score
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score

def run(data_class, out_class=[], printer=Printer()):
    has_out = np.any(out_class)
    start = time.time()
    
    print('Target data shape: (%d,%d)' % (data_class.shape[0], data_class.shape[1]) )
    X = np.delete(data_class, -1, axis=1)
    y = data_class[:,-1]
    # print(y)

    if(has_out):
        print('Has out class: Yes')
        print('Out data shape: (%d,%d)' % (out_class.shape[0], out_class.shape[1]) )
        X_out = np.delete(out_class, -1, axis=1)
        y_out = out_class[:,-1]
        # print(y_out)

    print(data_class.shape, X.shape, y.shape)

    clf = EllipticEnvelope(
        contamination=0.01, 
        random_state=0, 
        store_precision=True, 
        assume_centered=False, 
        support_fraction=None
        )
        
    kf = KFold(n_splits=5)
    kf.get_n_splits(X)

    param_dist = {
        'contamination': stats.uniform(.0, .99),
        }

    n_inter = 20
    clf = RandomizedSearchCV(clf, param_distributions=param_dist, n_iter=n_inter, cv=5, scoring="accuracy")

    f1_scores = []
    precision_scores = []
    recall_scores = []

    print(kf)
    for train_index, test_index in kf.split(X):
        
        X_train, X_test = X[train_index], X[test_index]
        y_train, y_test = y[train_index], y[test_index]

        if(has_out):
           X_test = np.concatenate((X_test, X_out)) 
           y_test = np.concatenate((y_test, y_out)) 

        clf = clf.fit(X_train, y_train)
        y_pred_test = clf.predict(X_test)

        print(y_test)
        print(y_pred_test)

        n_error_test = (y_pred_test != y_test).sum()
        f1_test_score = f1_score(y_test, y_pred_test, pos_label=-1)
        precision_test_score = precision_score(y_test, y_pred_test)
        recall_test_score = recall_score(y_test, y_pred_test)

        printer.print_write("\n=============ITERATION SCORES=============\n")

        printer.print_write("Test error: {:d}".format(n_error_test))
        printer.print_write('Test F1 Score: %.3f' % f1_test_score)
        printer.print_write('Test Precision Score: %.3f' % precision_test_score)
        printer.print_write('Test Recall Score: %.3f' % recall_test_score)

        f1_scores.append(f1_test_score)
        precision_scores.append(precision_test_score)
        recall_scores.append(recall_test_score)

    f1_scores = np.array(f1_scores)
    precision_scores = np.array(precision_scores)
    recall_scores = np.array(recall_scores)

    printer.print_write("\n=============FINAL SCORES=============\n")
    printer.print_write("F1 Score Final: %f" % (f1_scores.sum()/f1_scores.size))
    printer.print_write("Precision Score Final: %f" % (precision_scores.sum()/precision_scores.size))
    printer.print_write("Recall Score Final: %f" % (recall_scores.sum()/recall_scores.size))

    end = time.time()
    printer.print_write("\n=============TIME=============\n")
    printer.print_write("It took: %.2f seconds" % (end - start))