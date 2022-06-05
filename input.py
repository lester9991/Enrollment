import pandas as pd
from pprint import pprint
import openpyxl
df = pd.read_csv('bio.csv')
YEAR = '22'
BLOCK = '1'
batches = ['a', 'b', 'c', 'd']
batches_id = {}
for batch in batches:
    num = str(batches.index(batch) + 1).zfill(2)
    batches_id[batch] = num
# pprint(batches_id)
batch_sort = {}
# print(df.to_string())
for batch in batches:
    batch_1 = df.index[df.batch == batch]
    batch_sort[batch] = batch_1
dict = {}
register = []
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
        num = str(names.index(name) + 1).zfill(2)
        reg = YEAR + BLOCK +batches_id[batches] + num
        dict[dict1[name]] = {'name': name, 'batch': batches, 'register': reg}
dict = sorted(dict.items())
# print(dict)
for index in dict:
    register.append(int(index[1]['register']))
# print(register)
df['register no.'] = register
df = df.sort_values('register no.')
print(df)
df.to_excel('enrollment.xlsx',sheet_name='Sheet1')








# print(batch)
# def sort():

