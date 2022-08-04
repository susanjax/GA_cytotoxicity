import joblib
trained_model = joblib.load('ML_models/Trained_model.joblib')

#one = [68.0, 35.0, 12.0, 0.0, 0.0008733333333333333, 0.18701505094886414, 0.49173358526216343, 0.307869979038986]

def evolved_compound(cross_individual):
    normal_cell = [cross_individual[index] for index in [0, 2, 3, 4, 5, 6 ]]
    cancer_cell = [cross_individual[index] for index in [1, 2, 3, 4, 5, 6]]
    normal_viability = trained_model.predict([normal_cell])
    cancer_viability = trained_model.predict([cancer_cell])
    fitness = (normal_viability / (normal_viability + cancer_viability))
    del cross_individual[-1]
    compound = [*cross_individual, *fitness]
    return compound
#print(evolved_compound(one))