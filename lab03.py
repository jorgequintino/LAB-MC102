# Jogo do bolo ou cerveja intergaláctica:

# Quantidade de jogadores.
player_numb = int(input())

# Números da caixa mágica para cada jogador.
box01_numb = input().split()
box01_numb_int = []
for i in box01_numb:
    box01_numb_int.append(int(i))

# Separação dos números da segunda caixa entre os limites esquerdo e limites direito de cada jogador.
box02_numb = input().split()
left_numb_int = []
right_numb_int = []
for i in range(len(box02_numb)) :
    if i % 2 == 0:
        left_numb_int.append(int(box02_numb[i]))
    else:
        right_numb_int.append(int(box02_numb[i]))

# Atribuição de pontuação para cada jogador.
player_points = []
for i in range(len(box01_numb)) :
    if i < ((player_numb - 1) // 2 + 1):
        player_points.append((right_numb_int[i] - left_numb_int[i])*box01_numb_int[i])
    else:
        player_points.append((right_numb_int[i] - left_numb_int[i]) + box01_numb_int[i])

# Busca do maior valor atrbuído e da possibilidade de empate.
i = 0
maximo = 0
empate = False
while i < player_numb:
    if player_points[i] > maximo:
        maximo = player_points[i]
        status = i + 1
        if i >= (status-1):
            empate = False
    elif player_points[i] == maximo:
        empate = True  
    i += 1

# Resultado da partida.
if empate == True :
    print("Rodada de cerveja para todos os jogadores!")
elif empate == False:
    print("O jogador número", status ,"vai receber o melhor bolo da cidade pois venceu com", maximo ,"ponto(s)!")