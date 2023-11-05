# Función para suma
def suma(a, b):
    return a + b

# Función para resta
def resta(a, b):
    return a - b

# Función para multiplicación
def multiplicacion(a, b):
    return a * b

# Función para división
def division(a, b):
    if b == 0:
        return "Error, no se puede realizar esta operación (división por cero)"
    else:
        return a / b

# Bloque principal del programa
if __name__ == "__main__":
    print("Operaciones disponibles: ")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    
    # Solicita al usuario que seleccione una operación
    operacion = input("Escoge entre 1, 2, 3, 4: ")
    
    # Verifica si la operación seleccionada es válida
    if operacion not in ['1', '2', '3', '4']:
        print("Operación no válida")
    else:
        num1 = float(input("Ingresa el primer número: "))
        num2 = float(input("Ingresa el segundo número: "))
        
        # Realiza la operación seleccionada y mostrar el resultado
        if operacion == '1':
            resultado = suma(num1, num2)
            print(f"Resultado = {num1} + {num2} = {resultado}")
        elif operacion == '2':
            resultado = resta(num1, num2)
            print(f"Resultado = {num1} - {num2} = {resultado}")
        elif operacion == '3':
            resultado = multiplicacion(num1, num2)
            print(f"Resultado = {num1} * {num2} = {resultado}")
        elif operacion == '4':
            resultado = division(num1, num2)
            print(f"Resultado = {num1} / {num2} = {resultado}")
