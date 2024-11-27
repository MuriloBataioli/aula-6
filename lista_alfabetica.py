minha_lista = ['fulano', 'ciclano', 'deltrano']
print('Antes', minha_lista)

#meu codigo
for i in range(len(minha_lista)):
    minha_lista[i] = minha_lista[i].upper()
    
minha_lista.sort()
    
print('Depois', minha_lista)