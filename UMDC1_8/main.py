#Utilice el programa anterior para generar una tabla de conversión de temperaturas, desde 0º F hasta 120º F, de 10 en 10.
faren = 0
centi=0
while faren < 120:
    centi = (faren - 32) / 1.8
    faren= faren + 10
    print('Hay ', round(centi, 2), "Cº")

