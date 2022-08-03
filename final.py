import pandas as pd
import prediction
import crossing_and_mutation
generation_number = 50

#input
population_size = 200
cross_over = 0.6


Generation1 = prediction.Viability_prediction()
#print('Generation1', prediction.sort_compound(Generation1))
Generation2 = crossing_and_mutation.evolution(Generation1)
#print(Generation2)



def new_generations(Gen):
    new = [Gen, prediction.Viability_prediction()]
    new_generation_input = pd.concat(new)
    sort_result = prediction.sort_compound(new_generation_input)
    sort_result.reset_index()
    new_gen = crossing_and_mutation.evolution(sort_result)
    return new_gen


print('Generation1\n', prediction.sort_compound(Generation1), '\n Generation2 \n',Generation2, '\n New \n',new_generations(Generation2), )


def final():
    #Generation1 = prediction.Viability_prediction()
    #Generation2 = crossing_and_mutation.evolution(Generation1)
    Generation_next = Generation2
    a = 3
    i = 0
    while i < 0.8 and a < generation_number:
        Generation_next = new_generations(Generation_next)
        i = Generation_next.iloc[0][7]
        print('generation_number:', a , 'fitness', i, '\n' )
        print(Generation_next)
        a += 1
    return Generation_next

print("Final result:", final())