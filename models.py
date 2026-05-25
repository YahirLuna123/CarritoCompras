# models.py
class User:
    Incremento = 0
    def __init__(self, nombre, contrasena, correo, numero):
        self.nombre = nombre
        self.contrasena = contrasena
        self.correo = correo
        self.numero = numero
        self.acceso = False

class Admin(User):
    def __init__(self, nombre, contrasena, correo, numero):
        super().__init__(nombre, contrasena, correo, numero)

class Producto:
    def __init__(self, nombre, precio, cantidad):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

class Carrito:
    def __init__(self):
        self.lista_productos = []