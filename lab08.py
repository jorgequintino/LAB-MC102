# Prêmio Abacaxi de Ouro


def victory(award, movies, category):
    '''
    A função "victory" retorna o vencedor da categoria sendo apresentada.
    Caso a média seja superior a pontuação, o filme é o vencedor, não há empate.
    Caso seja igual, ocorre empate e há uma lista com os nomes dos filmes
    empatados para analisar a maior quantidade de avaliadores.
    
    Parâmetros:
    argumentos:
        award (dict) = dict com dados de categoria, filme, média, e quantidade de avaliadores.
                award = {categoria : {filme avaliado : [pontos, quant. avaliadores]}}
        movies (dict) = dict com dados de quantidade de prêmios, média total, quantidade de avaliadores.
                {nome: [qtd premios, S média, qtd de avaliação]}
        category (str) = categoria
    Retorno:
        winner (str) = filme vencedor da categoria
    '''
    point_winner = 0
    draw = False
    movies_winning = []
    for movies_name in award[category].keys():
        if award[category][movies_name][0] > point_winner:
            draw = False
            point_winner = award[category][movies_name][0]
            winner = movies_name
            movies_winning.clear()
            movies_winning.append(movies_name)
        elif award[category][movies_name][0] == point_winner:
            draw = True
            movies_winning.append(movies_name)
    if draw is True:
        valuers = 0
        for movies_name in movies_winning:
            if award[category][movies_name][1] > valuers:
                winner = movies_name
                valuers = award[category][movies_name][1]
    movies[winner][0] += 1
    return winner


def worst_movie(movies):
    '''
    A função "shouldnt_be_here" retorna o filme vencedor da categoria especial
    "não merecia estar aqui". Caso a quantidade de prêmios seja superior a
    estabelecida, o filme é o vencedor, não há empate. Caso seja igual, ocorre
    empate e há uma lista com os nomes dos filmes empatados para analisar a
    maior média.

    Parâmetros:
    argumentos:
        movies (dict) = dict com dados de quantidade de prêmios, média total, quantidade de avaliadores.
                {nome: [qtd premios, S média, qtd de avaliação]}
    Retorno:
        winner (str) = filme vencedor categoria
    '''
    amount_award = 0
    movies_winning = []
    draw = False
    for movies_name in movies.keys():
        if movies[movies_name][0] > amount_award:
            amount_award = movies[movies_name][0]
            draw = False
            winner = movies_name
            movies_winning.clear()
            movies_winning.append(movies_name)
        elif movies[movies_name][0] == amount_award:
            draw = True
            movies_winning.append(movies_name)
    if draw is True:
        add = 0
        for movies_name in movies_winning:
            if movies[movies_name][1] > add:
                winner = movies_name
                add = movies[movies_name][1]
    return winner


def shouldnt_be_here(movies):
    '''
    A função "worst_movie" retorna o filme vencedor da categoria especial
    "pior filme do anor". Para cada filme com quantidade de prẽmios simples
    igual a zero, ele é um vencedor da categoria.

    Parâmetros:
    argumentos:
        movies (dict) = dict com dados de quantidade de prêmios, média total, quantidade de avaliadores.
                {nome: [qtd premios, S média, qtd de avaliação]}
    Retorno:
        winner (str) = filme vencedor categoria
    '''
    movies_winning = []
    for movies_name in movies.keys():
        if movies[movies_name][2] == 0:
            movies_winning.append(movies_name)
    if movies_winning == []:
        winner = "sem ganhadores"
    else:
        winner = ""
        for movies_name in movies_winning:
            winner += movies_name + ", "
        winner = winner[:-2]
    return winner


def victory_in_category(category, movies, award):
    '''
    A função "victory_in_category" reescreve os valores contidos no dicionário
    dentro do dicionário "award". Ela também distribue a média de cada film
    nas categoria para a média geral do filme ea qauntidade de avaliadores total.

    Parâmetros:
    argumentos:
        award (dict) = dict com dados de categoria, filme, média, e quantidade de avaliadores.
                award = {categoria : {filme avaliado : [pontos, quant. avaliadores]}}
        movies (dict) = dict com dados de quantidade de prêmios, média total, quantidade de avaliadores.
                {nome: [qtd premios, S média, qtd de avaliação]}
        category (str) = categoria
    Retorno:
        winner (str) = filme vencedor da categoria
    '''
    for movies_name in award[category].keys():
        points = (sum(award[category][movies_name]) / len(award[category][movies_name]))
        movies[movies_name][1] += points
        movies[movies_name][2] += (len(award[category][movies_name]))
        award[category][movies_name] = [points, len(award[category][movies_name])]
        # award = {category : {filme avaliado : [pontos, quant. avaliadores]}}
    winner = victory(award, movies, category)
    return winner


def main ():
    amount_movies = int(input())
    movies = {}
    for _ in range(amount_movies):
        movies_name = input()
        # movies = {nome: [qtd premios, S média, qtd de avaliação]}
        movies[movies_name] = [0, 0, 0]
    amount_category = int(input())
    award = {}
    award["filme que causou mais bocejos"] = {}
    award["filme que foi mais pausado"] = {}
    award["filme que mais revirou olhos"] = {}
    award["filme que não gerou discussão nas redes sociais"] = {}
    award["enredo mais sem noção"] = {}
    # award = {category : {filme avaliado : [ponto1, ponto2 (...)]}}
    for _ in range(amount_category):
        valuer, category, movie_valued, score = input().split(sep=", ")
        if movie_valued not in award[category].keys():
            award[category][movie_valued] = [int(score)]
        else:
            award[category][movie_valued].append(int(score))
    print("#### abacaxi de ouro ####\n\ncategorias simples")
    for category in award.keys():
        print("categoria:", category)
        print("-", victory_in_category(category, movies, award))
    print("\ncategorias especiais\nprêmio pior filme do ano\n-", worst_movie(movies))
    print("prêmio não merecia estar aqui\n-", shouldnt_be_here(movies))


if __name__ == "__main__":
    main()
