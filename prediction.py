import random
import pandas as pd
import compound
import joblib

column = ['normal_cell', 'cancer_cell', 'test', 'time (hr)', 'concentration (ug/ml)', 'Hydrodynamic diameter (nm)', 'Zeta potential (mV)', 'fitness']
List_of_normal_cell = [1, 2, 3, 4, 6, 7, 8, 9, 11, 12, 13, 14,16,17,18,19,21,22,23,24,26,27,28,29,31,32,33,34]
List_of_cancer_cell = [5, 10, 15, 20, 25, 30]

population_size = 100
trained_model = joblib.load('ML_models/Trained_model.joblib')
sample = compound.transformed_input()


def Viability_prediction():
    global_list = []
    compound_list = []
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
    for i in range (population_size):
        dataframe.append(df.sort_values('fitness',ascending=False).iloc[i].values.tolist())
    return pd.DataFrame(dataframe, columns=column)

#print(Viability_prediction())
#print('output:\n', sort_compound(Viability_prediction()))
# here the printed values are cell line, cancer line, test, time, concentration, Hydrodynamic diameter (nm), Zeta potential and viability
