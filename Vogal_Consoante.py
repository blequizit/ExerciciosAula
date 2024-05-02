frase = input('Digite uma frase: ')
lista_palavras = list(frase.lower())

vogal = 0
consoante = 0
espaco = 0

for i in range(len(lista_palavras)):
    if lista_palavras[i] == "a" or lista_palavras[i] == "e" or lista_palavras[i] == "i" or lista_palavras[i] == "o" or lista_palavras[i] == "u":
        vogal += 1
    elif lista_palavras[i] == " ":
        espaco += 1
    else:
        consoante += 1

print(f"O total de vogais é: {vogal}\n"
      f"O total de consoantes é: {consoante}\n")
