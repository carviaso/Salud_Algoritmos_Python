…

# Librería necesaria
from datetime import date

# Funciones necesarias

# Función para calcular los días transcurrido entre 2 fechas

def dias_entre(d1, d2):
    """
    Función que calcula los días transcurrido entre 2 fechas

    Parámetros de entrada:
    d1: Fecha inicial
    d2: Fecha final

    Salida:
    Devuelve el número de días transcurrido entre las 2 fechas
    """
    
    return abs(d2 - d1).days

# Función que devuelve la fecha de ingreso de una historia clínica
# concreta a partir de un índice determinado y de un dataset que
# se le pasa como entrada

def busca_historia(historia_clinica, desde, dataset):
    """
    Función que busca una Historia Clínica a partir de un índice determinado para buscar su fecha de ingreso en el hospital
    
    Parámetros de entrada:
        historia_clinica: Código de Historia Clínica
  desde: índice desde el que empezar a buscar la Historia Clínica
        dataset: Conjunto de datos donde busca los datos
    
    Salida:
        Devuelve la fecha de ingreso en formato fecha
    """
    
    if desde <= len(dataset):
        for c in range(desde, len(dataset)):
            if dataset['HISTORIA_COD'][c] == historia_clinica:
                fecha = date(int(dataset['FECING'][c][0:4]), int(dataset['FECING'][c][5:7]), int(dataset['FECING'][c][8:]))
                return fecha

# Función que modifica el dataset de entrada con el número de días
# transcurridos en las readmisiones

def calcula_dias_Readmision(desde, dataset):
    """
    Función que busca Readmisiones para calcular el número de días
    que ha pasado desde que ingresa hasta su próxima readmisión

    Parámetros de entrada:
        desde: índice desde el que empezar a buscar la historia clínica
        dataset: Conjunto de datos donde se encuentra los casos (registros) a estudiar

    Salida:
        El dataset de entrada será modificado (dataset['READMISION']) indicando si el número de días pasado desde el ingreso hasta la readmisión 
    """
    
    if desde <= len(dataset):
        # Recorremos el dataset
        for c in range(desde, len(dataset)):
            # Guardamos la fecha de ingreso de la posición actual
            fecha1 = date(int(dataset['FECING'][c][0:4]), int(dataset['FECING'][c][5:7]), int(dataset['FECING'][c][8:]))
            # Buscamos un reingreso a futuro y recuperamos su fecha de ingreso
            fecha2 = busca_historia(dataset['HISTORIA_COD'][c], c+1, dataset)
            if fecha2 is None:
                num_dias = 0
            else:
                num_dias = dias_entre(fecha1, fecha2)
            
            # Solo modificamos el dataset si encuentra una readmisión
            if num_dias > 0:
                dataset['READMISION'][c] = num_dias
                
…

# Ejecutamos algoritmo para rellenar la característica READMISION con
# los valores a futuro del número días readmisión

calcula_dias_Readmision(0, conjunto_de_datos)

# Ejemplo para Readmisiones a 7 días
# Creamos dataset con readmisiones de 7 o menos días

conjunto_de_datos_r7_pre = conjunto_de_datos[conjunto_de_datos ['READMISION'] < 8]

# Creamos dataset con readmisones mayores que 0, es decir, que
# sean readmisiones (0 = no hay readmisión)

conjunto_de_datos_r7 = conjunto_de_datos_r7_pre[conjunto_de_datos_r7_pre['READMISION'] > 0]

…