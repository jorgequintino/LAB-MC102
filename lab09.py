# Cleaning Room Robot From Smaug


def scanner(room, robot):
    # controlar as paredes, tipo (-1,0)
    if room[robot[0] - 1][robot[1]] != "o":
        if room[robot[0]][robot[1] - 1] != "o":
            if room[robot[0] + 1][robot[1]] != "o":
                if room[robot[0] - 1][robot[1]] != "o":
                    x = walking # # salvar a posição que tem sujeira
                elif room[robot[0] - 1][robot[1]] == "o":
                    x = cleaning
            elif room[robot[0] + 1][robot[1]] == "o":
                x = cleaning
        elif room[robot[0]][robot[1] - 1] == "o":
            x = cleaning
    elif room[robot[0] - 1][robot[1]] == "o":
        x = cleaning
    return x

# salvar a posição da sujeira e mandar ele ir atras
def cleaning():
    pass


def back_scanner():
    pass


def finish_cleaning(room, room_numb, robot):
    if robot == (room_numb - 1, len(room[room_numb - 1])):
        return stamp


def stamp(room):
    return print(room)


def walking(room, robot):
    if robot[0] % 2 == 0:
        if (robot[1] + 1) < len(room[0]):
            room[robot[0]][robot[1] + 1] = "r"
            room[robot[0]][robot[1]] = "."
            # mudar a localizaçã do robo .
        else:
            room[robot[0] + 1][robot[1]] = "r"
            room[robot[0]][robot[1]] = "."
    else:
        if (robot[1] - 1) < 0:
            room[robot[1] - 1] = "r"
            robot[1] = "."
        else:
            room[robot[0] + 1] = "r"
            robot[0] = "."
    return room


def location(room, robot):
    # na posição em ue moveu-se o r,
    # está a localização do robot 
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
