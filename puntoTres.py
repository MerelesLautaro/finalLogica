import csv
from operator import itemgetter
#Inicializamos el diccionario
diccionario=[]

# Leerlo y almacenarlo en un diccionario
with open('datos.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        #Aniadimos los datos con el metodo append
        diccionario.append({
            'nombre': row['nombre'],
            'apellido': row['apellido'],
            'correo_electronico': row['correo_electronico']
        })
        
#Escribir en el archivo punto_3/datos_sin_com.csv sólo los registros cuyo correo electrónico no sean ".com"
#Pasos 1. crear una nueva lista para los correos sin el .com
#2. Recorremos los elementos de el indice 'correo_electronico' con un forEach, si el elemento termina en '.com' retorna False y no lo agrega // metodo endswith
correos_sin_com = [e for e in diccionario 
                   if not e['correo_electronico'].endswith('.com')]

#Imprime los correos sin el .com
for e in correos_sin_com:
   print(e['nombre'], e['apellido'], e['correo_electronico'])
    
