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

# tf_idf_matrix = np.array(tf_idf_matrix)

from sklearn.cluster import KMeans, SpectralClustering, DBSCAN

# def kmeansCluster():
#     k = 3
#     kmeans_cluster = KMeans(n_clusters=k).fit(tf_idf_matrix)
#     # 每个样本所属的簇
#     print(kmeans_cluster.labels_)
#     # 来评估簇的个数是否合适，距离越小说明簇分的越好，选取临界点的簇个数
#     # print(f'k={k} {kmeans_cluster.inertia_}')
 
# # kmeansCluster()

with open('cluster_results_2.txt', 'w') as crf:
    pass

k = 5
groups = [[] for _ in range(k)]
def spectralCluster(k):
    global groups
    groups = [[] for _ in range(k)]
    # spectral_cluster = SpectralClustering(n_clusters=k).fit(tf_idf_matrix)
    spectral_cluster = SpectralClustering(n_clusters=k).fit(tf_idf_matrix)
    # print(spectral_cluster.labels_)
    for doc in range(len(spectral_cluster.labels_)):
        gid = spectral_cluster.labels_[doc]
        groups[gid].append(doc)
        # print(doc, spectral_cluster.labels_[doc])
    # for gid, group in enumerate(groups):
    #     print(f'id: {gid}, size:{len(group)}')
    #     print(*group, sep=' ')

id_list, sz_list = [], []
def outputGroups():
    global id_list, sz_list
    id_list, sz_list = [], []
    for gid, group in enumerate(groups):
        id_list.append(gid)
        sz_list.append(len(group))
        with open('cluster_results_2.txt', 'a') as crf:
            print(f'[id: {gid}, size: {len(group)}]', file=crf)
            print(*group, sep=' ', file=crf)
            # print('', file=crf)

# spectralCluster(k)

# def dbscanCluster():
#     dbscan_cluster = DBSCAN(eps=80, min_samples=2).fit(tf_idf_matrix)
#     print(dbscan_cluster.labels_)

# dbscanCluster()

if __name__ == '__main__':
    k_min, k_max = 2, 33
    k_list = [i for i in range(k_min, k_max+1)]
    plt.figure(figsize=(1200/72, 960/72), dpi=72)
    for idx, k in enumerate(k_list):
        with open('cluster_results_2.txt', 'a') as crf:
            print(f'k = {k}')
            print(f'\nk = {k}', file=crf)
        col_num = 4
        row_num = int((k_max - k_min + 1) / col_num) + 1
        # col_id = (idx) % col_num + 1
        try:
            spectralCluster(k)
            outputGroups()
            plt.subplot(row_num, col_num, idx+1)
            tick_step = int((k-1)/10) + 1
            plt.bar(id_list, sz_list)
            locator = matplotlib.ticker.MultipleLocator(tick_step)
            plt.gca().xaxis.set_major_locator(locator)
            formatter = matplotlib.ticker.StrMethodFormatter("{x:.0f}")
            plt.gca().xaxis.set_major_formatter(formatter)
            plt.gca().set_xlim([id_list[0]-0.5, id_list[-1]+0.5])
            plt.xlabel(f'k = {k}')
        except Exception as excp:
            pass

    plt.tight_layout()
    plt.savefig('./images/cluster_results_2.png', dpi=72, bbox_inches='tight')
    plt.show()