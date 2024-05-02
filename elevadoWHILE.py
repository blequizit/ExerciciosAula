x = int(input("Digite o valor de x (maior que 1): "))
y = int(input("Digite o valor de y (inteiro maior ou igual a 2): "))

resultado = 1
contador = 0

while contador < y:
    resultado *= x
    contador += 1

print(f"{x} elevado a {y} é igual a {resultado}.")
