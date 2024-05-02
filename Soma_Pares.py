# Solicita ao usuário um número inteiro positivo
numero = int(input("Digite um número inteiro positivo: "))

# Inicializa a soma
soma = 0

# Verifica se o número inserido é positivo
if numero > 0:
    # Itera de 1 até o número inserido (incluindo-o)
    for i in range(1, numero + 1):
        # Verifica se o número é par
        if i % 2 == 0:
            # Adiciona o número par à soma
            soma += i

    # Imprime a soma dos números pares
    print("A soma dos números pares até", numero, "é:", soma)
else:
    print("O número inserido não é positivo. Por favor, insira um número inteiro positivo.")
