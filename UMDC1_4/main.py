# Escribir un programa que use un ciclo definido con rango numérico, que pregunte los nombres de sus seis mejores amigos/as, y los salude.
amigos=[]
print('Da el nombre de 6 amigos')
for i in [0,1,2,3,4,5]:
    nombres = input()
    amigos.append(nombres)
for amigo in amigos:
    print('Hola '+amigo)