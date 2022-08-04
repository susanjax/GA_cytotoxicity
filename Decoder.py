import pickle

scaler_location = 'ML_models/scaler.pkl'
encoder_location = 'ML_models/encoder.pkl'

def Scaler():
    with open(scaler_location, 'rb') as f:
        scaler_function = pickle.load(f)
        return scaler_function

def Decoder():
    with open(encoder_location, 'rb') as file:
        encoder_function = pickle.load(file)
    return encoder_function

#print(Scaler())
print(Decoder())

#def reverse_scaler():

