tamanho_da_lista = int(input('Qual é o tamanho da lista telefonica? '))
lista_de_nomes = []
lista_de_telefones = []
for listas in range(tamanho_da_lista):
    lista_de_nomes.append(input('escreva 1 nome: '))
    lista_de_telefones.append(input('escreva o numero da pessoa correspondente: '))

for i in range(len(lista_de_nomes)):
    print(lista_de_nomes[i])
    print(lista_de_telefones[i])