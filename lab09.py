# Cleaning Room Robot From Smaug


def location(robot_position, a, b):
    return (robot_position[0] + a, robot_position[1] + b)


def walking_right(room, robot_position):
    room[robot_position[0]][robot_position[1] + 1] = "r"
    room[robot_position[0]][robot_position[1]] = "."
    robot_position = location(robot_position, 0, 1)


def walking_up(room, robot_position):
    room[robot_position[0] - 1][robot_position[1]] = "r"
    room[robot_position[0]][robot_position[1]] = "."
    robot_position = location(robot_position, -1, 0)


def walking_left(room, robot_position):
    room[robot_position[0]][robot_position[1] - 1] = "r"
    room[robot_position[0]][robot_position[1]] = "."
    robot_position = location(robot_position, 0, -1)


def walking_down(room, robot_position):
    room[robot_position[0] + 1][robot_position[1]] = "r"
    room[robot_position[0]][robot_position[1]] = "."
    robot_position = location(robot_position, 1, 0)


def scanner(room, robot_position):
    if robot_position[0] % 2 == 0:
        try:
            if (robot_position[1] + 1) < len(room[0]):
                walking_right(room, robot_position)
            else:
                walking_down(room, robot_position)
        except IndexError:
            return None, robot_position
    elif robot_position[0] % 2 != 0:
        try:
            if (robot_position[1] - 1) >= 0:
                walking_left(room, robot_position)
            else:
                walking_down(room, robot_position)
        except IndexError:
            return None, robot_position
    return room, robot_position


def search(room, robot_position, room_numb):
    scanning = [(0, -1), (-1, 0), (0, +1), (+1, 0)]
    for position in scanning:
        dirty = robot_position + position
        if dirty[1] >= 0 and dirty[1] < len(room[0]):
            if dirty[0] >= 0 and dirty[0] < room_numb:
                if room[dirty[0]][dirty[1]] == "o":
                    return dirty, robot_position
    return None, robot_position


def cleaning(robot_position, room, dirty, room_numb):  # salvar a posição da sujeira e mandar ele ir atras
    room[dirty[0]][dirty[1]] = "r"
    room[robot_position[0]][robot_position[1]] = "."
    robot_position = location(dirty, 0, 0)


def back_scanner(dirty, last_position, room, room_numb):
    if dirty[1] != last_position[1]:
        if dirty[1] < last_position[1]:
            walking_right(room, last_position)
        elif dirty[1] > last_position[1]:
            walking_left(room, last_position)
    elif dirty[1] == last_position[1]:
        if dirty[0] > last_position[0]:
            walking_up(room, last_position)
        elif dirty[0] > last_position[0]:
            walking_down(room, last_position)
    # voltar para posição antes do cleaning


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


def main():
    room_numb = int(input())
    room = []
    for _ in range(room_numb):
        room.append(input().split())
    robot_position = (0, 0)
    stamp(room)

    while True:  # maybe figure out a better condition
        dirty, last_position = search(room, robot_position, room_numb)
        # dirty_position = [] # problema
        # dirty_position.append(dirty)
        if dirty is not None:
            cleaning(robot_position, room, dirty, room_numb)
            dirti, posi = search(room, dirty, room_numb)
            # fazer um loop aqui que vai meter um search and cleaning eterno
            # vai dar problema com dirty
            while dirti is not None:
                cleaning(posi, room, dirti, room_numb)
                dirti, posi = search(room, dirti, room_numb)
            while dirti is None:
                back_scanner(posi, last_position, room, room_numb)
                dirti, posi = search(room, posi, room_numb)  # this dirty / posi
        room, robot_position = scanner(room, last_position)
        if room is None:
            break
        stamp(room)

    finish_cleaning(room, room_numb, robot_position)


if __name__ == "__main__":
    main()
