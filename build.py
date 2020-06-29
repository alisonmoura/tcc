import shutil
import os

if not os.path.isdir('dist'):
    os.mkdir('dist')
else: 
    shutil.rmtree('dist')
    os.mkdir('dist')


shutil.copy('./index.py', './dist/index.py')
shutil.copy('./printer.py', './dist/printer.py')
shutil.copy('./importer.py', './dist/importer.py')
shutil.copy('./osvm.py', './dist/osvm.py')
shutil.copy('./iforest.py', './dist/iforest.py')
shutil.copy('./mcd.py', './dist/mcd.py')
shutil.copy('./requirements.txt', './dist/requirements.txt')
shutil.copytree('./datas', './dist/datas')