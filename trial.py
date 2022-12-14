import pandas as pd
import random
import matplotlib.pyplot as plt
import joblib
import sklearn
import pickle
import numpy as np
from sklearn.preprocessing import  MinMaxScaler
from category_encoders import OrdinalEncoder
import sklearn

individual_char = ['rand_cell_type', 'rand_test', 'rand_time', 'rand_conc', 'rand_hd', 'rand_zeta'] #for crossover
population_size = 50    # number of individuals in generation
max_generations = 50    # maximal number of generations
elite_group = 5 # top 5 compounds which have highest fitness score after random feature (they are not exposed to mutation and crossover)
desired_fitness = 0.9
prob_crossover = 0.8    # probability of each gene exchange
prob_mutation = 0.1
Tournament_selection = 4

db = pd.read_csv('Database/Cytotoxicity.csv')   # here the toxicity database is loaded
with open('ML_models/scaler.pkl', 'rb') as f:
    scaler = pickle.load(f)
#scaled_values = scaler.fit_transform(values)
with open('ML_models/encoder.pkl', 'rb') as file:
    encoder = pickle.load(file)
trained_model = joblib.load('ML_models/Trained_model.joblib')

cell_type = db['Cell type']
test = db['test']
material = db['material']
time = db['time (hr)']
concentration = db['concentration (ug/ml)']
viability = 0  # to be determined by the trained model
hd = db['Hydrodynamic diameter (nm)']
zeta = db['Zeta potential (mV)']

class Individual:
    def __init__(self):
        inlist = []
        cols = ['unnamed', 'Cell type', 'material', 'test']
        for a in range(100):
            inlist.append([0, random.choice(cell_type), random.choice(material), random.choice(test)])
        df = pd.DataFrame(inlist, columns=cols)
        #with open('ML_models/encoder.pkl', 'rb') as file:
        #    encoder = pickle.load(file)
        out1 = encoder.transform(df)  # randomized sample with 3 features (one unnecessary)
        mod_out1 = out1.iloc[:, [1, 3]]  # choose only cell type and test
        # print(type(mod_out1))
        # print('part_1:', df.values.tolist()[0][1:], mod_out1)

        scaler_input = []
        cols = ['del', 'time (hr)', 'concentration (ug/ml)', 'Hydrodynamic diameter (nm)', 'Zeta potential (mV)']
        for a in range(100):
            scaler_input.append(
                [0, random.choice(time), random.choice(concentration), random.choice(hd), random.choice(zeta)])
        df2 = pd.DataFrame(scaler_input, columns=cols)
        #with open('ML_models/scaler.pkl', 'rb') as f:
        #    sp = pickle.load(f)
        out2 = scaler.fit_transform(df2)
        # print(type(out2))
        mod_out2 = np.delete(out2, 0, axis=1)
        mod_out2 = pd.DataFrame(mod_out2, columns=['a', 'b', 'c', 'd'])
        # print(mod_out2)
        # print('part_2:', df2.values.tolist()[0][1:], mod_out2 )

        sample = pd.concat([mod_out1, mod_out2], axis=1, join="inner")
        normal_cell = [1, 2, 3, 4, 6, 7, 8, 9, 10]
        fitness_final = []
        fit = 0
        for a in range(10):
            sample1 = sample.iloc[a].values.tolist()
            normal = sample1
            if normal_cell.count(sample1[0]) == True:
                #print('sample',sample1)
                cell_viability = trained_model.predict([sample1])
                cancer_cell = sample1
                cancer_cell[0] = 5  # here put a number which is cancer cell
                #print('cancer', cancer_cell)
                cancer_viability = trained_model.predict([cancer_cell])
                fitness_final = (cell_viability / (cell_viability + cancer_viability))
                fit = round(float(fitness_final), 3)
                break
            else:
                a += 1
                continue
            break

        #print(fit)
        #print('fitness:', type(fitness_final), fitness_final)
        self.character = normal
        self.fitness = fit


    def get_character(self): # return the individual feature for further processing
        return self.character

    def get_fitness(self):  # return the fitness for further processing
        return self.fitness

    def __str__(self):  # to print the individual feature and fitness
        return self.character.__str__()
        #return 'Individual:' + str(self.individual) + 'Fitness:' + str(self.fitness)


class compounds:
    def __init__(self, size):
        self._populations = []
        i = 0
        while i < size:
            self._populations.append(Individual()) #it will join all generated nanomaterial into one single array with all its feature
        i += 1

    def get_individual(self):
        return self._populations


class GeneticAlgorithm:
    @staticmethod
    def evolve(feature):
        return GeneticAlgorithm.mutate_features(GeneticAlgorithm.crossover_features(feature))

    @staticmethod
    def crossover_features(feature):
        crossover_char = compounds(0) #
        for i in range(elite_group):
            crossover_char.get_individual().append(feature.get_individual()[i])
        i = elite_group
        while i < population_size:
            individual1 = GeneticAlgorithm.select_tournament_individuals(feature).get_individual()[0]
            individual2 = GeneticAlgorithm.select_tournament_individuals(feature).get_individual()[0]
            crossover_char.get_individual().append(GeneticAlgorithm.crossover_individuals(individual1, individual2))
            i += 1
        return crossover_char

    @staticmethod
    def mutate_features(feature):
        for i in range(elite_group, population_size):
            GeneticAlgorithm.mutate_individual(feature.get_individual()[i])
            return feature

    @staticmethod
    def crossover_individuals(individual1, individual2):
        cross_individual = Individual()
        for i in range(individual_char.__len__()):
            if random.random() <= prob_crossover:
                if random.random() >= 0.5:
                    cross_individual.get_character()[i] = individual1.get_character()[i]
                else:
                    cross_individual.get_character()[i] = individual2.get_character()[i]
                return cross_individual

    @staticmethod
    def mutate_individual(char):
        for i in range (individual_char.__len__()):
            if random.random() <= prob_mutation:
                if random.random() < 0.5: #code might not work- here change the feature based on the list and position
                    char.get_character()[i] = random.choice()[i]
                else:
                    char.get_character()[i] = random.choice()[i]

    @staticmethod
    def select_tournament_individuals(feature):
        tournament_individual = compounds(0)
        i = 0
        while i < Tournament_selection:
            tournament_individual.get_individual().append(feature.get_individual()[random.randrange(0, population_size)])
            i += 1
        tournament_individual.get_individual().sort(key=lambda x: x.get_fitness(), reverse=True)
        return tournament_individual

def print_all_feature(feature, generation):
    print("\n ........")
    print("Generation Number: ", generation, "| Best fitness Features: ", feature.get_individual()[0].get_fitness())
    print(".........")
    i = 0
    for x in feature.get_individual():
        print("Individual#", i, " :", x, "| Fitness: ", x.get_fitness())
        i += 1

population = compounds(population_size)
population.get_individual().sort(key=lambda x:x.get_fitness(), reverse=True)
print_all_feature(population, 0)
generation_number = 1
while population.get_individual()[0].get_fitness() < individual_char.__len__():
    population = GeneticAlgorithm.evolve(population)
    population.get_individual().sort(key=lambda x: x.get_fitness(), reverse=True)
    print_all_feature(population, generation_number)
    generation_number += 1


