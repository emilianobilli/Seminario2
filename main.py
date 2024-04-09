from api import AdoptAPetAPI
from key import APIKEY

def print_pet_info(pet_data):
    # Esto es otro comentario
    """
    Imprime la información de cada mascota de forma amigable para el humano.
    """
    if "pets" in pet_data:
        print("Información de las mascotas:")
        print("----------------------------")
        for pet in pet_data["pets"]:
            print(f"Nombre: {pet['pet_name']}")
            print(f"Sexo: {'Macho' if pet['sex'] == 'm' else 'Hembra'}")
            print(f"Edad: {pet['age']}")
            print(f"Tamaño: {pet['size']}")
            print(f"Raza Primaria: {pet['primary_breed']}")
            # Usando get para manejar None en 'secondary_breed'
            print(f"Raza Secundaria: {pet.get('secondary_breed', 'N/A')}")
            print(f"Ciudad: {pet['addr_city']}, Estado: {pet['addr_state_code']}")
            print(f"Detalles: {pet['details_url']}")
            print(f"Foto (pequeña): {pet['results_photo_url']}")
            print(f"Foto (grande): {pet['large_results_photo_url']}\n")
    else:
        print("Fallo tu consulta")
        print(pet_data["error"])

api_client = AdoptAPetAPI(APIKEY)
resultado = api_client.query(10, "Miami", "cat")
print_pet_info(resultado)
