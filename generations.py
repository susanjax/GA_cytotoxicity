import prediction
import crossing_and_mutation
import pandas as pd


def first_generation():
    Generation1 = prediction.sort_compound(prediction.Viability_prediction())
    return Generation1

def second_generation(first):
    Generation2 = crossing_and_mutation.evolution(first)
    return Generation2

def new_generations(Gen):
    new = [Gen, prediction.Viability_prediction()]
    new_generation_input = pd.concat(new)
    sort_result = prediction.sort_compound(new_generation_input)
    sort_result.reset_index()
    new_gen = crossing_and_mutation.evolution(sort_result)
    return new_gen

#first_gen = first_generation()
#second_gen = second_generation(first_gen)
#next_gen = new_generations(second_gen)
#print(first, second, new_generations(second))
#print(new_generations(Generation2))

#print('Generation1\n', prediction.sort_compound(Generation1), '\n Generation2 \n',Generation2, '\n New \n',new_generations(Generation2), )
