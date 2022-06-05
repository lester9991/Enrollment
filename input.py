import pandas as pd
from pprint import pprint
df = pd.read_csv('bio.csv')
YEAR = '22'
BLOCK = '01'
batches = ['a', 'b', 'c', 'd']
batches_id = {}
for batch batc
batch_sort = {}
# print(df.to_string())
for batch in batches:
    batch_1 = df.index[df.batch == batch]
    batch_sort[batch] = batch_1
dict = {}
for batches in batch_sort:
    # print(batch_sort[batches])
    indices = batch_sort[batches]
    names = []
    dict1 = {}
    for index in indices:
        name = df.at[index, 'name']
        names.append(name)
        dict1[name] = index
    # print(dict1)
    names.sort()
    for name in names:

        dict[dict1[name]] = {'name': name, 'batch': batches}
pprint(dict)











# print(batch)
# def sort():

