#Entre com 3 números em 3 variáveis diferentes ordene imprimindo também a
#classificação: menor, intermediário, maior

num1 = int(input("Digite um número: "))
num2 = int(input("Digite outro número: "))
num3 = int(input("Digite outro número: "))

if num1>num2 and num1>num3 and num2>num3:
    print(f"O maior numero é:{num1}, o intermediário é: {num2}, e o menor é:{num3}")

elif num1>num2 and num1>num3 and num3>num2:
    print(f"O maior numero é:{num1}, o intermediário é: {num3}, e o menor é:{num2}")

elif num2>num1 and num2>num3 and num1>num3:
    print(f"O maior numero é:{num2}, o intermediário é: {num1}, e o menor é:{num3}")

elif num2>num1 and num2>num3 and num3>num1:
    print(f"O maior numero é:{num1}, o intermediário é: {num3}, e o menor é:{num2}")

elif num3>num1 and num3>num2 and num1>num2:
    print(f"O maior numero é:{num3}, o intermediário é: {num1}, e o menor é:{num2}")

elif num3>num2 and num3>num2 and num2>num1:
    print(f"O maior numero é:{num3}, o intermediário é: {num2}, e o menor é:{num1}")
