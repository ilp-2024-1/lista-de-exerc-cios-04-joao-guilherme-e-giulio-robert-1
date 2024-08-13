tamanho_da_lista = int(input('Digite o tamanho das listas: '))
primeira_lista = []
segunda_lista = []
primeira_soma_par = 0
primeira_soma_impar = 0
segunda_soma_par = 0
segunda_soma_impar = 0

for i in range(tamanho_da_lista):
    valores_da_primeira_lista = int(input('Digite aqui os valores da lista: '))
    valores_da_segunda_lista = int(input('Digite os valores da segunda lista: '))
    primeira_lista += [valores_da_primeira_lista]
    segunda_lista += [valores_da_segunda_lista]
    if primeira_lista[i] % 2 == 0:
        primeira_soma_par += primeira_lista[i]
    else: 
        primeira_soma_impar += primeira_lista[i]
    if segunda_lista[i] % 2 == 0:
        segunda_soma_par += segunda_lista[i]
    else:
        segunda_soma_impar += segunda_lista[i]

print(f'Soma listapar1:{primeira_soma_par}')
print(f'Soma listapar2:{segunda_soma_par}')
if primeira_soma_par > segunda_soma_par:
    print('Soma listapar1 > Soma listapar2')
elif primeira_soma_par == segunda_soma_par:
    print('Soma listapar1 = Soma listapar2')
else:
    print('Soma listapar2 > Soma listapar1')
print(f'Soma listaimpar1:{primeira_soma_impar}')
print(f'Soma listaimpar2:{segunda_soma_impar}')
if primeira_soma_impar > segunda_soma_impar:
    print('Soma listaimpar1 > Soma listaimpar2')
elif primeira_soma_impar == segunda_soma_impar:
    print('Soma listaimpar1 = Soma listaimpar2')
else:
    print('Soma listaimpar2 > Soma listaimpar1')

