# adicionar marcações de html em cada elemento da lista
# adicionar <div> string </div>

lista = ['cavalo', 'roupa de cama', 'cabelo', 'casa amarela']

html = list(map(lambda x : '<div>' + x + '</div>', lista))

print(html)

