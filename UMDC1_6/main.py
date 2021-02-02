#Escribir un programa que le pregunte al usuario una cantidad de pesos, una tasa de interés y un número de años y muestre como resultado el monto final a obtener. La fórmula a utilizar es:

#Cn = C * (1 + x/100) ^ n

#Donde C es el capital inicial, x es la tasa de interés y n es el número de años a calcular.

capIni=float(input("Pon el capital inicial"))
tasa=float(input("Ahora el interés"))
anno=float(input("¿A cuántos años?"))
capTot= capIni * (1 + tasa/100).__pow__(anno)
print("El dinero total será de " ,float(capTot))