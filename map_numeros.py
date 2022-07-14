# aplicar uma função matemática a todos os números de uma dada lista

lista = [2, 4, 5]
lista_mult = list(map(lambda x : 3*x**2 + 2/x + 1, lista))

print(lista_mult)