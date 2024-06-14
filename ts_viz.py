import pandas as pd
from pfisheries import of_landings, of_species_codes, of_country_codes

def build_species_country_landings_dataframe():
    # Get species codes and country codes
    species_codes = of_species_codes()
    country_codes = of_country_codes()
    
    # Initialize an empty list to store individual DataFrames
    all_data_frames = []
    
    # Iterate over each species
    for index, species_row in species_codes.iterrows():
        species_code = species_row['a3_code']
        
        # Fetch landings data for the current species
        landings_data = of_landings(species=species_code)
        
        if landings_data is not None and not landings_data.empty:
            # Add species column
            landings_data['species'] = species_code
            
            # Append to the list
            all_data_frames.append(landings_data)
    
    # Concatenate all individual DataFrames into a single DataFrame
    if all_data_frames:
        all_data = pd.concat(all_data_frames, ignore_index=True)
    else:
        all_data = pd.DataFrame()
    
    # Merge with country codes to get country names
    if not all_data.empty:
        all_data = pd.merge(all_data, country_codes, left_on='country', right_on='iso3c', how='left')
        all_data.drop(columns=['iso3c'], inplace=True)  # Drop iso3c column after merge
    
    return all_data

# Call the function to build the big DataFrame
species_country_landings_data = build_species_country_landings_dataframe()

# Print or inspect the resulting DataFrame
print(species_country_landings_data.head())

# Save the DataFrame to a CSV file
species_country_landings_data.to_csv('species_country_landings_data.csv', index=False)

