
while True:
    num = input("Ingresa un numero mayor a 0: ")
    
    # Verificamos que solo se ingresen numeros (usamos isdigit) y que sea mayor a 0
    if num.isdigit() and int(num) > 0:
        num = int(num)  # si da true, el número ingresado lo guarda en la variable num
    else:
        print("Entrada no valida")
        break

    # Ingrese una palabra o frase
    frase = input("Ingresa una palabra o frase: ")
    longitud = len(frase)
    print(f"La longitud de la palabra o frase es: {longitud}")
    
    # Calcular el factorial
    factorial = 1 # iniciamos en 1 xq el factorial arranca multiplicando x1
    for i in range(1, longitud + 1):
        factorial *= i
    print(f"El factorial de {longitud} es: {factorial}")
    
    # Par o impar
    if factorial % 2 == 0:
        print("El resultado es par.")
    else:
        print("El resultado es impar.")
    
    # Verificar si se desea iniciar de nuevo
    num = input("Ingresa un número mayor a 0 una letra para salir: ")
    if not (num.isdigit() and int(num) > 0):
        print("Entrada no válida, saliendo del programa =(")
        break
