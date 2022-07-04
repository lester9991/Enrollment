import pandas as pd
from pprint import pprint
import openpyxl


class Dataframe:
    batches = ['a', 'b', 'c', 'd']
    df = pd.read_csv('enrollment.csv', index_col=False)
    year = '22'
    block = '1'
    batches_id = {}
    for batch in batches:
        num = str(batches.index(batch) + 1).zfill(2)
        batches_id[batch] = num





    def create_csv(self, csv):
        self.df = pd.read_csv(csv, index_col=False)

    # pprint(batches_id)
    def create_register(self):
        """Gives register no to the students according to their name and batch"""

        batch_sort = {}
        # print(df.to_string())
        for batch in self.batches:
            batch_1 = self.df.index[self.df.batch == batch]
            batch_sort[batch] = batch_1
        dict = {}
        register = []
        for batches in batch_sort:
            # print(batch_sort[batches])
            indices = batch_sort[batches]
            names = []
            dict1 = {}

            for index in indices:
                name = self.df.at[index, 'name']
                names.append(name)
                dict1[name] = index
            # print(dict1)
            names.sort()
            for name in names:
                num = str(names.index(name) + 1).zfill(2)
                reg = self.year + self.block + self.batches_id[batches] + num
                dict[dict1[name]] = {'name': name, 'batch': batches, 'register': reg}
        dict = sorted(dict.items())
        # print(dict)
        for index in dict:
            register.append(int(index[1]['register']))
        # print(register)
        self.df['register no.'] = register
        df = self.df.sort_values('register no.')
        self.save_csv(df)

    def save_csv(self, df):
        self.df = df
        print(df)
        df.to_csv('enrollment.csv', index=False)

    def remove_register(self, register=int):


        index = self.df.index[self.df['register no.'] == int(register)][0]
        print(index)
        df = self.df.drop(index, axis=0)
        self.save_csv(df)

    def add_student(self, name=str, batch=str, phone_number=int):
        if batch not in self.batches:
            print('batch does not exist')
            return
        df2 = {'name': name, 'batch': batch, 'phone': phone_number}
        df = self.df.append(df2, ignore_index=True)
        self.save_csv(df)


    def search_student(self, register=int):
        register_no = self.df.index[self.df['register no.'] == int(register)]
        info = self.df.iloc[[register_no[0]]]
        print(info)
