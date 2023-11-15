# Este tercer ejercicio reune y muestra como usar el metodo append() para lograr
# el mismo resultado que los anteriores, pero con un agregado en su estructura y 
# lectura del codigo.
print('\n     - MY DATABASE - ')
users = {}
id_num = 1

while True:
    # En este punto creamos un nuevo diccionario, pero en vez de dejarlo vacio, 
    # le asignaremos sus claves cuyos valores estaran vacios:
    for i in range(id_num):
        user = {
            'id': [],
            'age': [],
            'city': []
        }

        while True:
            print("   Generating new user:")
            user_name = input("name: ")
            user_age = input("age: ")
            user_city = input("city: ")

            if user_name in users:
                print("Repeat users are not allowed")
            else:
                break
            
            # Aqui es donde se introduce la funcion append() para generar los 
            # valores de nuestros datos de forma que se puedan iterar sin 
            # problema:
            user['age'].append(user_age)
            user['city'].append(user_city)
            
        print('\n  -- REGISTRED USERS --')

        if id_num > 0:
            id_num += 1

            for i in range(id_num):
                id_user = i
                users[user_name] = user
                name = user_name

                user['id'] = id_user
                user['age'] = user_age
                user['city'] = user_city

            for name, user_name in users.items():
                identy = user_name['id']
                age = user_name['age']
                city = user_name['city']
                
                print("**********")
                print("- USER ", identy)
                print("  name: ", name)
                print("  age: ", age)
                print("  city: ", city)
                print("-----------")

        opciones = input("¿Do you want to keep inputting users?: ")
        match opciones:
            case "si":
                continue

            case "yes":
                continue

            case default:

                print(input("press ENTER to exit: "))

                exit()