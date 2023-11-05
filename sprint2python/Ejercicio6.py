import random

def adivinanza(pregunta, opciones, respuesta_correcta):
    # Muestra la pregunta al usuario
    print(pregunta)
    
    # Muestra las opciones disponibles
    for opcion, descripcion in opciones.items():
        print(f"({opcion}) {descripcion}")

    # El usuario ingresa su respuesta
    respuesta_usuario = input("Tu respuesta (a, b o c): ")

    # Comprueba si la respuesta del usuario es correcta
    if respuesta_usuario == respuesta_correcta:
        print("¡Respuesta correcta!\n")
        return 10
    else:
        # Muestra la respuesta correcta si el usuario se equivoca
        print(f"Respuesta incorrecta. La respuesta correcta es ({respuesta_correcta}) {opciones[respuesta_correcta]}.\n")
        return -5

def main():
    puntuacion = 0

    # Lista de adivinanzas
    adivinanzas = [
        {
            "pregunta": "¿Qué animal camina en cuatro patas por la mañana, en dos patas por la tarde y en tres patas por la noche?",
            "opciones": {"a": "El perro", "b": "El hombre", "c": "La serpiente"},
            "respuesta_correcta": "b"
        },
        {
            "pregunta": "¿Qué tiene llaves pero no abre puertas?",
            "opciones": {"a": "Un candado", "b": "Un coche", "c": "Un zapato"},
            "respuesta_correcta": "a"
        },
        {
            "pregunta": "Si quieres saber cómo soy, toca un triángulo y escucharás mi voz. ¿Quién soy?",
            "opciones": {"a": "Una flor", "b": "El viento", "c": "El agua"},
            "respuesta_correcta": "b"
        }
    ]

    # Selecciona dos adivinanzas aleatoriamente sin repetición
    adivinanzas_seleccionadas = random.sample(adivinanzas, 2)

    # Itera a través de las adivinanzas seleccionadas
    for adivinanza_data in adivinanzas_seleccionadas:
        pregunta = adivinanza_data["pregunta"]
        opciones = adivinanza_data["opciones"]
        respuesta_correcta = adivinanza_data["respuesta_correcta"]
    
        # Llama a la función de adivinanza y actualiza la puntuación
        puntuacion += adivinanza(pregunta, opciones, respuesta_correcta)

    # Muestra la puntuación final al usuario
    print(f"Tu puntuación final es: {puntuacion} puntos.")

if __name__ == "__main__":
    main()
