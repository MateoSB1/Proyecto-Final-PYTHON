from users import Users

users: list[Users] = []

def signup() -> Users | None:
    try:
        username: str = input("Ingrese su nombre de usuario: ")
        email: str = input("Ingrese su email: ")
        password: str = input("Ingrese su contraseña: ")
        age_input: str = input("Ingrese su edad: ")
        
        if not username or not email or not password or not age_input:
            print("Error: Todos los campos son obligatorios.")
            return None
        
        try:
            age: int = int(age_input)
        except ValueError:
            print("Error: La edad debe ser un número entero.")
            return None
        
        for user in users:
            if user.username == username:
                print("Error: El nombre de usuario ya está en uso.")
                return None
            if user.email == email:
                print("Error: El email ya está registrado.")
                return None
    except Exception as error:
        print(f"Error inesperado: {error}")
        return None
    else:
        print("Registro exitoso.")
        return Users(username, email, password, age)

def validate_login(username: str, password: str) -> Users | None:
    for user in users:
        if user.username == username and user.password == password:
            return user
    return None

def login() -> Users | None:
    try:
        username: str = input("Ingrese su nombre de usuario: ")
        password: str = input("Ingrese su contraseña: ")
        
        if not username or not password:
            print("Error: El nombre de usuario y la contraseña no pueden estar vacíos.")
            return None
    except Exception as error:
        print(f"Error inesperado: {error}")
        return None
    else:
        user: Users | None = validate_login(username, password)
        if user:
            user.login(password)
            return user
        else:
            print("Nombre de usuario o contraseña incorrectos.")
            return None

def show_users() -> None:
    if not users:
        print("No hay usuarios registrados.")
    else:
        print("\nUsuarios registrados:")
        for user in users:
            print(user)

def main() -> None:
    while True:
        print("\n1. Registrarse")
        print("2. Iniciar Sesión")
        print("3. Mostrar todos los usuarios registrados")
        print("4. Salir")
        opcion: str = input("Seleccione una opción: ")
        if opcion == "1":
            user: Users | None = signup()
            if user:
                users.append(user)
        elif opcion == "2":
            user: Users | None = login()
            if user:
                while user.is_logged_in:
                    print("\n1. Cerrar sesión")
                    print("2. Ver información del usuario")
                    print("3. Volver al menú principal")
                    opcion_usuario: str = input("Seleccione una opción: ")
                    if opcion_usuario == "1":
                        user.logout()
                    elif opcion_usuario == "2":
                        print(user)
                    elif opcion_usuario == "3":
                        break
                    else:
                        print("Error: Opción no válida. Intente de nuevo.")
        elif opcion == "3":
            show_users()
        elif opcion == "4":
            break
        else:
            print("Error: Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    main()