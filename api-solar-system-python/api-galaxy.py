import requests
import os

def get_bodies(body_type):
    os.system("cls" if os.name == "nt" else "clear")  
    print(f"::: {body_type.upper()} INFORMATION :::")
    api_url = f"https://api.le-systeme-solaire.net/rest/bodies/"

    try:
        response = requests.get(api_url, params={"filter[]": f"bodyType,{body_type}"})
        response.raise_for_status()  

        data = response.json()

        if "bodies" in data:
            for body in data["bodies"]:
                if body.get("bodyType") == body_type.capitalize():  
                    print("Nombre en inglés:", body["englishName"])
                    print("Gravedad:", body["gravity"])
                    print("Inclinación:", body["inclination"])
                    print("¿Es un planeta?", body["isPlanet"])
                    print("\n")
        else:
            print(f"Not information {body_type}.")

    except requests.exceptions.RequestException as e:
        print(f"Error al realizar la solicitud a la API: {e}")

def main():
    while True:
        print(" #### MAIN MENU ####")
        print("[1]. Planets information")
        print("[2]. Moons information")
        print("[3]. Stars information")
        print("[4]. Asteroid information")
        print("[5]. Comets iformation")
        print("[6]. Exit")

        opt = input("::: select an option: ")

        if opt == '6':
            print("Exit")
            break
        
        if opt == '1':
            get_bodies("Planet")
        elif opt == '2':
            get_bodies("Moon")
        elif opt == '3':
            get_bodies("Star")
        elif opt == '4':
            get_bodies("Asteroid")    
        elif opt == '5':
            get_bodies("Comet")    
        else:
            print("please choose again")

if __name__== "__main__":
    main()