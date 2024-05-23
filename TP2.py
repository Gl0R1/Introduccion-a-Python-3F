# 1. Realizar un programa que me diga si un numero es par o impar.

num = int(input("Ingrese un número: "));
8
if num % 2 == 0:
  print("el numero ingresado es par");
else:
  print("el numero ingresado es impar");



# 2. Realizar un programa que genere la tabla de multiplicar de un numero, ingresado por el usuario (del 1 al 10).

num = int(input("Ingrese un número: "));

for i in range(1,11):
  resultado = num * i
  print(f"{num} x {i} = {resultado}");



# 3. Realizar un programa que le pida al usuario su numobre y edad y nos diga si es mayor de edad

nombre = input("Ingresa tu nombre: ");
edad = int(input("Ingrese su edad: "));

if edad <= 18 :
  print(f"{nombre} Usted es Menor de edad" )
else:
  print(f"{nombre} Usted es Mayor de edad" )
  



# 4. Realizar un programa donde el usuario ingrese una palabra y un numero e imprima 
#   por pantalla la palabra ingresa tantas veces como el numero ingresado.

palabra = input("Ingrese una palabra: ")
num = int(input("Ingrese un número: "))
cont = 0

while cont < num:
  cont += 1
  print(palabra)



# 5. Realizar un programa que sume los numeros ingresados por el usuario hasta que se ingrese un 0,
#    Al finalizar nos debe mostrar la suma por pantalla.
  
suma = 0
num = int(input("Ingrese un numero o (0 para terminar): "))

while num != 0:
  if num > 0:
    suma += num
    num = int(input("Ingrese un numero o (0 para terminar): "))

print("La suma de los numeros ingresados es:", suma)

