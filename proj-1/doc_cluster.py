from init_var import *
from random import randint
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker

akld_matrix = [[0] * docnum for _ in range(docnum)]
with open('akld_matrix.txt', 'r') as akld_matrix_file:
    i = -1
    for row in akld_matrix_file:
        i += 1
        row = row.split()
        for j in range(len(row)):
            ele = row[j]
            akld_matrix[i][j] = float(ele)

# print(len(akld_matrix), len(akld_matrix[0]))

all_term = []
with open('all_term.txt', 'r') as all_term_file:
    for line in all_term_file:
        term = line.split()[0]
        all_term.append(term)

tf_idf_matrix = [[0] * len(all_term) for _ in range(docnum)]
with open('tf_idf_matrix.txt', 'r') as tf_idf_matrix_file:
    i = -1
    for row in tf_idf_matrix_file:
        i += 1
        row = row.split()
        for j in range(len(row)):
            ele = row[j]
            tf_idf_matrix[i][j] = float(ele)



with open('cluster_results.txt', 'w') as crf:
    pass

k = 5

groups = [[] for _ in range(k)]
grouped_doc = []
ungrouped_doc = [i for i in range(0, docnum)]

def chooseInitDoc():
    global groups, grouped_doc, ungrouped_doc
    groups = [[] for _ in range(k)]
    grouped_doc = []
    ungrouped_doc = [i for i in range(0, docnum)]

    first_doc = randint(0, docnum-1)
    groups[0].append(first_doc)

    ungrouped_doc.pop(first_doc)
    grouped_doc.append(first_doc)

    for i in range(1, k):
        distance_this = 0
        doc_tmp = 0
        idx_tmp = 0
        for new_idx, new_doc in enumerate(ungrouped_doc):
            distance_tmp = 0
            for old_doc in grouped_doc:
                distance_tmp += akld_matrix[new_doc][old_doc]

            if distance_tmp >= distance_this:
                distance_this = distance_tmp
                doc_tmp = new_doc
                idx_tmp = new_idx
        ungrouped_doc.pop(idx_tmp)
        grouped_doc.append(doc_tmp)
        groups[i].append(doc_tmp)
    with open('cluster_results.txt', 'a') as crf:
        print('initial doc id:', file=crf)
        print(*grouped_doc, sep=' ', file=crf)
        print('', file=crf)

# chooseInitDoc()

def updateGroups():
    global groups, grouped_doc, ungrouped_doc
    for i in range(len(ungrouped_doc)):
        new_idx = randint(0, len(ungrouped_doc)-1)
        new_doc = ungrouped_doc[new_idx]
        distance_this = float('inf')
        gid_tmp = 0
        for gid, group in enumerate(groups):
            distance_tmp = 0
            for gele in group:
                distance_tmp += akld_matrix[gele][new_doc]
            distance_tmp = distance_tmp / len(group)
            if distance_tmp <= distance_this:
                distance_this = distance_tmp
                gid_tmp = gid
        ungrouped_doc.pop(new_idx)
        groups[gid_tmp].append(new_doc)
        grouped_doc.append(new_doc)
# updateGroups()

id_list, sz_list = [], []
def outputGroups():
    global id_list, sz_list
    id_list, sz_list = [], []
    for gid, group in enumerate(groups):
        id_list.append(gid)
        sz_list.append(len(group))
        with open('cluster_results.txt', 'a') as crf:
            print(f'id: {gid}, size:{len(group)}', file=crf)
            print(*group, sep=' ', file=crf)
            # print('', file=crf)

if __name__ == '__main__':
    k_min, k_max = 2, 33
    k_list = [i for i in range(k_min, k_max+1)]
    plt.figure(figsize=(1200/72, 960/72), dpi=72)
    for idx, k in enumerate(k_list):
        with open('cluster_results.txt', 'a') as crf:
            print(f'k = {k}')
            print(f'\nk = {k}', file=crf)
        col_num = 4
        row_num = int((k_max - k_min + 1) / col_num) + 1
        # col_id = (idx) % col_num + 1
        plt.subplot(row_num, col_num, idx+1)
        chooseInitDoc()
        updateGroups()
        outputGroups()
        plt.bar(id_list, sz_list)
        plt.gca().set_xlim([id_list[0]-0.5, id_list[-1]+0.5])
        tick_step = int((k-1)/10) + 1
        locator = matplotlib.ticker.MultipleLocator(tick_step)
        plt.gca().xaxis.set_major_locator(locator)
        formatter = matplotlib.ticker.StrMethodFormatter("{x:.0f}")
        plt.gca().xaxis.set_major_formatter(formatter)
        plt.xlabel(f'k = {k}')
    plt.tight_layout()
    plt.savefig('./images/cluster_results.png', dpi=72, bbox_inches='tight')
    plt.show()