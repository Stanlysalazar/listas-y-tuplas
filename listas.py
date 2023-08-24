modulos = ["Logica de Programacion","Base de Datos","HTML5","Moviles","HTML5",'14043']
# print(modulos)


# print("Elemento inicial de la lista",modulos[0])
# print("Elemento final de la lista",modulos[-1])

# print("Nro de elmentos que contiene la lista", modulos[len(modulos)-1])

# print("Agregar un elemento a lista..Metologias agiles")
# modulos.append("Metologias agiles")
# print(modulos)
# print("Nro de elmentos que contiene la lista", modulos[len(modulos)-1])

# modulos.insert(2, "web2")
# print(modulos)

#print("Cantidad de veces que aparece HTML5  ",modulos.count("HTML5"))

print("Lista ordenada alfabeticamente")
modulos.sort()
# print(modulos)

i=1
for ind in modulos:
    print(i,ind)
    i=i+1