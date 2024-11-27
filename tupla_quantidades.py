def pegar_nomes():
    nomes = []
    quantidade = int(input('Qual será o tamanho da sua lista?: '))
    for i in range(quantidade):
        nomes.append(input('Coloque o nome: '))
    qtd_nomes = len(nomes)
    tupla = (nomes, qtd_nomes)
    return tupla


nomes, qtd_nomes = pegar_nomes()
for i in range(qtd_nomes):
    print(f'{i}   |    {nomes[i]}')