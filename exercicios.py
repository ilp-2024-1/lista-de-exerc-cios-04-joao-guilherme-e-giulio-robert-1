#QUestão 01

# lista_usuario = []
# soma_par = 0

# for _ in range(10):
#     valor = int(input("Digite os valores da lista: "))
#     lista_usuario += [valor]

# for elementos in lista_usuario:
#     if elementos % 2 == 0:
#         soma_par += 1
# print(f"Qtd valores par: {soma_par}")

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

#questão 03
# lista_usuario = []
# soma_par = 0

# for _ in range(10):
#     valor = int(input("Digite os valores da lista: "))
#     lista_usuario += [valor]
# for elemento in lista_usuario:
#     if elemento % 2 == 0 and elemento != 0:
#         soma_par += 1

# print(f"Quantidade de valores par: {soma_par}")


# Questão 04
# tamanho_da_lista = int(input('Digite o valor das listas: '))
# primeira_lista = []
# primeiro_valor_boolean = False
# primeiro_valor_numerico = 0
# elemento_desejado_cert = ['boolean', 'string', 'numero']

# for i in range(tamanho_da_lista):
#     if i == 0:
#         primeiro_valor = input('Digite o primeiro valor string: ')
#         primeira_lista += [primeiro_valor]
#     elif i == 1:
#         primeiro_valor_boolean = bool(input('Digite o primeiro valor boolean: '))
#         primeira_lista += [primeiro_valor_boolean]
#     elif i == 2:
#         primeiro_valor_numerico = int(input('Digite o primeiro valor numerico: '))
#         primeira_lista += [primeiro_valor_numerico]
#     else:
#         outro_valor_numerico = 0
#         elemento_desejado = input('Digite o tipo de elemento desejado: ')
#         while elemento_desejado not in elemento_desejado_cert:
#             print('Elemento inválido.')
#             elemento_desejado = input('Digite outro tipo de elemento desejado: ')
#         if elemento_desejado == elemento_desejado_cert[0]:
#             outro_valor_boolean = bool(input('Digite outro valor boolean: '))
#             primeira_lista += [outro_valor_boolean]
#         elif elemento_desejado == elemento_desejado_cert[1]:
#             outro_valor_string = input('Digite outro valor string: ')
#             primeira_lista += [outro_valor_string]
#         else:
#             outro_valor_numerico = int(input('Digite outro valor numerico: '))
#             primeira_lista += [outro_valor_numerico]

# segunda_lista = []
# segundo_valor_boolean = False
# segundo_valor_numerico = 0


# for k in range(tamanho_da_lista):
#     if k == 0:
#         segundo_valor = input('Digite o primeiro valor string: ')
#         segunda_lista += [segundo_valor]
#     elif k == 1:
#         segundo_valor_boolean = bool(input('Digite o primeiro valor boolean: '))
#         segunda_lista += [segundo_valor_boolean]
#     elif k == 2:
#         segundo_valor_numerico = int(input('Digite o primeiro valor numerico: '))
#         segunda_lista += [segundo_valor_numerico]
#     else:
#         segundo_outro_valor_numerico = 0
#         elemento_desejado = input('Digite o tipo de elemento desejado: ')
#         while elemento_desejado not in elemento_desejado_cert:
#             print('Elemento inválido.')
#             elemento_desejado = input('Digite outro tipo de elemento desejado: ')
#         if elemento_desejado == elemento_desejado_cert[0]:
#             segundo_outro_valor_boolean = bool(input('Digite outro valor boolean: '))
#             segunda_lista += [segundo_outro_valor_boolean]
#         elif elemento_desejado == elemento_desejado_cert[1]:
#             segundo_outro_valor_string = input('Digite outro valor string: ')
#             segunda_lista += [segundo_outro_valor_string]
#         else:
#             segundo_outro_valor_numerico = int(input('Digite outro valor numerico: '))
#             segunda_lista += [segundo_outro_valor_numerico]

# lista_resultante = []
# for n in range(tamanho_da_lista):
#     lista_resultante += [primeira_lista[n]]
#     lista_resultante += [segunda_lista[n]]
# print(lista_resultante)

#Questão 05

# tamanho = int(input("Digite quantos valores serao fornecidos: "))
# lista_usuario = []
# soma = 0

# for _ in range(tamanho):
#     valor = int(input("Digite os valores da lista: "))
#     lista_usuario += [valor]

# menor_valor = lista_usuario[0]
# maior_valor = lista_usuario [0]

# for elemento in lista_usuario:
#     if elemento < menor_valor:
#         menor_valor = elemento
#     elif elemento > maior_valor:
#         maior_valor = elemento
#     soma += elemento

# media = soma / len(lista_usuario)

# print(f"menor valor: {menor_valor}")
# print(f"maior valor: {maior_valor}")
# print(f"Media aritimetica: {media}")


#Questão 06

# tamanho_da_lista = int(input('Digite o tamanho da lista: '))

# lista_um = []
# for i in range(tamanho_da_lista):
#     valor_num = int(input('Digite os valores numéricos dentro da lista: '))
#     lista_um += [valor_num]

# lista_dois = []
# for j in range(tamanho_da_lista):
#     valor_string = input('Digite a quantidade de letras proporcional à quantidade de números: ')
#     lista_dois += [valor_string]

# lista_resultante = []
# for k in range(tamanho_da_lista):
#     print(k)
#     if k % 2 != 0:
#         lista_resultante += [lista_dois[k]]
#     else:
#         lista_resultante += [lista_um[k]]
# print(lista_resultante)

#Questão 08

lista_inicial = input('Digite os números por espaço: ')
lista_final = lista_inicial.split()

lista_numero = [int(numero) for numero in lista_final]
soma_num = 0
i = 0

for valor in lista_numero:
    i += 1
    if valor % 2 != 0:
        soma_num += valor
        print(valor, end='+')
        



