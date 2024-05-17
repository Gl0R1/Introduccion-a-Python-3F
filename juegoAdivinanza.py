#El juego termina cuando el Jugador acierta el numero o hace 5 intentos.
# #Cuando se pide ingresar el número se le debe indicar al  jugador el rango máximo y mínimo.
# Si el jugador falla, se debe indicar si el número es mayor o menor.
# Al perder se le enviara un mensaje indicandole que ha perdido y cual era el número.


import random

numero_secreto = random.randint(1, 20)

print("******** Adivina el Numero **********")
print("Ingresa un numero entre el 1 y el 20")

intentos = 0
bandera = True

while intentos < 5 and bandera:
    intentos += 1
    print(f"Intento número {intentos}")
    jugador = int(input("Ingresa tu número: "))

    if jugador == numero_secreto:
        print("Felicidades! Has adivinado el numero xD")
        bandera = False
        
    elif jugador < numero_secreto:
        print("El numero es mayor.")
    else:
        print("El numero es menor.")
    
    if intentos == 5 and bandera:
        print(f" Perdiste! El numero oculto era  {numero_secreto}")

        
  
        

    
    