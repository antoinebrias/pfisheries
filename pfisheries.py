import requests
import pandas as pd

def of_country_codes(foptions=None):
    if foptions is None:
        foptions = {}
        
    url = "http://openfisheries.org/api/landings/countries.json"
    response = requests.get(url, **foptions)
    response.raise_for_status()
    
    countries = response.json()
    countries_df = pd.DataFrame(countries)
    
    return countries_df

def of_landings(country=None, species=None, foptions=None):

    if foptions is None:
        foptions = {}

    if country is None and species is None:
        url = "http://openfisheries.org/api/landings"
    elif country is not None and species is None:
        url = f"http://openfisheries.org/api/landings/countries/{country}.json"
    elif country is None and species is not None:
        url = f"http://openfisheries.org/api/landings/species/{species}.json"
    else:
        url = f"http://openfisheries.org/api/landings/countries/{country}/species/{species}.json"
        
    
    try:
        response = requests.get(url, **foptions)
        response.raise_for_status()  # Raise HTTPError for non-2xx status codes

        landings_data_JSON = response.json()

        if not landings_data_JSON:
            return pd.DataFrame()

        landings_data = pd.DataFrame(landings_data_JSON)

        if species is not None:
            landings_data['species'] = species
        if country is not None:
            landings_data['country'] = country

        return landings_data if not landings_data.empty else None

    except requests.exceptions.HTTPError as http_err:
        if response.status_code == 404:
            print(f"Data not found for {species} in country {country}")
            return None  # or return pd.DataFrame() if you prefer
        else:
            raise  # Re-raise the exception for other HTTP errors

    except requests.exceptions.RequestException as req_err:
        print(f"Request error: {req_err}")
        return None  # Handle other request errors gracefully

def spfillnull(x):
    if x.get("isscaap") is None:
        x["isscaap"] = None
    return x

def of_species_codes(foptions=None):
    if foptions is None:
        foptions = {}
        
    url = "http://openfisheries.org/api/landings/species.json"
    response = requests.get(url, **foptions)
    response.raise_for_status()
    
    species_data = response.json()
    species_data = [spfillnull(item) for item in species_data]
    
    species_data_frame = pd.DataFrame(species_data)
    
    return species_data_frame

# not working
def of_country_landings_for_species(species, foptions=None):
    if foptions is None:
        foptions = {}
    countries_df = of_country_codes(foptions=foptions)
 
    all_country_landings = pd.DataFrame()

    for index, row in countries_df.iterrows():
        country_code = row['iso3c']
        url = f"http://openfisheries.org/api/landings/countries/{country_code}/species/{species}.json"

        try:
            response = requests.get(url, **foptions)
            response.raise_for_status()  # Raise HTTPError for non-2xx status codes

            landings_data_JSON = response.json()

            if not landings_data_JSON:
                continue  # Skip if no data for this country and species

            landings_data = pd.DataFrame(landings_data_JSON)
            landings_data['country'] = row['country']  # Add country name

            all_country_landings = pd.concat([all_country_landings, landings_data], ignore_index=True)

        except requests.exceptions.HTTPError as http_err:
            if response.status_code == 404:
                print(f"Data not found for species {species} in country {row['country']}")
                continue  # Skip to the next country
            else:
                raise  # Re-raise the exception for other HTTP errors

        except requests.exceptions.RequestException as req_err:
            print(f"Request error: {req_err}")
            continue  # Skip to the next country on error

    return all_country_landings if not all_country_landings.empty else None


# not working
def of_species_landings_for_country(country, foptions=None):
    if foptions is None:
        foptions = {}

    species_df = of_species_codes(foptions=foptions)
    print(species_df.head())
    all_species_landings = pd.DataFrame()

    for index, row in species_df.iterrows():
        species_code = row['a3_code']
        url = f"http://openfisheries.org/api/landings/countries/{country}/species/{species_code}.json"

        try:
            response = requests.get(url, **foptions)
            response.raise_for_status()  # Raise HTTPError for non-2xx status codes
            print(species_code)
            landings_data_JSON = response.json()

            if not landings_data_JSON:
                continue  # Skip if no data for this species in the country

            landings_data = pd.DataFrame(landings_data_JSON)
            landings_data['species'] = row['scientific_name']  # Add species name

            all_species_landings = pd.concat([all_species_landings, landings_data], ignore_index=True)
            

        except requests.exceptions.HTTPError as http_err:
            if response.status_code == 404:
                print(f"Data not found for species {row['scientific_name']} in country {country}")
                
                continue  # Skip to the next species
            else:
                raise  # Re-raise the exception for other HTTP errors

        except requests.exceptions.RequestException as req_err:
            print(f"Request error: {req_err}")
            continue  # Skip to the next species on error

    return all_species_landings if not all_species_landings.empty else None

