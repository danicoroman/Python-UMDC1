# Escribir un programa que use un ciclo definido con rango numérico, que pregunte los nombres de sus cinco mejores amigos/as, y los salude.
amigos=[]
print('Da el nombre de 5 amigos')
for i in [0,1,2,3,4]:
    nombres = input()
    amigos.append(nombres)
for amigo in amigos:
    print('Hola '+amigo)

