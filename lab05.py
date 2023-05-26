#Relação de árvore filogenética

def reverter(i,j,genome):
    '''Inverte a ordem de uma sequência de letras do genoma.'''
    return genome[:i] + genome[i:j+1][::-1] + genome[j+1:]

def transpor(i,j,k,genome):
    '''Troca de lugar dois grupos de letras do genoma.'''
    return genome[:i] + genome[j+1:k+1] + genome[i:j+1] + genome[k+1:]

def combinar(g,i,genome):
    '''Adiciona novo grupo de letras ao genoma.'''
    return genome[:i] + g + genome[i:]

def concatenar(g,genome):
    '''Adiciona, no final do genoma, novo grupo de letras.'''
    return genome + g

def remover(i,j,genome):
    '''Remove do genoma uma sequência de letras.'''
    return genome[:i] + genome[j+1:]

def transpor_e_reverter(i,j,k,genome):
    '''Primeiro executa a transposição de dois grupos de letras e depois inverte a ordem do resultado da transposição.'''
    genome = transpor(i, j, k, genome)
    genome = reverter(i, k, genome)
    return genome

def buscar(g,genome):
    '''Mostra quantas vezes uma sequência de letras aparece no genoma.'''
    print(genome.count(g))

def buscar_bidirecional(g,genome):
    '''Mostra a quantidade de vezes que uma sequência de letras aparece no genoma e no seu inverso.'''
    print(genome.count(g) + genome[::-1].count(g))

def mostrar(genome):
    '''Mostra o genoma.'''
    print(genome)

genome = input()
while True:
    act = input().split()
    if act[0] == "reverter":
        i = int(act[1])
        j = int(act[2])
        genome = reverter(i,j,genome)
    elif act[0] == "transpor":
        i = int(act[1])
        j = int(act[2])
        k = int(act[3])
        genome = transpor(i,j,k,genome)
    elif act[0] == "combinar":
        i = int(act[2])
        g = act[1]
        genome = combinar(g,i,genome)
    elif act[0] == "concatenar":
        g = act[1]
        genome = concatenar(g,genome)
    elif act[0] == "remover":
        i = int(act[1])
        j = int(act[2])
        genome = remover(i,j,genome)
    elif act[0] == "transpor_e_reverter":
        i = int(act[1])
        j = int(act[2])
        k = int(act[3])
        genome = transpor_e_reverter(i,j,k,genome)
    elif act[0] == "buscar":
        g = act[1]
        buscar(g,genome)
    elif act[0] == "buscar_bidirecional":
        g = act[1]
        buscar_bidirecional(g,genome)
    elif act[0] == "mostrar":
        mostrar(genome)
    elif act[0] == "sair":
        break