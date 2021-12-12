import numpy as np
import pickle

model = pickle.load(open('model.pkl', 'rb'))
# lat, lon, barea, larea, nbed, nbath, gar
num = model.predict([[500, 500, 3, 3]])
print(num[0]*10000000)