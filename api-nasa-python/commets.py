import requests  
import os 

def get_commet_data(api_key):
    print("::: COMET INFORMATION :::")
    api_url = f"https://api.nasa.gov/neo/rest/v1/neo/3726712?api_key={api_key}"

    try: 
        response = requests.get(api_url)
        response.raise_for_status()
        data = response.json()

        os.system('clear') 
        print(f'Comet name: {data["name"]}')
        print(f'Absolute magnitude: {data["absolute_magnitude_h"]}')
        print(f'Diameter max (KM): {data["estimated_diameter"]["kilometers"]["estimated_diameter_max"]}')
        print(f'Diameter min (KM): {data["estimated_diameter"]["kilometers"]["estimated_diameter_min"]}')
        print(f'Diameter max (FT): {data["estimated_diameter"]["feet"]["estimated_diameter_max"]}')
        print(f'Diameter min (FT): {data["estimated_diameter"]["feet"]["estimated_diameter_min"]}')
        print(f'Last observation date: {data["orbital_data"]["last_observation_date"]}')

    except requests.exceptions.RequestException as e:
        print(f"API error: {e}")

api_key_nasa = 'c9hkw2qN7iXHdixPD2OKlTMNTNBe0x1qFGxkABFo'
get_commet_data(api_key_nasa) 