import pandas as pd
import prediction
import crossing_and_mutation
import generations
generation_number = 50


#input
population_size = 50
#cross_over = 0.4

import warnings
warnings.filterwarnings("ignore")


def Genetic_Algorithm():
    Generation1 = prediction.Viability_prediction()
    Generation2 = crossing_and_mutation.evolution(Generation1)
    Generation_next = generations.new_generations(Generation2)
    a = 3
    i = 0
    while i < 0.8 and a < generation_number:
        print('generation_number:', a, 'fitness', i, '\n')
        print(Generation_next)
        i = Generation_next.iloc[0][7]
        Generation_next = generations.new_generations(Generation_next)
        a += 1
    return Generation_next

print("Final result:", Genetic_Algorithm())
data_output = Genetic_Algorithm()
data_output.to_csv('data_out.csv')