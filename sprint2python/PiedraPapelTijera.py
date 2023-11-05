import random
contadorAliado = 0
contadorEnemigo = 0

i = 0
while i < 5:
    i += 1
    print()
    print("BIENVENIDO AL JUEGO, tu preguntaras: ¿QUE juego?, y yo te respondo, EL JUEGO")
    print()
    print("POSIBLES JUGADAS")
    print("================")
    print("1.- piedra")
    print("2.- papel")
    print("3.- tijeras")
    print("Acuerdate, si pierdes, mueres")
    jugada = input("Seleccione un movimiento entre los siguientes: piedra, papel, tijeras: ")

    jugadas_array = ["piedra", "papel", "tijeras"]

    aleatorio = random.choice(jugadas_array)

    if jugada == aleatorio:
        print()
        print("Has empatado. Esta ronda no se contará")
    elif jugada == 'piedra' and aleatorio == 'papel':
        print()
        print("Has perdido, moriste")
        contadorEnemigo += 1
    elif jugada == 'papel' and aleatorio == 'piedra':
        print()
        print("Has ganado, papel gana a piedra")
        contadorAliado += 1
    elif jugada == 'piedra' and aleatorio == 'tijeras':
        print()
        print("Has ganado, pedra gana a tijeras")
        contadorAliado += 1
    elif jugada == 'tijeras' and aleatorio == 'piedra':
        print()
        print("Has perdido, moriste")
        contadorEnemigo += 1
    elif jugada == 'papel' and aleatorio == 'tijeras':
        print()
        print("Has perdido, moriste")
        contadorEnemigo += 1
    elif jugada == 'tijeras' and aleatorio == 'papel':
        print()
        print("Has ganado, tijeras gana a papel")
        contadorAliado += 1


if contadorAliado > contadorEnemigo:
    print("Has ganado el mejor de cinco. ¡Enhorabuena!")
elif contadorEnemigo > contadorAliado:
    print("Estás malito y moriste")
else :
    print("Habéis empatado el mejor de cinco")
