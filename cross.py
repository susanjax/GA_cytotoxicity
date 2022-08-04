import random

#individual1 = [6.0, 10.0, 7.0, 0.23404255319148934, 0.2, 0.021006350757205666, 0.5427514148889857, 0.50300869684053]
#individual2 = [1.0, 1.0, 1.0, 0.934, 0.12, 0.1021006350757205666, 0.15427514148889857, 0.150300869684053]

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
