…

# Librería necesaria
import pandas as pd

# Leemos el fichero CSV que contiene las Enfermedades digestivas
# relacionadas realizado por doctores en medicina. Este archivo
# contiene un listado de las enfermedades según la codificación
# internacional CIE9MC2014

enf = pd.read_csv('EnfermedadesDig_CIE9MC2014v2.csv')

…

# Funciones necesarias

# Función para comprobar si tiene “-“
def tiene_guion(entrada):
    texto = str(entrada)
    result = texto.find("-")
    if result < 0:
        return False
    else:
        return True

# Función para comprobar si tiene V
def tiene_V(entrada):
    texto = str(entrada)
    result = texto.find("V")
    if result < 0:
        return False
    else:
        return True

# Función para extraer los números Si tiene guión y SI tiene V (Ejem.: ‘V44.1-V44.4’)
def extraeNums_g_V(entrada):
    texto = str(entrada)
    num1 = float(texto[1:texto.find("-")])
    num2 = float(texto[texto.find("-")+2:len(texto)])
    return num1,num2

# Función para extraer los números Si tiene guion y NO tiene V (Ejem.: ‘571.0-571.3’)
def extraeNums_g(entrada):
    texto = str(entrada)
    num1 = float(texto[0:texto.find("-")])
    num2 = float(texto[texto.find("-")+1:len(texto)])
    return num1,num2

# Función para extraer el número Si NO tiene guión y SI tiene V (Ejem.: ‘V12.54’)
def extraeNum_V(entrada):
    texto = str(entrada)
    num = float(texto[1:len(texto)])
    return num

# Función para saber si es un número
def es_numero(n):
    try:
        float(n)
    except ValueError:
        return False
    return True

# Función para saber si es nan (NaN)
def es_nan(n):
    var = str(n)
    if var == 'nan':
        return True
    else:
        return False

# Función para saber si NO es nan (NaN)
def noes_nan(n):
    var = str(n)
    if var == 'nan':
        return False
    else:
        return True

# Función para buscar si es de Digestivo un diagnóstico
def busca_digestivo(diagnostico, enfermedades_digestivo, dataset):
    for c in range(len(dataset)):
        for e in range(len(enfermedades_digestivo)):
            if noes_nan(dataset[diagnostico][c]):
                if dataset['DIGESTIVO'][c] == 0:
                    if tiene_guion(enfermedades_digestivo['id'][e]):
                        if tiene_V(enfermedades_digestivo['id'][e]):
                            if tiene_V(dataset[diagnostico][c]):
                                numc = extraeNum_V(dataset[diagnostico][c])
                                inf, sup = extraeNums_g_V(enfermedades_digestivo['id'][e])
                                if numc >= inf and numc <= sup:
                                    dataset['DIGESTIVO'][c] = 1
                                else:
                                    dataset['DIGESTIVO'][c] = 0
                            else:
                                dataset['DIGESTIVO'][c] = 0
                        else:
                            if tiene_V(dataset[diagnostico][c]):
                                dataset['DIGESTIVO'][c] = 0
                            else:
                                if es_numero(dataset[diagnostico][c]):
                                    inf, sup = extraeNums_g(enfermedades_digestivo['id'][e])
                                    if float(dataset[diagnostico][c]) >= inf and float(dataset[diagnostico][c]) <= sup:
                                        dataset['DIGESTIVO'][c] = 1
                                    else:
                                        dataset['DIGESTIVO'][c] = 0
                                else:
                                    dataset['DIGESTIVO'][c] = 0
                    else:
                        if tiene_V(dataset[diagnostico][c]):
                            numc = extraeNum_V(dataset[diagnostico][c])
                            if tiene_V(enfermedades_digestivo['id'][e]):
                                nume = extraeNum_V(enfermedades_digestivo['id'][e])
                                if numc == nume:
                                    dataset['DIGESTIVO'][c] = 1
                                else:
                                    dataset['DIGESTIVO'][c] = 0
                            else:
                                dataset['DIGESTIVO'][c] = 0
                        else:
                            if tiene_V(enfermedades_digestivo['id'][e]):
                                dataset['DIGESTIVO'][c] = 0
                            else:
                                if es_numero(dataset[diagnostico][c]):
                                    if float(dataset[diagnostico][c]) == float(enfermedades_digestivo['id'][e]):
                                        dataset['DIGESTIVO'][c] = 1
                                    else:
                                        dataset['DIGESTIVO'][c] = 0
                                else:
                                    dataset['DIGESTIVO'][c] = 0

…

# Creamos una columna nueva (DIGESTIVO) con todos los valores a 0

DIGESTIVO = cmbd['GRDS'].astype('int')
DIGESTIVO.name = 'DIGESTIVO'
cmbd2 = cmbd.join(DIGESTIVO)
cmbd2['DIGESTIVO'] = 0

…

# Buscamos en todos los diagnósticos si existe alguna enfermedad
# relacionada con Digestivo en el conjunto de datos (cmbd2). En 
# este caso tenemos 13 posibles diagnósticos (D1 a D13)

for i in range(13):
    busca_digestivo('D' + str(i+1), enf, cmbd2)
    
…