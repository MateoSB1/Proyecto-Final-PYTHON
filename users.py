class Users:
    def __init__(self, username: str, email: str, password: str, age: int) -> None:
        self.username: str = username
        self.email: str = email
        self.password: str = password
        self.age: int = age
        self.is_logged_in: bool = False

    def __str__(self) -> str:
        return f"Usuario: {self.username}, Email: {self.email}, Edad: {self.age}"

    def login(self, password: str) -> None:
        if self.password == password:
            self.is_logged_in = True
            print(f"Bienvenido, {self.username}! Has iniciado sesión correctamente.")
        else:
            print("Contraseña incorrecta. Inténtalo de nuevo.")

    def logout(self) -> None:
        self.is_logged_in = False
        print(f"{self.username} ha cerrado sesión.")