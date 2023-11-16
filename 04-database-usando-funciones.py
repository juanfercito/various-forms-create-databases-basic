# Este ejercicio usa todo lo anterior, pero vamos a encapsular algunos procesos en funciones 
# que nos permitan gestionar el codigo de forma mas eficiente y escalable:
users = {}
id_num = 1

while True:
    # Las funciones que necesitamos deben incluirse en este punto para poder invocarlas mas 
    # adelante en el codigo y se ejecuten sin mayor problemas, teniendo en cuenta que estamos 
    # trabajando con bucles:
    def key_val(user_data):    
        for i in range(id_num):
            id_user = i
            users[username] = user

            user['id'] = id_user
            user['age'] = user_age
            user['city'] = user_city              
        return user_data
    
    def show_user(data):
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
        return data
    
    for i in range(id_num):
        user = {}
        while True:
            print("   Generating new user:")
            username = input("name: ")
            user_age = input("age: ")
            user_city = input("city: ")
                
            if username in users:
                print("Repeat users are not allowed\n")
            else:
                break 
    
        print('\n  -- REGISTRED USERS --')
        
        if id_num > 0:
            id_num += 1   
            key_val(users)
            show_user(users)
        
        # Aqui simplificamos el uso de opciones usando sentencia if para validar continuidad 
        # en vez de usar un match, dando el mismo resultado:
        opciones = input("¿Do you want to keep inputting users?: ")
        if opciones == "si":
            continue
        elif opciones == "yes":
            continue
        else:
            print(input("press ENTER to exit: "))
            exit()