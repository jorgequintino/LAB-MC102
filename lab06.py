# Cálculo de vetores de hiperespaço.

from typing import Tuple


def equalizador_vetores(
        vetor1: list[int], vetor2: list[int], numb1: int, numb2: int
) -> Tuple[list[int], list[int]]:
    '''Transforma os vetores em mesmo tamanho. Caso o primeiro vetor
    seja maior, adiciona o número "numb2" ao final, caso ele seja
    o menor, adiona o número "numb1"'''
    if len(vetor1) > len(vetor2):
        for _ in range(len(vetor1) - len(vetor2)):
            vetor2.append(numb2)
    elif len(vetor1) < len(vetor2):
        for _ in range(len(vetor2) - len(vetor1)):
            vetor1.append(numb1)
    return vetor1, vetor2


def soma_vetores(vetor1: list[int], vetor2: list[int]) -> list[int]:
    '''Soma os elementos de mesmo índice dos vetores.'''
    vetor1, vetor2 = equalizador_vetores(vetor1, vetor2, 0, 0)
    return [vetor1[i] + vetor2[i] for i in range(len(vetor1))]


def subtrai_vetores(vetor1: list[int], vetor2: list[int]) -> list[int]:
    '''Subtrai os elementos de mesmo índice dos vetores.'''
    vetor1, vetor2 = equalizador_vetores(vetor1, vetor2, 0, 0)
    return [vetor1[i] - vetor2[i] for i in range(len(vetor1))]


def multiplica_vetores(vetor1: list[int], vetor2: list[int]) -> list[int]:
    '''Multiplica os elementos de mesmo índice dos vetores.'''
    vetor1, vetor2 = equalizador_vetores(vetor1, vetor2, 1, 1)
    return [vetor1[i] * vetor2[i] for i in range(len(vetor1))]


def divide_vetores(vetor1: list[int], vetor2: list[int]) -> list[int]:
    '''Divide os elementos de mesmo índice dos vetores.'''
    vetor1, vetor2 = equalizador_vetores(vetor1, vetor2, 0, 1)
    return [vetor1[i] // vetor2[i] for i in range(len(vetor1))]


def multiplicacao_escalar(vetor: list[int], escalar: int) -> list[int]:
    '''Multiplica os elementos de um vetor por um número.'''
    vetor = [vetor[i] * escalar for i in range(len(vetor))]
    return vetor


def n_duplicacao(vetor: list[int], n: int) -> list[int]:
    '''Replica os vetores n vezes.'''
    if n != 0:
        vetor = n*vetor
    else:
        vetor = []
    return vetor


def soma_elementos(vetor: list[int]) -> int:
    '''Soma todos os elementos do vetor.'''
    add = 0
    for i in range(len(vetor)):
        add += vetor[i]
    return add


def produto_interno(vetor1: list[int], vetor2: list[int]) -> int:
    '''Multiplica os elementos de mesmo índice de um vetor e
    depois efetua a soma dos valores.'''
    vetor1, vetor2 = equalizador_vetores(vetor1, vetor2, 1, 1)
    vetor = multiplica_vetores(vetor1, vetor2)
    resultado = soma_elementos(vetor)
    return resultado


def multiplica_todos(vetor1: list[int], vetor2: list[int]) -> list[int]:
    '''Multiplica cada elemento do vetor1 pelos elementos do
        vetor2 e efetua a soma desses valores. Transforma
        em vetor cujos elementos são as somas efetuadas.'''
    vetor = []
    for i in range(len(vetor1)):
        add = 0
        for j in range(len(vetor2)):
            add += vetor1[i] * vetor2[j]
        vetor.append(add)
    return vetor


def correlacao_cruzada(vetor: list[int], mascara: list[int]) -> list[int]:
    '''Calcula um produto interno de vetor e máscara,
    no qual caminha-se os elementos do vetor.'''
    vector = []
    for i in range(len(vetor) - len(mascara) + 1):
        add = 0
        for j in range(len(mascara)):
            add += vetor[i + j] * mascara[j]
        vector.append(add)
    return vector


def main() -> None:
    '''Chama as funções correspondentes e as executa de
    sacordo com seus parametros.'''
    vetor = [int(entry1) for entry1 in input().split(sep=",")]
    while True:
        command = input()
        if command == "soma_vetores":
            vetor2 = [int(entry2) for entry2 in input().split(sep=",")]
            vetor = soma_vetores(vetor, vetor2)
            print(vetor)
        elif command == "subtrai_vetores":
            vetor2 = [int(entry2) for entry2 in input().split(sep=",")]
            vetor = subtrai_vetores(vetor, vetor2)
            print(vetor)
        elif command == "multiplica_vetores":
            vetor2 = [int(entry2) for entry2 in input().split(sep=",")]
            vetor = multiplica_vetores(vetor, vetor2)
            print(vetor)
        elif command == "divide_vetores":
            vetor2 = [int(entry2) for entry2 in input().split(sep=",")]
            vetor = divide_vetores(vetor, vetor2)
            print(vetor)
        elif command == "multiplicacao_escalar":
            escalar = int(input())
            vetor = multiplicacao_escalar(vetor, escalar)
            print(vetor)
        elif command == "n_duplicacao":
            escalar = int(input())
            vetor = n_duplicacao(vetor, escalar)
            print(vetor)
        elif command == "soma_elementos":
            vetor = [soma_elementos(vetor)]
            print(vetor)
        elif command == "produto_interno":
            vetor2 = [int(entry2) for entry2 in input().split(sep=",")]
            vetor = [produto_interno(vetor, vetor2)]
            print(vetor)
        elif command == "multiplica_todos":
            vetor2 = [int(entry2) for entry2 in input().split(sep=",")]
            vetor = multiplica_todos(vetor, vetor2)
            print(vetor)
        elif command == "correlacao_cruzada":
            mascara = [int(entry2) for entry2 in input().split(sep=",")]
            vetor = correlacao_cruzada(vetor, mascara)
            print(vetor)
        elif command == "fim":
            break


if __name__ == '__main__':
    main()
