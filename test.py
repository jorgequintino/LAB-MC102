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