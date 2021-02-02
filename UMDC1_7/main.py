#Escribir un programa que convierta un valor dado en grados Fahrenheit a grados Celsius. Recordar que la fórmula para la conversión es: F = 9/5 * C + 32.
faren=int(input('Pon los grados para convertirlos a Celsius'))
centi=(faren - 32) / 1.8
print('Hay ' ,round(centi, 2) ,"Cº")
