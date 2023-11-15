# Este segundo ejercicio tiene la misma logica del anterior, con la diferencia 
# de que no presentaremos un id, aunque seguiremos usando nuestra variable 
# iteradora para generar otros datos, como edad y ciudad.

# Aqui haremos lo mismo que antes, solo que para nuestro segundo diccionario 
# le crearemos las claves y sus valores a partir de los inputs directos que 
# alojaran nuestras variables:
print('\n     - BASE DE DATOS - ')
users = {}
count = 1

while True:
    for i in range(count):
        user = {}

        while True:
            print("   Generando nuevo usuario:")
            user_name = input("nombre: ")
            user_age = input("edad: ")
            user_city = input("ciudad: ")

            if user_name in users:
                print("Usuario ya existente, Intente de nuevo")
            else:
                break

        print('\n  -- USUARIOS REGISTRADOS --')
        if count > 0:
            count += 1

            for i in range(count):
                users[user_name] = user
                name = user_name
                user['edad'] = user_age
                user['ciudad'] = user_city

            for name, user_name in users.items():
                age = user_name['edad']
                city = user_name['ciudad']
                print("**********")
                print(name)
                print("edad: ", age)
                print("ciudad: ", city)
                print("----------")

        opciones = input("¿desea continuar ingresando usuarios?: ")
        print("---------")
        match opciones:
            case "si":
                continue
            case "yes":
                continue
            case default:
                print(input("presione ENTER para salir: "))
                exit()