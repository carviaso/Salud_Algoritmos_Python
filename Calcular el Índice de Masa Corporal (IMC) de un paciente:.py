# Solicita la formacion para calcular el IMC
peso = float(input("Ingrese el peso del paciente (kg): "))
altura = float(input("Ingrese la altura del paciente (m): "))

imc = peso / (altura ** 2)  # Fórmula del IMC

if imc < 18.5:
    categoria = "Bajo peso"
elif imc < 25:
    categoria = "Peso normal"
elif imc < 30:
    categoria = "Sobrepeso"
else:
    categoria = "Obesidad"

print(f"El IMC del paciente es {imc:.2f}, categoría: {categoria}")
