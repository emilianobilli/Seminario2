import requests
from key import APIKEY

class AdoptAPetAPI:
    def __init__(self, key):
        self.base_url = "https://api.adoptapet.com/search/pet_search"
        self.key = key
        self.version = 1  # Versión por defecto
        self.output = "json"  # Output por defecto
    
    def query(self, geo_range, city_or_zip, species):
        params = {
            "key": self.key,
            "v": self.version,
            "geo_range": geo_range,
            "city_or_zip": city_or_zip,
            "species": species,
            "output": self.output
        }
        response = requests.get(self.base_url, params=params)
        return response.json()

# Uso de la clase
if __name__ == "__main__":
    api_client = AdoptAPetAPI(APIKEY)
    resultado = api_client.query(10, "90210", "dog")
    print(resultado)
