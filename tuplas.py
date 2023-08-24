estudiante =("felecity","Nuevas tecnologias",[4,1.7,4.9])

print("Cantidad de elementos de la lisa",len(estudiante))

nombre = estudiante[0]
modulo = estudiante[1]
notas = estudiante[2]

print(f"Nombre del estudiante: {nombre}\n El modulo: {modulo}\n Las notas son: {notas}")


for ind in estudiante:
    print(ind)