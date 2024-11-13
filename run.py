import pickle
import numpy as np
import pandas as pd
import random
import json
import time
import matplotlib.pyplot as plt
import seaborn as sns



# Load the attributes
attr_path = 'pickleFiles/trajectory_meta.pkl'
with open(attr_path, 'rb') as f:
    attrs = pickle.load(f)

# Load the trajectories
trajs_path= 'pickleFiles/trajectories.pkl'
with open(trajs_path, 'rb') as f:
    trajs = pickle.load(f)

attrs = np.array(attrs)

print('Number of synthetic trajectories: {:d}'.format(len(attrs)))
print(type(trajs))
print(attrs.shape)
print(len(trajs))



print('attributes of the first trip: [trip distance, trip time, departure time, sample points] \n',attrs[0])

trip_distance, trip_time, depart_time, sample_points = attrs[:,0], attrs[:,1], attrs[:,2], attrs[:,3]