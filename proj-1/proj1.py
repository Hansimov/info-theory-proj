import pandas as pd

# At 2018.10
# By Hansimov

    # 1. Apply the relative entropy rule to cluster different papers into different groups according to their title, abstract, keywords.
    # 2. Besides the relative entropy rule, please apply another method to achieve the target in 1.

if __name__ == '__main__':
    # title, authors, groups, keywords, topics, abstract
    # https://aaai.org/Conferences/AAAI-18/aaai18keywords/

    df = pd.read_csv('./aaai14.csv', sep=',', encoding='utf8')
    for i in range(0, len(df)):
        print('=== {:0>4} ==='.format(i))

        # title, abstract, keywords
        title = df['title'][i]
        abstract = df['abstract'][i]
        keywords = df['keywords'][i]
        # topics = df['topics'][i]
        # groups = df['groups'][i]

        print(title)
        # print('-----------------------------------')
        # print(abstract)
        print('-----------------------------------')
        print(keywords)
        # print('-----------------------------------')
        # print(topics)
        # print('-----------------------------------')
        # print(groups)
        # print('-----------------------------------')
        print('')
