# Este primer ejercicio sirve para entender como generar datos con un numero 
# sin que se repitan sus valores.

# Primero creamos un diccionario vacio que contendra todos los datos y un 
# valor iterable en una variable, que nos servira para simular un id:
dataBase = {}
gen_id = 1

while True:
    try:
        
        # Aqui creamos un nuevo diccionario que contendra cada dato ingresado, 
        # y usaremos nuestra variable como iterable para nuestro id:
        for _ in range(gen_id):
            data = {}

            while True:
                username = input("write a name: ")

                if username in dataBase:
                    print("Repeat users are not allowed")
                else:
                    break

            print("**********\n REGISTRED USERS: \n")

            if gen_id > 0:
                gen_id += 1

                for u in range(gen_id):
                    id_user = 'id'
                    data[id_user] = u
                    dataBase[username] = data

                for name, id_user in dataBase.items():
                    print(f"user {name}: ")
                    print(id_user)
                    print("\n---------")

        opciones = input("¿Do you want to keep inputting users?: ")
        if opciones == 'si':
                continue
        elif opciones == 'yes':
                continue
        elif opciones == 'no':
                print(input("Press ENTER to Exit: "))
                exit()
        else:
            print("Invalid, Try again")

    except ValueError:
        print("incorrect, please tray again")