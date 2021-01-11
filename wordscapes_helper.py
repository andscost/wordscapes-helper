from english_words import english_words_set
from itertools import *

def anagrama(palavra):
    lista = []
    for num in range(3,len(palavra)+1):
        perm = permutations(palavra, num)
        for i in perm:
            result = ''
            for j in range(0,num):
                result += i[j]
            lista.append(result)
    return list(dict.fromkeys(lista))

def listar(palavra,n):
    lista = []
    perm = permutations(palavra, n)
    for i in perm:
        result = ''
        for j in range(0,n):
            result += i[j]
        lista.append(result)
    return lista

#---------------------------------------------
while True:
    print('*'*20)
    selecionar = input('escreva as letras: ')
    for teste in anagrama(selecionar):
        if teste in english_words_set:
            print(teste)
    manter = True
    while manter:
        deseja_listar = int(input('escreva um numero para procurar todos os anagramas possiveis (0 caso queira passar de fase): '))
        if deseja_listar > 0:
            letras = {}
            while manter:
                posicao = int(input('escreva a posição de uma letra na palavra (0 caso nao tenha): '))
                if posicao > 0 and posicao <= len(selecionar):
                    letra = input(f'escreva a letra que corresponde a posicao {posicao}: ')
                    letras[letra] = posicao-1
                    nova_letra = input('tem uma nova letra (sim: escreva algo / nao: apenas de enter): ')
                    if len(nova_letra) < 1:
                        manter = False
                else:
                    manter = False
            lista_letras = ['_']*deseja_listar
            for letra,posicao in letras.items():
                lista_letras[posicao] = letra  
            palavras = listar(selecionar,deseja_listar)
            for palavra in palavras:
                num = 0
                negar = False
                for i in palavra:
                    if i != lista_letras[num] and lista_letras[num] != '_':
                        num += 1
                        negar = True
                    else:
                        num += 1
                if negar == False:
                    print(palavra)
            manter = True
        else:
            manter = False


