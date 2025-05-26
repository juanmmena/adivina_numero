# Adivida el número
import random

vidas= 7



print("Bienvenido al juego, adivina el número")
dificultad = int(input("Elija la dificultad\n1. Nivel fácil\n2. Nivel intermedio\n3. Nivel difícil\n"))

if dificultad == 1:
    numero_random = random.randint(1,10)
    while vidas > 0:
        num = int(input("Por favor, ingrese un número del 1 al 10: \n"))

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
    if vidas == 0:
        print(f"Te quedaste sin vidas el número era: {numero_random}")

elif dificultad == 2:
    numero_random = random.randint(1,50)
    while vidas > 0:
        num = int(input("Por favor, ingrese un número del 1 al 50: \n"))

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
    if vidas == 0:
        print(f"Te quedaste sin vidas el número era: {numero_random}")

elif dificultad == 3:
    numero_random = random.randint(1,100)
    while vidas > 0:
        num = int(input("Por favor, ingrese un número del 1 al 100: \n"))

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
    if vidas == 0:
        print(f"Te quedaste sin vidas el número era: {numero_random}")





