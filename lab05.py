#Relação de árvore filogenética

def reverter(i,j,genoma):
    '''Inverte a ordem de uma sequência de letras do genoma.'''
    return genoma[:i] + genoma[i:j+1][::-1] + genoma[j+1:]

def transpor(i,j,k,genoma):
    '''Troca de lugar dois grupos de letras do genoma.'''
    return genoma[:i] + genoma[j+1:k+1] + genoma[i:j+1] + genoma[k+1:]

def combinar(g,i,genoma):
    '''Adiciona novo grupo de letras ao genoma.'''
    return genoma[:i] + g + genoma[i:]

def concatenar(g,genoma):
    '''Adiciona, no final do genoma, novo grupo de letras.'''
    return genoma + g

def remover(i,j,genoma):
    '''Remove do genoma uma sequencia de letras.'''
    return genoma[:i] + genoma[j+1:]

def transpor_e_reverter(i,j,k,genoma):
    '''Primeiro executa a transposição de dois rupos de letras e depois inverte a ordem do resultado da transposição.'''
    genoma = transpor(i, j, k, genoma)
    genoma = reverter(i, k, genoma)
    return genoma

def buscar(g,genoma):
    '''Conta quantas vezes uma sequência de letras aparece no genoma.'''
    return genoma.count(g)

def buscar_bidirecional(g,genoma):
    '''Soma a quantidade de vezes que uma sequẽncia de letras aparece no genoma e no seu inverso.'''
    return genoma.count(g) + genoma[::-1].count(g)

def mostrar(genoma):
    '''Mostra o genoma.'''
    print(genoma)

genoma = input()
while True:
    comando = input().split()
    if comando[0] == "reverter":
        i = int(comando[1])
        j = int(comando[2])
        genoma = reverter(i,j,genoma)
    elif comando[0] == "transpor":
        i = int(comando[1])
        j = int(comando[2])
        k = int(comando[3])
        genoma = transpor(i,j,k,genoma)
    elif comando[0] == "combinar":
        i = int(comando[2])
        g = comando[1]
        genoma = combinar(g,i,genoma)
    elif comando[0] == "concatenar":
        g = comando[1]
        genoma = concatenar(g,genoma)
    elif comando[0] == "remover":
        i = int(comando[1])
        j = int(comando[2])
        genoma = remover(i,j,genoma)
    elif comando[0] == "transpor_e_reverter":
        i = int(comando[1])
        j = int(comando[2])
        k = int(comando[3])
        genoma = transpor_e_reverter(i,j,k,genoma)
    elif comando[0] == "buscar":
        g = comando[1]
        print(buscar(g,genoma))
    elif comando[0] == "buscar_bidirecional":
        g = comando[1]
        print(buscar_bidirecional(g,genoma))
    elif comando[0] == "mostrar":
        mostrar(genoma)
    elif comando[0] == "sair":
        break