import numpy as np
import pickle

model = pickle.load(open('model.pkl', 'rb'))
# lat, lon, barea, larea, nbed, nbath, gar
print(model.predict([[-6, 108, 300, 300, 3, 3, 0]]))