#Escribir un programa que use un ciclo definido con rango numérico, que averigue a cuántos amigos quieren saludar, les pregunte los nombres de esos amigos/as, y los salude.
amigos=[]
numeroAmig=int(input('¿Cuántos amigos tienes?'))
rango=numeroAmig
print("Di el nombre de tus amigos para saludarlos")
for i in range(rango):
    nombres = input()
    amigos.append(nombres)
for amigo in amigos:
    print('Hola '+amigo)