#Escribir un programa que imprima todos los números pares entre dos números que se le pidan al usuario.
num1=int(input('Dame un número'))
num2=int(input('Dame otro número'))
while num1 < num2:
    if num1 % 2 == 0:
        print(num1)
        num1 = num1 + 2
    else:
        num1= num1 + 1
        print(num1)
        num1 = num1 + 2
while num2 < num1:
    if num2 % 2 == 0:
        print(num2)
        num2 = num2 + 2
    else:
        num2= num2 + 1
        print(num2)
        num2 = num2 + 2
