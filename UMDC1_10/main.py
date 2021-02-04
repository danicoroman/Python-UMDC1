#Escribir un programa que reciba un número n por parámetro e imprima los primeros números triangulares, junto con su índice. Los números triangulares se obtienen mediante la suma de los números naturales desde 1 hasta n. Es decir, si se piden los primeros 5 números triangulares, el programa debe imprimir:
#n ∗ (n + 1)
#1 - 1
#2 - 3
#3 - 6
#4 - 10
#5 - 15
i=1
num=int(input('Establezca un rango(un número)'))
for i in range(1,num + 1):
    num= (i * (i + 1)) /2
    print(i ,'-' ,int(num))



