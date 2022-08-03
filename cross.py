import random


cross_over_frequency = 0.3

def crossover_individuals(individual1, individual2):
    cross_individual = []
    for i in range( individual1.__len__()):
        if random.random() >= cross_over_frequency:
            cross_individual.append(individual1[i])
        else:
            cross_individual.append(individual2[i])
    return cross_individual

#print(crossover_individuals(individual1, individual2))
