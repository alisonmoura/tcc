import sys
import time
import arff
import getopt
import numpy as np

def main(argv):
    filename = 'arfftocsv.py'
    inputfile = ''
    outputfile = ''
    try:
        opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
    except getopt.GetoptError:
        print('%s -i <inputfile> -o <outputfile>' % filename)
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print ('%s -i <inputfile> -o <outputfile>' % filename)
            sys.exit()
        elif opt in ("-i", "--ifile"):
            inputfile = arg
        elif opt in ("-o", "--ofile"):
            outputfile = arg

    if inputfile == '': raise RuntimeError("Input file name required, see in arfftocsv.pyt -h")
    
    if outputfile == '': outputfile = inputfile.replace('.arff', '.csv')

    print('Input file is %s' % inputfile)
    print('Output file is %s' % outputfile)

    print('Loading file...')
    start = time.time()
    arff_file = arff.load(inputfile)
    data_class = np.array(list(arff_file))
    # data_class[:,-1] = np.char.replace(data_class[:,-1], 'pos', '1')
    # data_class[:,-1] = np.char.replace(data_class[:,-1], 'neg', '-1')
    data_class[:,-1] = np.char.replace(data_class[:,-1], 'negative', '-1')
    data_class[:,-1] = np.char.replace(data_class[:,-1], 'irrelevant', '0')
    data_class[:,-1] = np.char.replace(data_class[:,-1], 'positive', '1')
    data_class[:,-1] = data_class[:,-1].astype(np.int)
    end = time.time()
    print('File loaded in %.2f seconds' % (end - start))
    # print('Exporting teste txt file...')
    # np.savetxt(inputfile.replace('.arff', '.txt'), data_class, fmt='%s')
    print('Exporting CSV file...')
    np.savetxt(outputfile, data_class, delimiter=",", fmt='%s')
    end = time.time()
    print('Done, ended in %.2f seconds' % (end - start))


if __name__ == "__main__":
   main(sys.argv[1:])
