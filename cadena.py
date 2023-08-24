mensaje = "   Bienvenido ....  al curso   ....  de python "

# #metodo len, imprime el tamaño de longitud del string
# print("texto original", mensaje)
# print("El tamaño del texto es de", len(mensaje)) 

# # strip, quita espacios al inicio y al final
# sinEspacios = mensaje.strip()
# print("El texto sin espacios", sinEspacios)
# print("El tamaño del texto sin espacios es de", len(sinEspacios)) 

# #UPPER mayusculas sostenida
# print( sinEspacios.upper())

# # LOWER minuscula sostenida
# print(sinEspacios.lower())

# #title inicial de cada palabra en MAYUSCULA
# print( sinEspacios.title())

# #capitalize solo aplica a la primera letra
# print( sinEspacios.capitalize())

parrafo = mensaje.split('....')
print(parrafo[0])
print(parrafo[1])
print(parrafo[2])


