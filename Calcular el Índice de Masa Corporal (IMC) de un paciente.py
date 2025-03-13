# Solicita la formacion para calcular el IMC
## Entrada de datos
peso = float(input("Ingrese el peso del paciente (kg): "))
altura = float(input("Ingrese la altura del paciente (m): "))

# Cálculos (peso / altura^2)
imc = peso / (altura ** 2)  # Fórmula del IMC

# Condiciones (if, elif, else)
if imc < 18.5:
    categoria = "Bajo peso"
elif imc < 25:
    categoria = "Peso normal"
elif imc < 30:
    categoria = "Sobrepeso"
else:
    categoria = "Obesidad"

# Formato de salida ({imc:.2f} redondea a 2 decimales)
print(f"El IMC del paciente es {imc:.2f}, categoría: {categoria}")
