import re

import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.stem import PorterStemmer, WordNetLemmatizer

from init_var import *
#-----------------------------------------------------------------------------#


def tokenizeText(text):
    # s = "string. With. Punctuation?"
    text = re.sub(r'[^\w\s]', '', text)
    term_list = word_tokenize(text)
    return term_list

wnl = WordNetLemmatizer()
def lemmatizeTerm(term):
    term_out = term
    term_out = wnl.lemmatize(term_out, pos='n').lower()
    term_out = wnl.lemmatize(term_out, pos='v').lower()
    return term_out

def lemmatizeText(text):
    if   isinstance(text, str):
        text_out = lemmatizeTerm(text)
    elif isinstance(text, list):
        text_out = []
        for term in text:
            text_out.append(lemmatizeTerm(term))
    return text_out

all_term = []

def getAllTerm():
    for i in range(docnum):
        for header in header_list:
            # print('>>> Processing doc {:0>4} ... '.format(i))
            text = df[header][i]
            term_list = lemmatizeText(tokenizeText(text))
            for term in term_list:
                if term in all_term:
                    pass
                else:
                    all_term.append(term)
getAllTerm()
with open('all_term.txt', 'w', encoding='utf8') as all_term_file:
    print(*all_term, sep='\n', file=all_term_file)

tf_matrix = [[0] * len(all_term) for _ in range(docnum)]
def calcTF():
    # tf: term frequency
    # return a 2d array
    for i in range(docnum):
        for header in header_list:
            text = df[header][i]
            term_list = lemmatizeText(tokenizeText(text))
            for term in term_list:
                tf_matrix[i][all_term.index(term)] += 1
print('Calculating tf_matrix ...')
calcTF()
with open('tf_matrix.txt', 'w') as tf_matrix_file:
    for row in tf_matrix:
        print(*row, sep=' ', file=tf_matrix_file)