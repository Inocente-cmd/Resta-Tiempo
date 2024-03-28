import time
from time import sleep
import time
import datetime 
from datetime import timedelta

import datetime

# Obtén la hora actual
dif_hora_1 = datetime.datetime.now()

while True:
    # Define otra hora (por ejemplo, 06:30:00 PM)
    dif_hora_2 = datetime.datetime.now()

    # Calcula la diferencia de tiempo
    diferencia = dif_hora_2 - dif_hora_1

    # Imprime la diferencia en horas, minutos y segundos
    #print("Nueva version: ", diferencia)

    diferencia_horas = diferencia.seconds // 3600
    diferencia_minutos = (diferencia.seconds % 3600) // 60
    diferencia_segundos = diferencia.seconds % 60
    dirent_total = diferencia_horas , diferencia_minutos , diferencia_segundos

    #print("Diferencia: ",dirent_total)
    #print("Diferencia: ",diferencia_horas,diferencia_minutos,diferencia_segundos)    
    #print(f"La diferencia entre las horas es: {diferencia_horas} horas, {diferencia_minutos} minutos y {diferencia_segundos} segundos.")


    import datetime

    # Tiempo en formato (horas, minutos, segundos)
    
    #tiempo_tupla = (0, 0, 5) # = dirent_total

    # Crear un objeto datetime con la fecha actual y el tiempo proporcionado
    fecha_actual = datetime.datetime.now()
    tiempo_objeto = fecha_actual.replace(hour=dirent_total[0], minute=dirent_total[1], second=dirent_total[2])

    # Formatear el tiempo como una cadena en el formato deseado (HH:MM:SS)
    tiempo_formateado = tiempo_objeto.strftime("%H:%M:%S")

    print("Tiempo formateado:", tiempo_formateado)
