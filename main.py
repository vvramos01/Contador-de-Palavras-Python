texto = input("Digite uma frase: ")
palavras = texto.split()
print(f"Total de palavras: {len(palavras)}")

contagem = {}
for p in palavras:
    contagem[p] = contagem.get(p,0)+1

print("Contagem por palavra:")
for p,qtd in contagem.items():
    print(f"{p}: {qtd}")
