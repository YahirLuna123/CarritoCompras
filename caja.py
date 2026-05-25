class CajaRegistradora:
    @staticmethod
    def procesar_pago_y_ticket(nombre_cliente, cosas_carrito, total):
        print(f"\nTotal a pagar: ${total:.2f}")
        
        try:
            pago = float(input("Ingrese el monto con el que va a pagar: $"))
            while pago < total:
                print(f"Monto insuficiente. Te faltan ${total - pago:.2f}")
                pago = float(input("Ingrese un nuevo monto: $"))
            
            cambio = pago - total
            print(f"\n¡Pago aceptado! Su cambio es: ${cambio:.2f}")
            
            # Generar Ticket TXT
            nombre_archivo = "ticket_compra.txt"
            with open(nombre_archivo, "w", encoding="utf-8") as f:
                f.write("=== TICKET DE COMPRA MERCADOVENTAS ===\n")
                f.write(f"Cliente: {nombre_cliente}\n")
                f.write("-" * 40 + "\n")
                for c in cosas_carrito:
                    # c[3] es cantidad, c[1] es nombre, c[2] es precio
                    f.write(f"{c[3]}x {c[1]} - ${c[2]*c[3]:.2f}\n")
                f.write("-" * 40 + "\n")
                f.write(f"Total a pagar: ${total:.2f}\n")
                f.write(f"Efectivo recibido: ${pago:.2f}\n")
                f.write(f"Cambio devuelto: ${cambio:.2f}\n")
                f.write("¡Gracias por su compra!\n")
            
            print(f"\nSe generó su recibo en el archivo '{nombre_archivo}'.")
            return True # Retorna True si todo salió bien
            
        except ValueError:
            print("Error: Por favor ingresa una cantidad numérica válida.")
            return False