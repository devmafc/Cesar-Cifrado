diccionario = {
    'A':0, "B":1, "C":2, 'D':3, "E":4, "F":5, "G":6, 
    "H":7, "I":8, "J":9, "K":10, "L":11, "M":12, "N":13,
    "Ñ":14, "O":15, "P":16, "Q":17,"R":18, "S":19, "T":20, 
    "U":21, "V":22, "W":23, "X":24, "Y":25, "Z":26 }


# def encriptar(mensaje, b):
    
#     lista = []
#     for i in mensaje:
#         if i == ' ': continue# Omite el espacio
#         m = (diccionario[i]) # Toma el valor de la clave y la devuelve como lista
#         ope = (m + b) % 27   # En la varible ope se guarda el caracter ya encriptado
#         for clave, valor in diccionario.items(): # Itera sobre el diccionario con 2 variables de iteracion que toman clave y valor 
#             if ope == valor:                     
#                 lista.append(clave)
#                 mensaje_encriptado = ' '.join(lista) # Convierte la lista de caracteres en cadena
        
#     return mensaje_encriptado

# mensaje = input('Ingrese mensaje a encriptar: ').upper()
# b = 7
# mensaje_encriptado = encriptar(mensaje, b)
# print(mensaje_encriptado)

# def dencriptar(mensaje_encriptado, b):
    
#     lista = []
#     for i in mensaje_encriptado:
#         if i == ' ': continue
#         m = (diccionario[i])
#         resultado = (m - b) % 27
#         for clave, valor in diccionario.items():
#             if resultado == valor:                     
#                 lista.append(clave)
#                 desencriptar = ' '.join(lista)
    
#     return desencriptar
    
# desencriptar = dencriptar(mensaje_encriptado, b)
# print(desencriptar)


#***********************************************************

def encriptar_caracter(caracter, b):
    
    if len(caracter) >= 2 or caracter == ' ':
        exit()
    valor = diccionario[caracter]
    resultado = (valor + b) % 27
    caracter_encriptado = list(diccionario.keys())[list(diccionario.values()).index(resultado)]
    
    return caracter_encriptado
    
    
carater = input('Ingrese caracter a encriptar: ').upper()
b = 8
caracter_encriptado = encriptar_caracter(carater, b)
print(caracter_encriptado)
    
def dencriptar_caracter(caracter_encriptado, b):
    
    valor = diccionario[caracter_encriptado]
    resultado = (valor - b) % 27
    carcater_desencriptado = list(diccionario.keys())[list(diccionario.values()).index(resultado)]
    return carcater_desencriptado

caracter_desencriptado = dencriptar_caracter(caracter_encriptado, b)
print(caracter_desencriptado)
    
    
    
    






    