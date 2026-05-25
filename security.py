import msvcrt
import sys

class Seguridad:
    @staticmethod
    def ingresar_contrasena(mensaje="Ingrese su contraseña: "):
        print(mensaje, end='', flush=True)
        contrasena = ""
        while True:
            char = msvcrt.getch()
            if char in {b'\r', b'\n'}: # Detecta la tecla Enter
                print('')
                break
            elif char == b'\x08': # Detecta la tecla Borrar (Backspace)
                if len(contrasena) > 0:
                    contrasena = contrasena[:-1]
                    sys.stdout.write('\b \b')
                    sys.stdout.flush()
            else:
                try:
                    contrasena += char.decode('utf-8')
                    sys.stdout.write('*') # Aquí imprime el asterisco
                    sys.stdout.flush()
                except UnicodeDecodeError:
                    pass
        return contrasena