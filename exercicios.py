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

#questão 07

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

#Questão 10

# linhas = 3
# colunas = 3 
# matriz = []
# soma_impar = 0

# for i in range(linhas):
#     linha = []
#     for j in range(colunas):
#         valor = int(input(f"Digite os valores das posicao: ({i},{j}): "))
#         linha += [valor]
#     matriz += [linha]

# for i in range(linhas):
#     for j in range(colunas):
#         if matriz[i][j] % 2 != 0:
#             soma_impar += 1

# print("Matriz:")

# for _ in matriz:
#     print(_)

# print(f"Números impares: {soma_impar}")
        

#Questão 11

# linhas = int(input("Digite o número de Linhas: "))
# colunas = int(input("Digite o número de Colunas: "))

# matriz = []
# for i in range(linhas):
#     linha = []
#     for j in range(colunas):
#         valor = int(input(f"Digite os valores da posição: ({i},{j}): "))
#         linha += [valor]
#     matriz += [linha]

# for i in range(linhas):
#     soma_linha = 0
#     for j in range(colunas):
#         soma_linha += matriz[i][j] 
#     print(f"{matriz[i]} = {soma_linha}")

#Questão 13

# linhas = 3
# colunas = 3
# matriz_a = []
# matriz_b = []
# matriz_resultante = [[0 for _ in range(linhas)] for _ in range(colunas)]

# print("Primeira matriz")
# for i in range(linhas):
#     linha = []
#     for j in range(colunas):
#         valor = int(input(f"Digite o valor das poisições ({i},{j}): "))
#         linha += [valor]
#     matriz_a += [linha]

# print("Segunda matriz")
# for i in range(linhas):
#     linha = []
#     for j in range(colunas):
#         valor = int(input(f"Digite o valor das poisições ({i},{j}): "))
#         linha += [valor]
#     matriz_b += [linha]

# for i in range(colunas):
#     for j in range(linhas):
#         if matriz_a[i][j] > matriz_b[i][j]:
#             matriz_resultante[i][j] = matriz_a[i][j]
#         if matriz_a[i][j] < matriz_b[i][j]:
#             matriz_resultante[i][j] = matriz_b[i][j]
#         else:
#             matriz_resultante[i][j] = matriz_a[i][j]
# print("Matriz a")
# for _ in matriz_a:
#     print(_)
# print("Matriz b")
# for _ in matriz_b:
#     print(_)

# print("matriz resultante:")

# for _ in matriz_resultante:
#     print(_)

#questão 15

# import random

# matriz = []
# linhas = random.randint(2,10)
# colunas = random.randint(2,10)

# for i in range(linhas):
#     linha = []
#     for j in range(colunas):
#         valor = random.randint(100,999)
#         linha.append(valor)
#     matriz.append(linha)

# menor_valor = matriz[0][0]
# maior_valor = matriz[0][0]
# menor_posicao = (0,0)
# maior_posicao = (0,0)

# for i in range(linhas):
#     for j in range(colunas):
#         if matriz[i][j] < menor_valor:
#             menor_valor = matriz[i][j]
#             menor_posicao = (i,j)
#         if matriz[i][j] > maior_valor:
#             maior_valor = matriz [i][j]
#             maior_posicao = (i,j)
            
# print("Matriz")
# for _ in matriz:
#     print(_)

# print(f"Menor valor: {menor_valor} ({menor_posicao})")
# print(f"Maior valor: {maior_valor} ({maior_posicao})")

#Questão 17

import random

linhas_a = int(input("Digite o valor de linhas da primeira matriz: "))
colunas_a = int(input("Digite o valor de colunas da primeira matriz: "))
linhas_b = int(input("Digite o valor de linhas da segunda matriz: "))
colunas_b = int(input("Digite o valor de colunas da seunda matriz: "))

if colunas_a != linhas_b:
    print("Impossibilidade de realizar o produto matricial")
else:

    matriz_a =[]
    matriz_b = []
    matriz_resultante = [[0 for _ in range(colunas_b)] for _ in range(linhas_a)]

    numero_aleatorio_inicial = int(input("Digite o valor do número alatorio inical: "))
    numero_aleatorio_final = int(input("Digite o valor do número alatorio inical: "))

    for i in range (linhas_a):
        linha_a = []
        for j in range(colunas_a):
            valor_a = random.randint(numero_aleatorio_inicial,numero_aleatorio_final)
            linha_a.append(valor_a)
        matriz_a.append(linha_a)

    for i in range (linhas_b):
        linha_b = []
        for j in range(colunas_b):
            valor_b = random.randint(numero_aleatorio_inicial,numero_aleatorio_final)
            linha_b.append(valor_b)
        matriz_b.append(linha_b)

    linhas_a = len(matriz_a)
    colunas_a = len(matriz_a[0])
    linha_b = len(matriz_b)
    colunas_b = len(matriz_b[0])

    for i in range(linhas_a):
        for j in range(colunas_b):
            for k in range(colunas_a):
                matriz_resultante[i][j] += matriz_a[i][k] * matriz_b[k][j]

    for linha in matriz_resultante:
        print(linha)

