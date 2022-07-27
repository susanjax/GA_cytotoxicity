import cross
import evolved_fitness
import random
import pandas as pd
import prediction
elite_population = 3
population_size = 100
cross_over_frequency = 0.2
Tournament_selection = 4
df = prediction.Viability_prediction()
sorted_pop = df.sort_values('fitness', ascending=False)
column = ['normal_cell', 'cancer_cell', 'test', 'time (hr)', 'concentration (ug/ml)', 'Hydrodynamic diameter (nm)', 'Zeta potential (mV)', 'fitness']



def evolution(sorted_population):
    dataframe = []
    length = len(sorted_population) - 1
    for i in range(elite_population):
        dataframe.append(sorted_population.iloc[i].values.tolist())
        #print('elite', dataframe)
        i += 1
    while i < population_size:
        individual1 = sorted_population.iloc[i].values.tolist()
        individual2 = sorted_population.iloc[random.randint(i, length)].values.tolist()
        cross_individual = cross.crossover_individuals(individual1, individual2)
        fitness_prediction_of_cross_individual = evolved_fitness.evolved_cross(cross_individual)
        dataframe.append(fitness_prediction_of_cross_individual)
        i += 1
        #print('cross;', dataframe)
    compound_List = pd.DataFrame(dataframe, columns=column)
    sorted = compound_List.sort_values('fitness', ascending=False)
    return sorted
#print(evolution(sorted_pop))