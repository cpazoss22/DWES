# Definición de la función 'adivinanza' que recibe una pregunta, opciones y respuesta correcta
def adivinanza(pregunta, opciones, respuesta_correcta):
    # Imprime la pregunta
    print(pregunta)

    # Recorre las opciones y sus descripciones
    for opcion, descripcion in opciones.items():
        print(f"({opcion}) {descripcion}")
    
    # Solicita la respuesta del usuario
    respuesta_usuario = input("Tu respuesta (a, b o c): ")
    
    # Compara la respuesta del usuario con la respuesta correcta
    if respuesta_usuario == respuesta_correcta:
        print("¡Respuesta correcta!\n")
        return 10
    else:
        # Muestra la respuesta correcta si es incorrecta y restar puntos
        print(f"Respuesta incorrecta. La respuesta correcta es ({respuesta_correcta}) {opciones[respuesta_correcta]}.\n")
        return -5

# Función principal que inicia el juego
def main():
    puntuacion = 0  # Inicializar la puntuación del jugador

    # Primera adivinanza
    pregunta1 = "¿Qué animal camina en cuatro patas por la mañana, en dos patas por la tarde y en tres patas por la noche?"
    opciones1 = {"a": "El perro", "b": "El hombre", "c": "La serpiente"}
    respuesta_correcta1 = "b"
    
    # Llama a la función 'adivinanza' para la primera pregunta y actualizar la puntuación
    puntuacion += adivinanza(pregunta1, opciones1, respuesta_correcta1)

     # Segunda adivinanza
    pregunta2 = "¿Qué tiene llaves pero no abre puertas?"
    opciones2 = {"a": "Un candado", "b": "Un coche", "c": "Un zapato"}
    respuesta_correcta2 = "a"
    
    puntuacion += adivinanza(pregunta2, opciones2, respuesta_correcta2)

    # Tercera adivinanza
    pregunta3 = "Si quieres saber cómo soy, toca un triángulo y escucharás mi voz. ¿Quién soy?"
    opciones3 = {"a": "Una flor", "b": "El viento", "c": "El agua"}
    respuesta_correcta3 = "b"
    
    puntuacion += adivinanza(pregunta3, opciones3, respuesta_correcta3)

    # Imprime la puntuación final del jugador
    print(f"Tu puntuación final es: {puntuacion} puntos.")

# Comprueba si este script es el punto de entrada principal
if __name__ == "__main__":
    main()  # Llama a la función principal 'main' para iniciar el juego
