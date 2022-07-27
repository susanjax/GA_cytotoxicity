import pandas as pd
import prediction
import crossing_and_mutation
generation_number = 100

Generation1 = prediction.sort_compound(prediction.Viability_prediction())
Generation2 = crossing_and_mutation.evolution(Generation1)
loop = Generation2

def new_generations(Gen):
    new = [Gen, prediction.Viability_prediction()]
    new_generation_input = pd.concat(new)
    sort_result = prediction.sort_compound(new_generation_input)
    new_gen = crossing_and_mutation.evolution(sort_result)
    return new_gen

#
# def generations(loop_gen):
#     future_generation = new_generations(loop_gen)
#     return future_generation


def final():

    a = 2
    old = new_generations(Generation2)
    i = 0
    while i < 0.9 and a < generation_number:
        old = new_generations(old)
        i = old.iloc[0][7]
        print('generation_number:', a , 'fitness', i)
        print(old)

        a += 1
    return old

print(final())