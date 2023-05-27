# Cleaning Room Robot From Smaug


<<<<<<< HEAD
def scanner(room, robot_position):
    if robot_position[0] % 0:
        if robot_position[0] == 0: # primeira linha
            if robot_position[1] == 0:
                if room[robot_position[0]][robot_position[1] + 1] != "o":
                    if room[robot_position[0] + 1][robot_position[1]] == "o":
                        dirty = (robot_position[0] + 1, robot_position[1])
                elif room[robot_position[0]][robot_position[1] + 1] == "o":
                    dirty = (robot_position[0], robot_position[1] + 1)
            elif robot_position[1] == len(room[0]) - 1:
                if room[robot_position[0] - 1][robot_position[1]] != "o":
                    if room[robot_position[0] + 1][robot_position[1]] == "o":
                        dirty = (robot_position[0] + 1, robot_position[1])
            else:
                if room[robot_position[0]][robot_position[1] - 1] != "o":
                    if room[robot_position[0]][robot_position[1] + 1] != "o":
                        if room[robot_position[0] - 1][robot_position[1]] == "o":
                            dirty = (robot_position[0] - 1, robot_position[1])
                    elif room[robot_position[0]][robot_position[1] + 1] == "o":
                        dirty = (robot_position[0], robot_position[1] + 1)
                elif room[robot_position[0]][robot_position[1] - 1] != "o":
                    dirty = (robot_position[0], robot_position[1] - 1)

        if robot_position[0] == len(room[0]) - 1: #ultima linha
            if robot_position[1] == 0:
                if room[robot_position[0]][robot_position[1] + 1] != "o":
                    if room[robot_position[0] + 1][robot_position[1]] == "o":
                        dirty = (robot_position[0] + 1, robot_position[1])
                elif room[robot_position[0]][robot_position[1] + 1] == "o":
                    dirty = (robot_position[0], robot_position[1] + 1)
            elif robot_position[1] == len(room[0]) - 1:
                if room[robot_position[0] - 1][robot_position[1]] != "o":
                    if room[robot_position[0] + 1][robot_position[1]] == "o":
                        dirty = (robot_position[0] + 1, robot_position[1])
            else:
                if room[robot_position[0]][robot_position[1] - 1] != "o":
                    if room[robot_position[0]][robot_position[1] + 1] != "o":
                        if room[robot_position[0] - 1][robot_position[1]] == "o":
                            dirty = (robot_position[0] - 1, robot_position[1])
                    elif room[robot_position[0]][robot_position[1] + 1] == "o":
                        dirty = (robot_position[0], robot_position[1] + 1)
                elif room[robot_position[0]][robot_position[1] - 1] != "o":
                    dirty = (robot_position[0], robot_position[1] - 1)

# linhas do meio

    return dirty
                    




# esq if room[robot_position[0]][robot_position[1] - 1] != "o":
# cima if room[robot_position[0] - 1][robot_position[1]] != "o":
# dir if room[robot_position[0]][robot_position[1] + 1] != "o":
# baixo if room[robot_position[0] + 1][robot_position[1]] != "o":
=======
def scanner(room, robot_position, room_numb):
    if robot_position[0] == 0:
        if robot_position[1] == 0:
            if room[robot[0] + 1][robot[1]] != "o":
                if room[robot[0] - 1][robot[1]] != "o":
                    x = walking # # salvar a posição que tem sujeira
                elif room[robot[0] - 1][robot[1]] == "o":
                    x = cleaning
            elif room[robot[0] + 1][robot[1]] == "o":
                x = cleaning
        elif robot_position[1] == len(room[0]) - 1:
            if room[robot[0] - 1][robot[1]] != "o":

        else:
            comando
    elif robot_position[0] == room_numb - 1:
        if robot_position[1] == 0:
            comando
        elif robot_position[1] == len(room[0]) - 1:
            comando
        else:
            comando
    while robot_position[0] > 0 and robot_position < room_numb - 1:
        if robot_position[1] == 1 :
            comando
        elif robot_position[1] == len(room[0]) - 1:
            
        else:
            if room[robot_position[0] - 1][robot_position[1]] != "o":
                if room[robot[0]][robot[1] - 1] != "o":
                    if room[robot[0] + 1][robot[1]] != "o":
                        if room[robot[0] - 1][robot[1]] != "o":
                            x = walking # # salvar a posição que tem sujeira
                        elif room[robot[0] - 1][robot[1]] == "o":
                            x = cleaning


# dependendo da linha, o movimento do robô muda
>>>>>>> b3e1f4e (k)

    # controlar as paredes, tipo (-1,0)
    if room[robot_position[0] - 1][robot_position[1]] != "o":
        if room[robot_position[0]][robot_position[1] - 1] != "o":
            if room[robot_position[0] + 1][robot_position[1]] != "o":
                if room[robot_position[0] - 1][robot_position[1]] != "o":
                    x = walking # # salvar a posição que tem sujeira
                elif room[robot_position[0] - 1][robot_position[1]] == "o":
                    x = cleaning
            elif room[robot_position[0] + 1][robot_position[1]] == "o":
                x = cleaning
        elif room[robot_position[0]][robot_position[1] - 1] == "o":
            x = cleaning
    elif room[robot_position[0] - 1][robot_position[1]] == "o":
        x = cleaning
    return x

# salvar a posição da sujeira e mandar ele ir atras
def cleaning():
    pass


def back_scanner():
    pass


def finish_cleaning(room, room_numb, robot_position):
    if robot_position == (room_numb - 1, len(room[room_numb - 1])):
        return stamp



def stamp(room):
    return print(room)


def walking_left():
    pass


def walking_up():
    pass


def walking_right():
    pass


def walking_low():
    pass


def walking(room, robot_position):
    if robot_position[0] % 2 == 0:
        if (robot_position[1] + 1) < len(room[0]):
            room[robot_position[0]][robot_position[1] + 1] = "r"
            room[robot_position[0]][robot_position[1]] = "."
            # mudar a localizaçã do robo .
        else:
            room[robot_position[0] + 1][robot_position[1]] = "r"
            room[robot_position[0]][robot_position[1]] = "."
    else:
        if (robot_position[1] - 1) < 0:
            room[robot_position[1] - 1] = "r"
            robot_position[1] = "."
        else:
            room[robot_position[0] + 1] = "r"
            robot_position[0] = "."
    return room


def location(room, robot_position):
    # na posição em ue moveu-se o r,
    # está a localização do robot_position 
    pass


def main ():
    room_numb = int(input())
    #line > 0
    room = []
    for _ in range(room_numb):
        room.append(input().split())
    print(room)
    robot_position = (0, 0)
    # salvar última posição do robô antes de entrar no modo limpeza
    #

# salvar a posição que tem sujeira
# mover até ela pela ordem que ele anda
# separar em diferentes funções de movimento
# TESTING 