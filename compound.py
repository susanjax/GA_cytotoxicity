import random
import Decoder #this will import all the function present in another file
import pandas as pd
import numpy as np
from sklearn.preprocessing import  MinMaxScaler
from category_encoders import OrdinalEncoder

db = pd.read_csv('Database/Cytotoxicity.csv')
cell_type = db['Cell type']
test = db['test']
material = db['material']
time = db['time (hr)']
concentration = db['concentration (ug/ml)']
viability = 0
hd = db['Hydrodynamic diameter (nm)']
zeta = db['Zeta potential (mV)']

class Single:
    def __init__(self):
        self.part1 = []
        self.part2 = []
        self.cols1 = ['unnamed', 'Cell type', 'material', 'test']
        self.cols2 = ['del', 'time (hr)', 'concentration (ug/ml)', 'Hydrodynamic diameter (nm)', 'Zeta potential (mV)']

    def Coder_input_1(self):
        for a in range (200):
            self.part1.append(['0', random.choice(cell_type), random.choice(material), random.choice(test)]) #unnamed and material should be removed before inputing in model
        df1 = pd.DataFrame(self.part1, columns= self.cols1)
        return df1

    def Coder_input_2(self):
        for a in range (200):
            self.part2.append([0, random.choice(time), random.choice(concentration), random.choice(hd), random.choice(zeta)]) #first empty part should be removed before inputing in model
        df2 = pd.DataFrame(self.part2, columns=self.cols2)
        return df2

#print(Single().Coder_input_1())
#print(Single().Coder_input_2())

def input_1_transformation():
    to_transform = Single().Coder_input_1()
    decoder = Decoder.Decoder()
    transformed = decoder.transform(to_transform)
    #print('before_transform1', to_transform)
    return  transformed

#print('transform1',input_1_transformation())

def input_2_transformation():
    to_transform = Single().Coder_input_2()
    scaler = Decoder.Scaler()
    transformed = scaler.fit_transform(to_transform)
    #print('before_transform2', to_transform)
    return transformed
#print('transform2', input_2_transformation())

def transformed_input():
    input_1 = input_1_transformation().iloc[:, [1, 3]] # choosing only cell type and test
    input_2 = np.delete(input_2_transformation(), 0, axis=1) # removing unncessary column also the dataset is only array after transformation
    input_2 = pd.DataFrame(input_2, columns= [ 'time (hr)', 'concentration (ug/ml)', 'Hydrodynamic diameter (nm)', 'Zeta potential (mV)'] )
    compound_list = pd.concat([input_1, input_2], axis=1, join="inner")
    return compound_list

#print(transformed_input())