nomes = ['Murilo', 'André', 'Thomas', 'Gustavo', 'Nicolal'] #varios nomes dentro de uma variavel

print('antes do append')
for i in range(len(nomes)):
    nome = nomes [i]
    print(nome)
#e se eu quiser colocar de trás para frente?
#for i in range(len(nomes)):
  #  nome = nomes [len(nomes)-i-1]
   # print(nome)

nomes.append('Lucas') #coloca o nome Lucas no final da lista

print('Depois do append')
for i in range(len(nomes)):
    nome = nomes [i]
    print(nome)

#para remover nomes da lista é usado pop(indice do nome que quer remover)
nomes.pop(0)

print('Depois do pop')
for i in range(len(nomes)):
    nome = nomes [i]
    print(nome)

#já se você não sabe qual é o indice mas sabe o valor/nome você pode usar remove
nomes.remove('Nicolal')

print('Depois do remove')
for i in range(len(nomes)):
    nome = nomes [i]
    print(nome)