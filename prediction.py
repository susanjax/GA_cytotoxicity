import random
import pandas as pd
from compound import transformed_input
import joblib


column = ['normal_cell', 'cancer_cell', 'test', 'time (hr)', 'concentration (ug/ml)', 'Hydrodynamic diameter (nm)', 'Zeta potential (mV)', 'fitness']
List_of_normal_cell = [1, 2, 3, 4, 6, 7, 8, 9, 11, 12, 13, 14, 16, 17, 18, 19, 21, 22, 23, 24, 26, 27, 28, 29, 31, 32, 33, 34, 36, 37, 38, 39, 41, 42, 43, 44, 46, 47, 48, 49, 51,52, 53, 54, 55, 56, 57,58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88]
List_of_cancer_cell = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]

trained_model = joblib.load('ML_models/Trained_model.joblib')
# sample = compound.transformed_input()

def Viability_prediction():
    sample = transformed_input()
    global_list = []
    #sam = compound.transformed_input()
    for a in range(sample.shape[0]):
        sample1 = sample.iloc[a].values.tolist()
        if List_of_normal_cell.count(sample1[0]) == True:
            normal = [sample1[0]]
            normal_cell_viability = trained_model.predict([sample1])
            #print('normal cell: and viability', sample1, normal_cell_viability)
            change_cell_into_cancer = sample1
            change_cell_into_cancer[0] = random.choice(List_of_cancer_cell)
            cancer_cell = change_cell_into_cancer
            cancer_cell_viability = trained_model.predict([cancer_cell])
            #print('cancer cell: and viability', cancer_cell, cancer_cell_viability)
            viability = (normal_cell_viability / (normal_cell_viability + cancer_cell_viability))
            compound = [*normal, *sample1, *viability]
            global_list.append(compound)
    return pd.DataFrame(global_list, columns= column )

def sort_compound(df):
    dataframe = []
    for i in range (df.shape[0]):
        dataframe.append(df.sort_values('fitness',ascending=False).iloc[i].values.tolist())
    dfff = pd.DataFrame(dataframe, columns= column)
    #dfff = dfff.reset_index()
    return dfff

#print(Viability_prediction())

#print('output:\n', sort_compound(Viability_prediction()))
# here the printed values are cell line, cancer line, test, time, concentration, Hydrodynamic diameter (nm), Zeta potential and viability
