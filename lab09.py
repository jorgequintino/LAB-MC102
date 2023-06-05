# Cleaning Room Robot From Smaug


def location(robot_position, line, column):
    '''Altera a localização do robô.
    Parâmetros:
    argumentos:
        robot_position (tuple)
        line (int)
        column (int)
    retorno:
        robot_position (tuple)
        '''
    return (robot_position[0] + line, robot_position[1] + column)


def walking_right(room, robot_position):
    '''Movimenta o robô de acordo com a função que a chamou e
    retorna sua nova posição.
    Parâmetros:
    argumentos:
        room (list)
        robot_position (tuple)
    retorno:
        robot_position (tuple)
        '''
    room[robot_position[0]][robot_position[1] + 1] = "r"
    room[robot_position[0]][robot_position[1]] = "."
    return location(robot_position, 0, 1)


def walking_up(room, robot_position):
    '''Movimenta o robô de acordo com a função que a chamou e
    retorna sua nova posição.
    Parâmetros:
    argumentos:
        room (list)
        robot_position (tuple)
    retorno:
        robot_position (tuple)
        '''
    room[robot_position[0] - 1][robot_position[1]] = "r"
    room[robot_position[0]][robot_position[1]] = "."
    return location(robot_position, -1, 0)


def walking_left(room, robot_position):
    '''Movimenta o robô de acordo com a função que a chamou e
    retorna sua nova posição.
    Parâmetros:
    argumentos:
        room (list)
        robot_position (tuple)
    retorno:
        robot_position (tuple)
        '''
    room[robot_position[0]][robot_position[1] - 1] = "r"
    room[robot_position[0]][robot_position[1]] = "."
    return location(robot_position, 0, -1)


def walking_down(room, robot_position):
    '''Movimenta o robô de acordo com a função que a chamou e
    retorna sua nova posição.
    Parâmetros:
    argumentos:
        room (list)
        robot_position (tuple)
    retorno:
        robot_position (tuple)
        '''
    room[robot_position[0] + 1][robot_position[1]] = "r"
    room[robot_position[0]][robot_position[1]] = "."
    return location(robot_position, 1, 0)


def scanner(room, robot_position, room_numb):
    '''Movimenta o robô de acordo  com os limites da matriz. Isto é,
    caso esteja em linha par, só pode mover para direita e para baixo,
    este se a primeira opção for inviável. Caso esteja em linha ímpar,
    só pode mover para esquerda e para baixo, este se a primeira opção
    for inviável. Caso não seja possível mover, sinaliza o fim do
    escaneamento.
    Parâmetros:
    argumentos:
        room (list)
        robot_position (tuple)
        room_numb (int)
    retorno:
        room (list)
        robot_position (tuple)
        finish_scanning (bool)
        '''
    finish_scanning = False
    if robot_position[0] % 2 == 0:
        if (robot_position[1] + 1) < len(room[0]):
            robot_position = walking_right(room, robot_position)
        elif (robot_position[1]) == len(room[0]) - 1 and robot_position[0] != room_numb - 1:
            robot_position = walking_down(room, robot_position)
        else:
            finish_scanning = True
    elif robot_position[0] % 2 != 0:
        if (robot_position[1] - 1) >= 0:
            robot_position = walking_left(room, robot_position)
        elif (robot_position[1]) == 0 and robot_position[0] != room_numb - 1:
            robot_position = walking_down(room, robot_position)
        else:
            finish_scanning = True
    return room, robot_position, finish_scanning


def search(room, robot_position, room_numb):
    '''Procura sujeira nos perímetros da posição do robô. Caso não há
    sujeira ao redor, retorna "None".
    Parâmetros:
    argumentos:
        room (list)
        robot_position (tuple)
        room_numb (int)
    retorno:
        dirty (tuple | None)
        robot_position (tuple)
    '''
    scanning = [(0, -1), (-1, 0), (0, +1), (+1, 0)]
    for position in scanning:
        dirty = (robot_position[0] + position[0], robot_position[1] + position[1])
        if dirty[1] >= 0 and dirty[1] < len(room[0]):
            if dirty[0] >= 0 and dirty[0] < room_numb:
                if room[dirty[0]][dirty[1]] == "o":
                    return dirty, robot_position
    return None, robot_position


def cleaning(robot_position, room, dirty):
    '''Limpa a posição em que foi detectada sujeira. Retorna após a nova
    posição do robô na sala.
    Parâmetros:
    argumentos:
        robot_position (tuple)
        room (list)
        dirty (tuple)
    retorno:
        robot_position (tuple)
    '''
    room[dirty[0]][dirty[1]] = "r"
    room[robot_position[0]][robot_position[1]] = "."
    return location(dirty, 0, 0)


