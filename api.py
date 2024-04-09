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

def CallApi():
    url = "https://api.adoptapet.com/search/pet_search?key=4a1213b4f464aa49cc1308dfaac6c532&v=1&geo_range=10&city_or_zip=90210&species=cat&output=json"
    response = requests.get(url)
    return response.json()

# Uso de la clase
if __name__ == "__main__":
    print(CallApi())
#    api_client = AdoptAPetAPI(APIKEY)
#    resultado = api_client.query(10, "90210", "dog")
#    print(resultado)
