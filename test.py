<<<<<<< HEAD
<<<<<<< HEAD
# def vence(kae, movies):
#     point_winner = 0
#     empate = False
#     dit = []
#     for movies_name in kae:
#         if kae[movies_name][0] > point_winner:
#             empate = False
#             point_winner = kae[movies_name][0]
#             winner = movies_name
#             movies[movies_name][0] += 1

#         if kae[movies_name][0] == point_winner:
#             empate = True
#             dit.append(movies_name)
#     if empate is True:
#         aval = 0
#         for i in dit:
#             if kae[movies_name][1] > aval:
#                 winner = movies_name
#             if not kae[movies_name][1] > aval:
#                 aval = kae[movies_name]
#     return winner



#     # if empate == True:
#     #     aval = []
#     #     x = []
#     #     for movies_name in kae:
#     #         if kae[movies_name][0] == point_winner:
#     #             aval.append(kae[movies_name][1])
#     #             x.append(movies_name)
#     #     max_aval = max(aval)
#     #     for i in range(len(aval)):
#     #         if aval[i] == max_aval:
#     #             winner = x[i]
#     return winner


# def category(category, movies, D, movies_name):
#     kae = {}
#     for movies_name in D[category].keys():
#         points = int(sum(D[category][movies_name]) / len(D[category][movies_name]))
#         movies[movies_name][1] += points
#         kae[movies_name] = [points, int(len(D[category]))]
#         #kae[movies_name][points] = int(len(D[category])[movies_name])
#     return vence(filme, points, qtd_av, movies, movies_name)


# def main ():
#     f = int(input())
#     movies = {}
#     for _ in range(f):
#         movies_name = input()
#         # movies= {nome: [qtd premios, S média]}
#         movies[movies_name] = [0, 0]
#     Q = int(input())
#     D = {}
#     D["filme que causou mais bocejos"] = {}
#     D["filme que foi mais pausado"] = {}
#     D["filme que mais revirou olhos"] = {}
#     D["filme que não gerou discussão nas redes sociais"] = {}
#     D["enredo mais sem noção"] = {}
#     # {category : {filme avaliado : [ponto1, ponto2 (...)]}}
#     for _ in range(Q):
#         valuer, category, movie_valued, score = input().split(sep=", ")
#         if movie_valued not in D[category].keys():
#             D[category][movie_valued] = [int(score)]
#         else:
#             D[category][movie_valued].append(int(score))
    

# if __name__ == "__main__":
#     main()

# win = ["titanic", "avenger", "starwars"]
# print("\n\nhsddja")

# f = int(input())
# movies = {}
# for _ in range(f):
#     movies_name = input()
#     # movies= {nome: [qtd premios, S média, qtd de avaliação]}
#     movies[movies_name] = [0, 0, 0]
# Q = int(input())
# D = {}
# D["filme que causou mais bocejos"] = {}
# D["filme que foi mais pausado"] = {}
# D["filme que mais revirou olhos"] = {}
# D["filme que não gerou discussão nas redes sociais"] = {}
# D["enredo mais sem noção"] = {}
# # {category : {filme avaliado : [ponto1, ponto2 (...)]}}
# #D[category].keys()
# for _ in range(Q):
#     valuer, category, movie_valued, score = input().split(sep=", ")
#     if movie_valued not in D[category].keys():
#         D[category][movie_valued] = [int(score)]
#     else:
#         D[category][movie_valued].append(int(score))
# print(D)

# D = {"valor" : [0, 2]}
# D["valor"] = [1, 3]
# print(D)

# d = ["kfsd", "cmk"]
# #d.append("key")
# str(d)
# print(d)

d = ["ds", "2" , "3"]
x = ""
for i in d:
    x += i + ", "
x = x[:-2]
print(x)
=======
=======
def walking_left(room, robot_position):
    room[robot_position[0]][robot_position[1] + 1] = "r"
    room[robot_position[0]][robot_position[1]] = "."


def walking_up():
    pass


def walking_right(room, robot_position):
    room[robot_position[0]][robot_position[1] - 1] = "r"
    room[robot_position[0]][robot_position[1]] = "."


def walking_low(room, robot_position):
    room[robot_position[0] + 1][robot_position[1]] = "r"
    room[robot_position[0]][robot_position[1]] = "."


def location(robot_position, a, b):
    robot_position = (robot_position[0] + a, robot_position[1] + b)
    return robot_position

def stamp(room):
    for i in range(len(room[0])):
        print(*room[i])
    print()


>>>>>>> 8022e0b (dsvs)
def walking(room, robot_position):
    if robot_position[0] % 2 == 0:
        if (robot_position[1] + 1) < len(room[0]):
            walking_left(room, robot_position)
            robot_position = location(robot_position, 0, 1)
            # mudar a localização do robo .
        else:
            walking_low(room, robot_position)
            robot_position = location(robot_position, 1, 0)
    elif robot_position[0] % 2 != 0:
        if (robot_position[1] - 1) >= 0:
            walking_right(room, robot_position)
            robot_position = location(robot_position, 0, -1)
        else:
            walking_low(room, robot_position)
            robot_position = location(robot_position, +1, 0)
    return room, robot_position


def finish_cleaning(room, room_numb, robot_position):
    if room_numb % 2 == 0:
        pos = robot_position
        for _ in range(len(room[0]) - 1):
            room[pos[0]][pos[1] + 1] = "r"
            room[pos[0]][pos[1]] = "."
            pos = (pos[0], pos[1] + 1)
            stamp(room)


def main():
    room_numb = int(input())
    #line > 0
    room = []
    for _ in range(room_numb):
        room.append(input().split())
    stamp(room)
    #print()
    robot_position = (0, 0)
    # for _ in range(len(room[0])*room_numb - 1):
    #     room, robot_position = walking(room, robot_position)
    #     stamp(room)
    # finish_cleaning(room, room_numb, robot_position)
    while True:
        search()

if __name__ == "__main__":
    main()
>>>>>>> bf87f75 (hfg)
