from pfisheries import of_country_codes, of_landings, of_species_codes, of_country_landings_for_species, of_species_landings_for_country
from plotting import fish_plot
import pandas as pd
import matplotlib.pyplot as plt

# Load datasets
species_code_data = pd.read_csv('species_code_data.csv')
country_code_data = pd.read_csv('country_code_data.csv')



# Example usage
if __name__ == "__main__":
    # Download country codes
    country_codes = of_country_codes()
    print(country_codes.head())
#
#    # Download landings data for a specific country
#    landings_canada = of_landings(country='CAN')
#    print(landings_canada.head())
#
#    # Download species codes
#    species_codes = of_species_codes()
#    print(species_codes.head())
#
#    # Plotting landings data
#    plot = fish_plot(landings_canada, species_code_data=species_code_data, country_code_data=country_code_data)
#    plt.show()
#

    # Example 1: Fetch total landings for a specific species across all countries
    species = 'FRO'
    total_species_landings = of_landings(species=species)
    if total_species_landings is not None:
        print(f"\nTotal Landings for {species} across all countries:")
        print(total_species_landings.head())
    else:
        print(f"No data found for {species} across all countries.")

    # Example 1.2: Fetch total landings for a specific species across one country
    country = 'FRA'
    country_species_landings = of_landings(species=species,country = country)
    if country_species_landings is not None:
        print(f"\nTotal Landings for {species} across {country}:")
        print(country_species_landings.head())
    else:
        print(f"No data found for {species} across {country}.")





#    # Example 2: Fetch Landings Data For A Specific Species Across All Countries
#    Species = 'Fro'
#    Country_Species_Landings = Of_Country_Landings_For_Species(Species)
#    If Country_Species_Landings Is Not None:
#        Print(F"\Nlandings Data For {Species} Across All Countries:")
#        Print(Country_Species_Landings.Head())
#    Else:
#        Print(F"No Data Found For {Species} Across All Countries.")

    # Example 3: Fetch landings data for a specific country across all species
    country = 'USA'
    species_country_landings = of_species_landings_for_country(country)
    if species_country_landings is not None:
        print(f"\nLandings Data for {country} across all species:")
        print(species_country_landings.head())
    else:
        print(f"No data found for {country} across all species.")    
