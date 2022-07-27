import joblib
trained_model = joblib.load('ML_models/Trained_model.joblib')

#one = [27.0, 15.0, 1.0, 0.48936170212765956, 0.024990249902499023, 0.04738641914997557, 0.4744922059518186, 0.5390397260038178]

def evolved_cross(cross_individual):
    normal_cell = [cross_individual[index] for index in [0, 2, 3, 4, 5, 6 ]]
    cancer_cell = [cross_individual[index] for index in [1, 2, 3, 4, 5, 6]]
    normal_viability = trained_model.predict([normal_cell])
    cancer_viability = trained_model.predict([cancer_cell])
    fitness = (normal_viability / (normal_viability + cancer_viability))
    del cross_individual[-1]
    compound = [*cross_individual, *fitness]
    return compound
#print(evolved_cross(one))