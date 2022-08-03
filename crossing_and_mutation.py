import cross
import evolved_fitness
import prediction
import mutation
import random
import pandas as pd

elite_population = 5
population_size = 100
#cross_over_frequency = 0.6
df = prediction.Viability_prediction()
column = ['normal_cell', 'cancer_cell', 'test', 'time (hr)', 'concentration (ug/ml)', 'Hydrodynamic diameter (nm)', 'Zeta potential (mV)', 'fitness']



def evolution(df_compound_list):
    dataframe = []
    sorted_pop = df_compound_list.sort_values('fitness', ascending=False)
    length = len(sorted_pop) - 1
    for i in range(elite_population):
        dataframe.append(sorted_pop.iloc[i].values.tolist())
        #print('elite', dataframe)
        i += 1
    while i < population_size:
        individual1 = sorted_pop.iloc[i].values.tolist()
        individual2 = sorted_pop.iloc[random.randint(i, length)].values.tolist()
        cross_individual = cross.crossover_individuals(individual1, individual2)
        #print('this is crossed individual', cross_individual)
        mutate_individual = mutation.to_mutation(cross_individual)
        fitness_prediction_of_cross_individual = evolved_fitness.evolved_compound(mutate_individual)
        dataframe.append(fitness_prediction_of_cross_individual)
        i += 1
        #print('cross;', dataframe)
    compound_List = pd.DataFrame(dataframe, columns=column)
    sorted = compound_List.sort_values('fitness', ascending=False)
    return sorted
#print('out', evolution(df))
