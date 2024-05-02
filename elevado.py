x = int(input("Digite o valor de x (maior que 1): "))
y = int(input("Digite o valor de y (inteiro maior ou igual a 2): "))

resultado = 1

for i in range(y):
    resultado *= x

print(f"{x} elevado a {y} é igual a {resultado}.")
