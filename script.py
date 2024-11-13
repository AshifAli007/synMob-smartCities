# import pandas as pd

# def convert_parquet_to_csv(parquet_path, csv_path):
#     # Load the Parquet file into a DataFrame
#     df = pd.read_parquet(parquet_path)

#     # Save the DataFrame to a CSV file
#     df.to_csv(csv_path, index=False)  # Set index=False to avoid writing row indices to the CSV file

# # Example usage:
# parquet_file_path = 'trajectory_meta.parquet'
# csv_file_path = 'csv/trajectory_meta.csv'
# convert_parquet_to_csv(parquet_file_path, csv_file_path)

import pickle

# Load the attributes
attr_path = 'pickleFiles/trajectory_meta.pkl'
with open(attr_path, 'rb') as f:
    attrs = pickle.load(f)

attrs_reduced = attrs[:7]
print(attrs_reduced)

import numpy as np
print(np.__version__)



# import pandas as pd

# # Load the .parquet file
# df = pd.read_parquet('./trajectories.parquet')

# # Group by 'uuid' and convert each group into a numpy array of [longitude, latitude]
# trajectory_list = df.groupby('uuid').apply(lambda x: x[['longitude', 'latitude']].to_numpy()).tolist()

# # Save the list of trajectories to a .pkl file
# pd.to_pickle(trajectory_list, 'pickleFiles/trajectories.pkl')

# print("Trajectories have been saved to 'trajectories.pkl'")



