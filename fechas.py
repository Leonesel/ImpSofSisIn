#fechas.py
from datetime import datetime
ahora = datetime.now()
print(ahora.year) #Año actual
print(ahora.strftime("%A")) # Día de hoy
fecha = datetime (2009,4,13)
print(fecha.strftime("%B")) #Mes  una fecha
str_fecha = "13/04/09 12:58:00"
fecha_obj = datetime.strptime(str_fecha,"%d/%m/%y %H:%M:%S")

print(ahora-fecha_obj)