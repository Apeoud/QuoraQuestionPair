import csv
import pandas as pd
import numpy as np

csv.field_size_limit(2147483647)

# with open('/Users/duanshangfu/PycharmProjects/quoraKaggle/data/train.csv', newline='', encoding="utf-8") as csvfile:
#     spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
#     for row in spamreader:
#         print(', '.join(row))


def load_corpus(src):
    print('Loading Quora dataset.')
    df_train = pd.read_csv(src + 'train.csv')
    df_train['test_id'] = -1
    df_test = pd.read_csv(src + 'test.csv')
    df_test['id'] = -1
    df_test['qid1'] = -1
    df_test['qid2'] = -1
    df_test['is_duplicate'] = -1
    df = pd.concat([df_train, df_test])
    df['question1'] = df['question1'].fillna('')
    df['question2'] = df['question2'].fillna('')
    df['uid'] = np.arange(df.shape[0])
    df = df.set_index(['uid'])
    shapes = (df_train.shape[0], df_test.shape[0])
    print('Dataset loaded,', df_train.shape, df_test.shape)
    return df, shapes


if __name__ == "__main__":
    src = '/Users/duanshangfu/PycharmProjects/quoraKaggle/data/'
    df, shapes = load_corpus(src)
    print(df[2:5])