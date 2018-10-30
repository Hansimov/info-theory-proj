import pandas as pd
from math import log

from init_var import *

#-----------------------------------------------------------------------------#

all_term = []
with open('all_term.txt', 'r') as all_term_file:
    for line in all_term_file:
        term = line.split()[0]
        all_term.append(term)

tf_matrix = [[0] * len(all_term) for _ in range(docnum)]
with open('tf_matrix.txt', 'r') as tf_matrix_file:
    i = -1
    for row in tf_matrix_file:
        i += 1
        row = row.split()
        for j in range(len(row)):
            ele = row[j]
            tf_matrix[i][j] = int(ele)

df_matrix = [0] * len(all_term)
def calcDF():
    # df: num of docs containing the term 't'
    # return a 1d array
    for col in range(len(tf_matrix[0])):
        for row in range(len(tf_matrix)):
            if tf_matrix[row][col] == 0:
                pass
            else:
                df_matrix[col] += 1
print('Calculating df_matrix ...')
calcDF()
with open('df_matrix.txt', 'w') as df_matrix_file:
    print(*df_matrix, sep='\n', file=df_matrix_file)

tf_idf_matrix = [[0] * len(all_term) for _ in range(docnum)]
def calcTFIDF():
    # tf: term frequency - inverse document frequency
    # return a 2d array
    for row in range(len(tf_idf_matrix)):
        for col in range(len(tf_idf_matrix[0])):
            tf_idf_matrix[row][col] = round(tf_matrix[row][col] * log(docnum / df_matrix[col]), 3)
    
print('Calculating tfidf_matrix ...')
calcTFIDF()
with open('tf_idf_matrix.txt', 'w') as tf_idf_matrix_file:
    for row in tf_idf_matrix:
        print(*row, sep=' ', file=tf_idf_matrix_file)

def calcKLD(vec1, vec2):
    # kld: KL divergence
    kld = 0
    for i in range(len(vec1)):
        if vec1[i]==0 or vec2[i]==0:
            pass
        else:
            kld += vec1[i] * log(vec1[i] / vec2[i])
    return kld

kld_matrix  = [[0] * docnum for _ in range(docnum)]
akld_matrix = [[0] * docnum for _ in range(docnum)]

def calcAKLD():
    # akld: average KL divergence
    for row in range(docnum):
        for col in range(docnum):
            kld_matrix[row][col] = calcKLD(tf_idf_matrix[row], tf_idf_matrix[col])

    for row in range(docnum):
        for col in range(docnum):
            akld_matrix[row][col] = round(1/2 * (kld_matrix[row][col] + kld_matrix[col][row]), 3)
print('Calculating alkd_matrix ...')
calcAKLD()
with open('akld_matrix.txt', 'w') as alkd_matrix_file:
    for row in akld_matrix:
        print(*row, sep=' ', file=alkd_matrix_file)


