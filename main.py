users = []

def signup():
    try:
        nombre_usuario = input("Ingrese su nombre de usuario: ")
        contraseña = input("Ingrese su contraseña: ")
        
        if not nombre_usuario or not contraseña:
            print("Error: El nombre de usuario y la contraseña no pueden estar vacíos.")
            return None
    except Exception as error:
        print(f"Error inesperado: {error}")
        return None
    else:
        print("Registro exitoso.")
        return {"username": nombre_usuario, "password": contraseña}

def validate_login(nombre_usuario, contraseña):
    for usuario in users:
        if usuario["username"] == nombre_usuario and usuario["password"] == contraseña:
            return True
    return False

def login():
    try:
        nombre_usuario = input("Ingrese su nombre de usuario: ")
        contraseña = input("Ingrese su contraseña: ")
        
        if not nombre_usuario or not contraseña:
            print("Error: El nombre de usuario y la contraseña no pueden estar vacíos.")
            return False
    except Exception as error:
        print(f"Error inesperado: {error}")
        return False
    else:
        if validate_login(nombre_usuario, contraseña):
            return True
        return False

def main():
    while True:
        print("\n1. Registrarse")
        print("2. Iniciar Sesión")
        print("3. Salir")
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            user = signup()
            if user:
                users.append(user)
        elif opcion == "2":
            if login():
                print("Inicio de sesión exitoso.")
            else:
                print("Nombre de usuario o contraseña incorrectos.")
        elif opcion == "3":
            break
        else:
            print("Error: Opción no válida. Intente de nuevo.")

main()