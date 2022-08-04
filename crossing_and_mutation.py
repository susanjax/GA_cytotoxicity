import cross
import evolved_fitness
import prediction
import mutation
import random
import pandas as pd

elite_population = 5
population_size = 50
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
        individual2 = sorted_pop.iloc[random.randint(i, 55)].values.tolist()
        cross_individual = cross.crossover_individuals(individual1, individual2)
        fitness_prediction_of_cross_individual = evolved_fitness.evolved_compound(cross_individual)
        #print('this is normal and crossed individual', individual1, cross_individual, fitness_prediction_of_cross_individual)
        cross_ind = []
        if individual1[7] >= fitness_prediction_of_cross_individual[7]:
            cross_ind = individual1
        else:
            cross_ind = fitness_prediction_of_cross_individual
        #print('selective individual', cross_ind)
        mutate_individual = mutation.to_mutation(cross_ind)
        #print('this is mutated individual', mutate_individual)
        fitness_prediction_of_mutated_individual = evolved_fitness.evolved_compound(mutate_individual)
        mutate_ind = []
        if cross_ind[7] >= fitness_prediction_of_mutated_individual[7]:
            mutate_ind = cross_ind
        else:
            mutate_ind = fitness_prediction_of_mutated_individual
        #print('evolved mutated', fitness_prediction_of_mutated_individual, mutate_ind)
        dataframe.append(mutate_ind)
        i += 1
        #print('cross;', dataframe)
    compound_List = pd.DataFrame(dataframe, columns=column)
    sorted = compound_List.sort_values('fitness', ascending=False)
    return sorted
print('out', evolution(df))
