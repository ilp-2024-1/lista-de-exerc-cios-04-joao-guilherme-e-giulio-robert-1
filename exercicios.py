# Questão 02

# tamanho_da_lista = int(input('Digite o tamanho das listas: '))
# primeira_lista = []
# segunda_lista = []
# primeira_soma_par = 0
# primeira_soma_impar = 0
# segunda_soma_par = 0
# segunda_soma_impar = 0

# for i in range(tamanho_da_lista):
#     valores_da_primeira_lista = int(input('Digite aqui os valores da lista: '))
#     valores_da_segunda_lista = int(input('Digite os valores da segunda lista: '))
#     primeira_lista += [valores_da_primeira_lista]
#     segunda_lista += [valores_da_segunda_lista]
#     if primeira_lista[i] % 2 == 0:
#         primeira_soma_par += primeira_lista[i]
#     else: 
#         primeira_soma_impar += primeira_lista[i]
#     if segunda_lista[i] % 2 == 0:
#         segunda_soma_par += segunda_lista[i]
#     else:
#         segunda_soma_impar += segunda_lista[i]

# print(f'Soma listapar1:{primeira_soma_par}')
# print(f'Soma listapar2:{segunda_soma_par}')
# if primeira_soma_par > segunda_soma_par:
#     print('Soma listapar1 > Soma listapar2')
# elif primeira_soma_par == segunda_soma_par:
#     print('Soma listapar1 = Soma listapar2')
# else:
#     print('Soma listapar2 > Soma listapar1')
# print(f'Soma listaimpar1:{primeira_soma_impar}')
# print(f'Soma listaimpar2:{segunda_soma_impar}')
# if primeira_soma_impar > segunda_soma_impar:
#     print('Soma listaimpar1 > Soma listaimpar2')
# elif primeira_soma_impar == segunda_soma_impar:
#     print('Soma listaimpar1 = Soma listaimpar2')
# else:
#     print('Soma listaimpar2 > Soma listaimpar1')

# Questão 04
tamanho_da_lista = int(input('Digite o valor das listas: '))
primeira_lista = []
primeiro_valor_boolean = False
outro_valor_boolean = True
primeiro_valor_numerico = 0
elemento_desejado_cert = ['boolean', 'string', 'numero']
for i in range(tamanho_da_lista):
    if i == 0:
        primeiro_valor = input('Digite o primeiro valor string: ')
        primeira_lista += [primeiro_valor]
    elif i == 1:
        primeiro_valor_boolean = bool(input('Digite o primeiro valor boolean: '))
        primeira_lista += [primeiro_valor_boolean]
    elif i == 2:
        primeiro_valor_numerico = int(input('Digite o primeiro valor numerico: '))
        primeira_lista += [primeiro_valor_numerico]
    else:
        outro_valor_numerico = 0
        elemento_desejado = input('Digite o tipo de elemento desejado: ')
        while elemento_desejado not in elemento_desejado_cert:
            print('Elemento inválido.')
            elemento_desejado = input('Digite outro tipo de elemento desejado: ')
        if elemento_desejado == elemento_desejado_cert[0]:
            outro_valor_boolean = bool(input('Digite outro valor boolean: '))
            primeira_lista += [outro_valor_boolean]
        elif elemento_desejado == elemento_desejado_cert[1]:
            outro_valor_string = input('Digite outro valor string: ')
            primeira_lista += [outro_valor_string]
        else:
            outro_valor_numerico = int(input('Digite outro valor numerico: '))
            primeira_lista += [outro_valor_numerico]
print(primeira_lista)