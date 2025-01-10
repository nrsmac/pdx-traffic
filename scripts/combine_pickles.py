import os
import glob
import pickle
import pandas as pd

def combine_pickle_files(prefix, output_filename):
    # Get all pickle files starting with the given prefix
    pickle_files = glob.glob(f"{prefix}*.pkl")
    
    
    # Combine all the lists into a single dataframe
    combined_df = pd.concat(data_lists, ignore_index=True)
    
    # Save the combined dataframe as a CSV file
    output_file = f"{output_filename}.csv"
    combined_df.to_csv(output_file, index=False)
    
    print(f"Combined dataframe saved as {output_file}")

combine_pickle_files("data/cls_inventory", "cls_inventory")
    # List to store the contents of each pickle file
    data_lists = []
    
    # Iterate through each pickle file
    for file in pickle_files:
        with open(file, 'rb') as f:
            # Deserialize the pickled data
            data = pickle.loads(f.read())
            # Add the deserialized data to the list
            data_lists.append(data)
# combine_pickle_files("data/rwis_inventory", "rwis_inventory")
# combine_pickle_files("data/rwis_status", "rwis_status")
# combine_pickle_files("data/traffic_detector_inventory", "traffic_detector_inventory")
# combine_pickle_files("data/traffic_detector_road_status", "traffic_detector_road_status")
