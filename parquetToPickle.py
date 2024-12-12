import pandas as pd
import numpy as np
from datetime import datetime, timedelta

def timestamp_to_interval(timestamp):
    # Convert Unix timestamp to datetime
    dt = datetime.utcfromtimestamp(timestamp)
    
    # Calculate the 5-minute interval of the day
    minutes_since_midnight = dt.hour * 60 + dt.minute
    interval = minutes_since_midnight // 5
    
    return interval

def convert_parquet_to_pkl(input_path, output_path):
    # Load the data from a Parquet file
    df = pd.read_parquet(input_path)
    
    # Convert 'departure_time' from Unix timestamp to 5-minute interval
    df['departure_time'] = df['departure_time'].apply(timestamp_to_interval)
    
    # Subtract 1 from 'count'
    df['count'] = df['count'] + 1
    
    # Selecting the required columns
    df_processed = df[['travel_distance', 'travel_time', 'departure_time', 'count']]
    
    # Convert the DataFrame to a NumPy array
    np_array = df_processed.to_numpy().tolist()
    
    # Save the numpy array to a pickle file
    pd.to_pickle(np_array, output_path)
    
    print(f"File has been converted and saved to {output_path}")


input_parquet_path = 'trajectory_meta.parquet'  # Specify your input file path
output_pickle_path = 'pickleFiles/trajectory_meta.pkl'    # Specify your output file path

convert_parquet_to_pkl(input_parquet_path, output_pickle_path)
