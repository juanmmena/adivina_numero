# Adivida el número
import random


def jugar(rango_max):
    vidas= 7
    numero_random = random.randint(1, rango_max)
    intentos_realizados = []

    print(f"Adivine el número del 1 al {rango_max}: \n")

    while vidas > 0:

        try:
            num = int(input("Por favor, ingresa tu número\n"))
        except ValueError:
            print("Ingrese un número válido")
            continue
            

        if num in intentos_realizados:
            print("Ya intentaste con este número, prueba con otro")
            continue

        intentos_realizados.append(num)

        if num == numero_random:
            print("Felicidades adivinaste el número!")
            break
        elif num > numero_random:
            if abs(num - numero_random) <= 2:
                print("alto, pero estás cerca")
            else:
                print("muy alto")
        else:
            if abs(num - numero_random) <=2:
                print("bajo, pero estás cerca")
            else:
                print("muy bajo")
        
        vidas = vidas - 1
        print(f"te quedan {vidas} vidas!")
        print(f"intentos anteriores: {intentos_realizados}")

    if vidas == 0:
        print(f"Te quedaste sin vidas, el número era: {numero_random}")

print("Bienvenido al juego, adivina el número")
dificultad = int(input("Elija la dificultad\n1. Nivel fácil\n2. Nivel intermedio\n3. Nivel difícil\n"))

if dificultad == 1:
    jugar(10)
elif dificultad == 2:
    jugar(50)
elif dificultad == 3:
    jugar(100)
else:
    print("Opción no válida")