def back_scanner(last_scanned_position, room, robot_position):
    '''Movimenta o robô de acordo  com os limites da matriz de volta para
    a útima posição em que fez escaneamento. Primeira, é preciso igual a
    coluna da localização do robô com a da última posição escaneada. Por
    fim, move-se na direção dessa coluna até chegar na linha correta.
    Parâmetros:
    argumentos:
        last_position (tuple)
        room (list)
        robot_position (tuple)
    retorno:
        robot_position (tuple)
        '''
    if robot_position[1] != last_scanned_position[1]:
        if robot_position[1] < last_scanned_position[1]:
            robot_position = walking_right(room, robot_position)
        elif robot_position[1] > last_scanned_position[1]:
            robot_position = walking_left(room, robot_position)
    elif robot_position[1] == last_scanned_position[1]:
        if robot_position[0] > last_scanned_position[0]:
            robot_position = walking_up(room, robot_position)
        elif robot_position[0] > last_scanned_position[0]:
            robot_position = walking_down(room, robot_position)
    return robot_position


def check_scanner(room, robot_position, room_numb):
    '''Busca qual seria a próxima posição no "escanesmento regular"
    de uma determinada localização.
    Parâmetros:
    argumentos:
        room (list)
        robot_position (tuple)
        room_numb (int)
    retorno:
        robot_position (tuple)
        '''
    if robot_position[0] % 2 == 0:
        if (robot_position[1] + 1) < len(room[0]):
            return (robot_position[0], robot_position[1] + 1)
        elif (robot_position[1]) == len(room[0]) - 1 and robot_position[0] != room_numb - 1:
            return (robot_position[0] + 1, robot_position[1])
    elif robot_position[0] % 2 != 0:
        if (robot_position[1] - 1) >= 0:
            return (robot_position[0], robot_position[1] - 1)
        elif (robot_position[1]) == 0 and robot_position[0] != room_numb - 1:
            return (robot_position[0] + 1, robot_position[1])


def check_last_position(last_position, room, robot_position, room_numb):
    '''Verifica se determinada posição seria a próxima escaneada pelo
    robô baseada na sua posição anterior.
    Parâmetros:
    argumentos:
        las_position (tuple)
        room (list)
        robot_position (tuple)
        room_numb (int)
    retorno:
        boolean
        '''
    position = check_scanner(room, last_position, room_numb)
    if robot_position == position:
        return False
    else:
        return True


def finish_cleaning(room, room_numb, robot_position):
    '''Para as matrizes de quantidade de linhas pares, move o robô
    ao longo da última linha a fim de deixá-lo na posição do canto
    inferior direito, o que marca o fim do escaneamento.
    Parâmetros:
    argumentos:
        room (list)
        room_numb (int)
        robot_position (tuple)
    retorno
        None
        '''
    if room_numb % 2 == 0:
        for _ in range(len(room[0]) - 1):
            robot_position = walking_right(room, robot_position)
            stamp(room)


def stamp(room):
    '''Prepara a impressão da estrutura da sala.
    Parâmetros:
    argumentos:
        room (list)
    retorno:
        None'''
    for i in range(len(room)):
        print(*room[i])
    print()


def main():
    room_numb = int(input())
    room = []
    for _ in range(room_numb):
        room.append(input().split())
    robot_position = (0, 0)
    last_scanned_position = (0, 0)
    scanning_mode = False
    cleaning_mode = False
    stamp(room)
    while True:
        dirty, initial_position = search(room, robot_position, room_numb)
        if dirty is not None:  # se há sujeira, verifica se está na estrutura de escaneamento ou não.
            cleaning_mode = check_last_position(initial_position, room, dirty, room_numb)
        if cleaning_mode is not True:  # Caso não esteja no modo limpeza, ativa-se o modo escaneamento.
            scanning_mode = True
        if scanning_mode is True:  # No modo escaneamento, salva a última posição escaneada.
            last_scanned_position = initial_position
        while dirty is not None and cleaning_mode:
            scanning_mode = False
            robot_position = cleaning(robot_position, room, dirty)
            stamp(room)
            dirty, robot_position = search(room, dirty, room_numb)
        while dirty is None and last_scanned_position != robot_position and cleaning_mode is True:
            robot_position = back_scanner(last_scanned_position, room, robot_position)
            stamp(room)
            dirty, robot_position = search(room, robot_position, room_numb)
            if last_scanned_position == robot_position:
                scanning_mode = True
        if scanning_mode is True:
            room, robot_position, finish_scanning = scanner(room, robot_position, room_numb)
            if finish_scanning is True:
                break
            stamp(room)
    finish_cleaning(room, room_numb, robot_position)


if __name__ == "__main__":
    main()
