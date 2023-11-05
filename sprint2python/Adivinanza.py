# Define de la función 'adivinanza' que recibe una pregunta, opciones y respuesta correcta
def adivinanza(pregunta, opciones, respuesta_correcta):
    # Imprime la pregunta
    print(pregunta)

    # Imprime las opciones (a, b, c) junto con sus descripciones
    for opcion, descripcion in opciones.items():
        print(f"({opcion}) {descripcion}")

    # Solicita la respuesta del usuario
    respuesta_usuario = input("Tu respuesta (a, b o c): ")

    # Verifica si la respuesta del usuario es correcta o incorrecta
    if respuesta_usuario == respuesta_correcta:
        print("¡Respuesta correcta!\n")  # Mostrar un mensaje de respuesta correcta
    else:
        print(f"Respuesta incorrecta. La respuesta correcta es ({respuesta_correcta}) {opciones[respuesta_correcta]}.\n")
        # Muestra un mensaje de respuesta incorrecta y la respuesta correcta

if __name__ == "__main__":
    # Define la adivinanza: pregunta, opciones y respuesta correcta
    pregunta = "¿Qué animal camina en cuatro patas por la mañana, en dos patas por la tarde y en tres patas por la noche?"
    opciones = {"a": "El perro", "b": "El hombre", "c": "La serpiente"}
    respuesta_correcta = "b"

    # Llama a la función 'adivinanza' con la adivinanza definida
    adivinanza(pregunta, opciones, respuesta_correcta)
