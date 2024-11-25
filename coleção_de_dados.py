#coleções de dados são recursos que armazenam dados de forma agrupada
#lista:     ['a', 'b', 'c', 'd']
#indice:      0    1    2    3   são assim correspondente
# lista é um arranjo sequencial de dados, enumerados de 0 a N-1


nome = 'Murilo' #somente 1 nome
nomes = ['Murilo', 'André', 'Thomas', 'Gustavo', 'Nicolal'] #varios nomes dentro de uma variavel

primeiro_nome = nomes[0]
segundo_nome = nomes[1]
quinto_nome = nomes[4]

print(primeiro_nome)
print(type(nomes))
#type é para mostrar se é str, int, float ou bool
print(primeiro_nome)
print(segundo_nome)
print(quinto_nome)

# e como saber qual é o ultimo nome de uma lista que varia? len(nome da lista) 1 ou voçê pode colocar somente o -1 pois em python ele considera como se voçê quisesse pegar ao contrario