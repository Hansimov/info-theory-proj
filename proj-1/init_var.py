# At 2018.10
# By Hansimov

'''
Task:
    1. Apply the relative entropy rule to cluster different papers into different groups according to their title, abstract, keywords.
    2. Besides the relative entropy rule, please apply another method to achieve the target in 1.

- 用Python实现文档聚类
    http://python.jobbole.com/85481/
    http://brandonrose.org/clustering

- Clustering US Laws using TF-IDF and K-Means
    https://beckernick.github.io/law-clustering/

- AAAI-14 KEYWORDS (MAIN TECHNICAL TRACK)
    http://www.aaai.org/Conferences/AAAI/2014/aaai14keywords.php

- Python 文本数据分析初学指南
    https://datartisan.gitbooks.io/begining-text-mining-with-python/content/

- 机器学习算法与Python实践之（五）k均值聚类（k-means）
    https://blog.csdn.net/zouxy09/article/details/17589329

- 使用scikit-learn进行KMeans文本聚类
    https://blog.razrlele.com/p/1614

- k-means+python︱scikit-learn中的KMeans聚类实现( + MiniBatchKMeans)
    https://blog.csdn.net/sinat_26917383/article/details/70240628

- 使用K-means及TF-IDF算法对中文文本聚类并可视化
    https://www.ioiogoo.cn/2018/05/31/使用K-means及TF-IDF算法对中文文本聚类并可视化/

'''

#-----------------------------------------------------------------------------#

def warnidle(*args, **kwargs):
    pass
import warnings
warnings.warn = warnidle


import pandas as pd

# title, authors, groups, keywords, topics, abstract
df = pd.read_csv('./aaai14.csv', sep=',', encoding='utf8')

# header_list = ['title', 'keywords'] #, 'abstract']
header_list = ['title', 'keywords', 'abstract']

docnum = len(df)