# Cleaning Room Robot From Smaug


def location(robot_position, a, b):
    return (robot_position[0] + a, robot_position[1] + b)


def walking_right(room, robot_position):
    room[robot_position[0]][robot_position[1] + 1] = "r"
    room[robot_position[0]][robot_position[1]] = "."
    return location(robot_position, 0, 1)


def walking_up(room, robot_position):
    room[robot_position[0] - 1][robot_position[1]] = "r"
    room[robot_position[0]][robot_position[1]] = "."
    return location(robot_position, -1, 0)


def walking_left(room, robot_position):
    room[robot_position[0]][robot_position[1] - 1] = "r"
    room[robot_position[0]][robot_position[1]] = "."
    return location(robot_position, 0, -1)


def walking_down(room, robot_position):
    room[robot_position[0] + 1][robot_position[1]] = "r"
    room[robot_position[0]][robot_position[1]] = "."
    return location(robot_position, 1, 0)


def scanner(room, robot_position, room_numb):
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

    scanning = [(0, -1), (-1, 0), (0, +1), (+1, 0)]
    for position in scanning:
        dirty = (robot_position[0] + position[0], robot_position[1] + position[1])
        if dirty[1] >= 0 and dirty[1] < len(room[0]):
            if dirty[0] >= 0 and dirty[0] < room_numb:
                # stamp(room)
                if room[dirty[0]][dirty[1]] == "o":
                    return dirty, robot_position
    return None, robot_position


def cleaning(robot_position, room, dirty): 
    room[dirty[0]][dirty[1]] = "r"
    room[robot_position[0]][robot_position[1]] = "."
    return location(dirty, 0, 0)


def back_scanner(last_position, room, robot_position):
    if robot_position[1] != last_position[1]:
        if robot_position[1] < last_position[1]:
            robot_position = walking_right(room, robot_position)
        elif robot_position[1] > last_position[1]:
            robot_position = walking_left(room, robot_position)
    elif robot_position[1] == last_position[1]:
        if robot_position[0] > last_position[0]:
            robot_position = walking_up(room, robot_position)
        elif robot_position[0] > last_position[0]:
            robot_position = walking_down(room, robot_position)
    return robot_position
    # voltar para posição antes do cleaning


def check_scanner(room, robot_position, room_numb):
    if robot_position[0] % 2 == 0:
        if (robot_position[1] + 1) < len(room[0]):
            return (robot_position[0], robot_position[1] + 1)
        elif (robot_position[1]) == len(room[0]) - 1 and robot_position[0] != room_numb - 1:
            return (robot_position[0] + 1, robot_position[1])
            # robot_position = walking_down(room, robot_position)
    elif robot_position[0] % 2 != 0:
        if (robot_position[1] - 1) >= 0:
            return (robot_position[0], robot_position[1] - 1)
            # robot_position = walking_left(room, robot_position)
        elif (robot_position[1]) == 0 and robot_position[0] != room_numb - 1:
            return (robot_position[0] + 1, robot_position[1])
            # robot_position = walking_down(room, robot_position)


def check_last_position(last_position, room, robot_position, room_numb):
    position = check_scanner(room, last_position, room_numb)
    # arrumar as funções de qalking
    if robot_position == position:
        return False
    elif robot_position != position:
        return True


def finish_cleaning(room, room_numb, robot_position):
    if room_numb % 2 == 0:
        for _ in range(len(room[0]) - 1):
            robot_position = walking_right(room, robot_position)
            stamp(room)


def stamp(room):
    for i in range(len(room)):
        print(*room[i])
    print()


def main():
    room_numb = int(input())
    room = []
    for _ in range(room_numb):
        room.append(input().split())
    robot_position = (0, 0)
    stamp(room)
    
    while True:
        cleaning_mode = False
        dirty, last_position = search(room, robot_position, room_numb)
        # print("cansei")
        while dirty is not None:
            # print(dirty)
            cleaning_mode = True
            robot_position = cleaning(robot_position, room, dirty)
            dirty, robot_position = search(room, dirty, room_numb)
            stamp(room)
            cleaning_mode = check_last_position(last_position, room, robot_position, room_numb)
        while dirty is None and last_position != robot_position and cleaning_mode is True:
            # print("dirty is none")
            robot_position = back_scanner(last_position, room, robot_position)
            dirty, robot_position = search(room, robot_position, room_numb)
            stamp(room)
        if cleaning_mode is False:
            room, robot_position, finish_scanning = scanner(room, robot_position, room_numb)
            if finish_scanning is True:
                break
            stamp(room)

    finish_cleaning(room, room_numb, robot_position)


if __name__ == "__main__":
    main()
