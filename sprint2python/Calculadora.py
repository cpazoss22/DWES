from EJERCICIO3 import suma, resta, multiplicacion, division

def main():
    while True:
        try:
            # Solicita al usuario dos números
            num1 = float(input("Ingresa el primer número: "))
            num2 = float(input("Ingresa el segundo número: "))
            
            # Solicita al usuario qué tipo de operación desea realizar
            print("Operaciones disponibles: ")
            print("1. Suma")
            print("2. Resta")
            print("3. Multiplicación")
            print("4. División")
            operacion = input("Elija la operación (1/2/3/4): ")
            
            if operacion not in ['1', '2', '3', '4']:
                print("Operación no válida")
                continue

            if operacion == '1':
                resultado = suma(num1, num2)
                print(f"Resultado: {num1} + {num2} = {resultado}")
            elif operacion == '2':
                resultado = resta(num1, num2)
                print(f"Resultado: {num1} - {num2} = {resultado}")
            elif operacion == '3':
                resultado = multiplicacion(num1, num2)
                print(f"Resultado: {num1} * {num2} = {resultado}")
            elif operacion == '4':
                resultado = division(num1, num2)
                print(f"Resultado: {num1} / {num2} = {resultado}")
        
            # Pregunta al usuario si desea hacer más operaciones
            continuar = input("¿Desea realizar más operaciones? (s/n): ")
            if continuar.lower() != 's':
                break
        except ValueError:
            print("Entrada no válida. Asegúrate de ingresar números válidos.")

if __name__ == "__main":
    main()
