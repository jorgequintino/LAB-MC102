# Cleaning Room Robot From Smaug


def search(room, robot_position, room_numb):
    scanning = [(0, -1), (-1, 0), (0, +1), (+1, 0)]
    for position in scanning:
        dirty = robot_position + position
        if dirty[1] >= 0 and dirty[1] < len(room[0]):
            if dirty[0] >= 0 and dirty[0] < room_numb:
                if room[dirty[0]][dirty[1]] == "o":
                    return dirty, robot_position
    return None, None

# def jasj():
#     point = search(room, robot_position, room_numb)
#     if search(room, robot_position, room_numb) == none:
#         scanner(room, robot_position)
#     elif search(room, robot_position, room_numb) != none:
#         cleaning(point)

#     #back_sc = robot_position

#     if dirt != []:
#         cleaning() #dirt[0]
#         search()


        
# salvar a posição da sujeira e mandar ele ir atras
def cleaning(robot_position, room, dirty, room_numb):
    room[dirty[0]][dirty[1]] = "r"
    room[robot_position[0]][robot_position[1]] = "."


def back_scanner(dirty, last_position, room, room_numb):
    x = dirty[1] - last_position[1]
    y = dirty[0] - last_position[0]
    if dirty[1] < last_position[1]:
        for i in range((-1)*x):
            walking_right(room, last_position)

    elif dirty[1] > last_position[1]:
        for _ in range(x):
            walking_left(room, last_position)
    
        if dirty[0] > last_position[0]:
            for _ in range(y):
                walking_up()
        
        elif dirty[0] > last_position[0]:
            for _ in range(y):
                walking_down(room, last_position)
    # voltar para posição antes do cleaning
    pass


def finish_cleaning(room, room_numb, robot_position):
    if room_numb % 2 == 0:
        pos = robot_position
        for _ in range(len(room[0]) - 1):
            room[pos[0]][pos[1] + 1] = "r"
            room[pos[0]][pos[1]] = "."
            pos = (pos[0], pos[1] + 1)
            stamp(room)


def stamp(room):
    for i in range(len(room[0])):
        print(*room[i])
    print()


def walking_right(room, robot_position):
    room[robot_position[0]][robot_position[1] + 1] = "r"
    room[robot_position[0]][robot_position[1]] = "."


def walking_up(room, robot_position):
    room[robot_position[0] - 1][robot_position[1]] = "r"
    room[robot_position[0]][robot_position[1]] = "."


def walking_left(room, robot_position):
    room[robot_position[0]][robot_position[1] - 1] = "r"
    room[robot_position[0]][robot_position[1]] = "."


def walking_down(room, robot_position):
    room[robot_position[0] + 1][robot_position[1]] = "r"
    room[robot_position[0]][robot_position[1]] = "."


def scanner(room, robot_position):
    if robot_position[0] % 2 == 0:
        if (robot_position[1] + 1) < len(room[0]):
            walking_right(room, robot_position)
            robot_position = location(robot_position, 0, 1)
        else:
            walking_down(room, robot_position)
            robot_position = location(robot_position, 1, 0)
    elif robot_position[0] % 2 != 0:
        if (robot_position[1] - 1) >= 0:
            walking_left(room, robot_position)
            robot_position = location(robot_position, 0, -1)
        else:
            walking_down(room, robot_position)
            robot_position = location(robot_position, +1, 0)
    return room, robot_position


def location(robot_position, a, b):
    return (robot_position[0] + a, robot_position[1] + b)

# last

def main ():
    room_numb = int(input())
    # line > 0
    room = []
    for _ in range(room_numb):
        room.append(input().split())
    robot_position = (0, 0)
    stamp(room)

    while True:
        dirty, last_position = search(room, robot_position, room_numb)
        # dirty_position = [] # problema
        # dirty_position.append(dirty)
        if dirty is not None:
            #for dirty in dirty_position: while, break se dirty is none
                cleaning(robot_position, room, dirty, room_numb)
                # fazer um loop aqui que vai meter um search and cleaning eterno
                search()
                if l == "chamar sujeira":
                    cleaning()
                    search()
                elif l == "clean":
                    back_scanner(dirty, last_position, room, room_numb)
        scanner(room, last_position)
        stamp(room)
        # finish_cleaning()
        # criar condicionais para chamar essa função

    # for _ in range(len(room[0])*room_numb - 1):
    #     room, robot_position = scanner(room, robot_position)
    #     stamp(room)
    # finish_cleaning(room, room_numb, robot_position)


if __name__ == "__main__":
    main()

# salvar a posição que tem sujeira
# mover até ela pela ordem que ele anda
# separar em diferentes funções de movimento
# TESTING 