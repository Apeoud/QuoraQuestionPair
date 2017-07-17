import csv

csv.field_size_limit(2147483647)

with open('/Users/duanshangfu/PycharmProjects/quoraKaggle/data/train.csv', newline='', encoding="utf-8") as csvfile:
    spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in spamreader:
        print(', '.join(row))
