tamanho_da_lista = int(input('Qual é o tamanho da lista telefonica? '))
lista_de_nomes = []
lista_de_telefones = []
for listas in range(tamanho_da_lista):
    lista_de_nomes.append(input('escreva 1 nome: '))
    lista_de_telefones.append(input('escreva o numero da pessoa correspondente: '))

while True:
    nome = input('informe o nome da pessoa da qual quer ver o telefone: ') 
    try:
        indice = lista_de_nomes.index(nome)
        telefone = lista_de_telefones[indice]
        print(f'O telefone de {nome} é {telefone}')
    except ValueError as ex: # ou podemos fazer 'except Exception as ex:'
        print('Não existe esse nome') 