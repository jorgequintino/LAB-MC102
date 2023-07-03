# Estrutura do jogo 'Duvido, ou Mentira'

class Player:
    '''Classe para separ os jogadores.
    '''
    def __init__(self, hand, numb, sorted_hand):
        self._hand = hand
        self._numb = numb
        self._sorted_hand = sorted_hand

    def discard_cards(self, pile, bluff, left_limit, right_limit):
        ''' Função em que se executa o descarte das cartas, mediante o cenário
        de vlefe ou não. Em caso de blefe, ela descarta as últimas cartas da
        mão do jogador de mesmo poder.
        Parâmetros:
        argumentos:
            self (class)
            pile (class)
            index (int)
            bluff (bool)
            left_limit (int)
            right_limit (int)
        retorno:
            None
            '''
        if not bluff:
            pile.pile_list.extend(self.sorted_hand[left_limit: right_limit + 1:][::-1])
            if self.sorted_hand[left_limit].power > pile.last_card.power:
                pile.last_card = self.sorted_hand[left_limit]
            print("[Jogador ", self._numb, "] ", len(self.sorted_hand[left_limit: right_limit + 1]), " carta(s) ", pile.last_card.power_str, sep='')
            self.sorted_hand = self.sorted_hand[:left_limit] + self.sorted_hand[right_limit + 1:]
        else:
            self.discard_last_card(pile)

    def discard_last_card(self, pile):
        ''' Função em que se executa o descarte das últimas cartas da
        mão do jogador de mesmo poder.
        Parâmetros:
        argumentos:
            self (class)
            pile (class)
        retorno:
            None
            '''
        bluff, left_limit, right_limit = self.binary_search(self.sorted_hand[len(self.sorted_hand) - 1])
        self.discard_cards(pile, bluff, left_limit, right_limit)

    def doubt(self, pile, player, bluff, set_card):
        ''' Função que executa aas consequencias do blefe para o jogador que
        perdeu.
        Parâmetros:
        argumentos:
            self (class)
            pile (class)
            player (class)
            bluff (bool)
            set_card (class)
        retorno:
            None
            '''
        if bluff:
            self.sorted_hand.extend(pile.pile_list)
            self.sorted_hand = sort_hand(self.sorted_hand)
            pile.clean_pile(set_card)
        else:
            player.doubt(pile, player, True, set_card)

    def binary_search(self, card):
        ''' Função em que se executa a busca por cartas de mesmo poder. Na impossibilidade
        de encontra, retornar a maior que está mais proxima ou quando não há.
        Parâmetros:
        argumentos:
            self (class)
            class (class)
        retorno:
            middle (int)
            bluff (bool)
            left_limit (int)
            right_limit (int)
            '''
        bluff = True
        beginning = 0
        end = len(self.sorted_hand) - 1
        closest_card = -1
        right_limit = -1
        left_limit = -1
        while beginning <= end:
            middle = (beginning + end) // 2
            if self.sorted_hand[middle].power == card.power:
                bluff = False
                for i in range(middle, len(self.sorted_hand)):
                    if self.sorted_hand[i].power == card.power:
                        right_limit = i
                for k in range(0, middle + 1):
                    if self.sorted_hand[k].power == card.power:
                        left_limit = k
                        break
                return bluff, left_limit, right_limit

            elif self.sorted_hand[middle].power > card.power:
                if middle > closest_card:
                    closest_card = middle
                    for i in range(middle, len(self.sorted_hand)):
                        if self.sorted_hand[i].power == self.sorted_hand[closest_card].power:
                            right_limit = i
                    for k in range(0, middle + 1):
                        if self.sorted_hand[k].power == self.sorted_hand[closest_card].power:
                            left_limit = k
                            break
                beginning = middle + 1
                bluff = False

            else:
                end = middle - 1

        return bluff, left_limit, right_limit

    def stamp_hand(self):
        ''' Função que printa a mão do jogador.
        Parâmetros:
        argumentos:
            self (class)
        retorno:
            None
            '''
        print("Jogador ", self.numb, sep='')
        hand_cards = ""
        for i in range(len(self.sorted_hand)):
            hand_cards += " " + self.sorted_hand[i].name
        print("Mão:", hand_cards, sep='')

    @property
    def hand(self):
        return self._hand

    @hand.setter
    def hand(self, hand):
        self._hand = hand

    @property
    def numb(self):
        return self._numb

    @property
    def sorted_hand(self):
        return self._sorted_hand

    @sorted_hand.setter
    def sorted_hand(self, sorted_hand):
        self._sorted_hand = sorted_hand

class Pile:
    ''' Classe refente a pilha de descarte
    '''
    def __init__(self, pile_list, last_card):
        self._pile_list = pile_list
        self._last_card = last_card

    def clean_pile(self, set_card):
        ''' Função que limpa a pilha. Isto é, reseta para uma lista limpa e
        e a última carta dela padrão.
        Parâmetros:
        argumentos:
            self (class)
            set_card (class)
        retorno:
            None
            '''
        self.pile_list.clear()
        self.last_card = set_card

    def stamp_pile(self):
        ''' Função para printar a pilha de descartes.
        Parâmetros:
        argumentos:
            self (class)
        retorno:
            None
            '''
        if self.pile_list == []:
            print("Pilha:", sep='')
        else:
            pile_str = ""
            for card_pile in self.pile_list:
                pile_str += " " + card_pile.name
            print("Pilha:", pile_str, sep='')

    @property
    def last_card(self):
        return self._last_card

    @last_card.setter
    def last_card(self, last_card):
        self._last_card = last_card

    @property
    def pile_list(self):
        return self._pile_list

    @pile_list.setter
    def pile_list(self, pile_list):
        self._pile_pile = pile_list

class Card:
    ''' Classe referente às cartas.
    '''
    def __init__(self, name, value, power, power_str):
        self._name = name
        self._value = value
        self._power = power
        self._power_str = power_str

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value

    @property
    def power(self):
        return self._power

    @power.setter
    def power(self, power):
        self._power = power

    @property
    def power_str(self):
        return self._power_str

    @power_str.setter
    def power_str(self, power_str):
        self._power_str = power_str

def set_card_value(card):
    ''' Função que atribui valores para numéricos para as cartas a fim de
    transformar a execução do código em apenas inteiros.
        Parâmetros:
        argumentos:
            card (class)
        retorno:
            None
            '''
    set = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    suit = ["O", "E", "C", "P"]
    for index1, i in enumerate(set):
        value = 0
        if i != "10":
            if card[:1] == i:
                value = 4 * index1
                power = index1 + 1
                power_str = card[:1]
                for index2, k in enumerate(suit):
                    if card[1:2] == k:
                        value += index2
                        return card, value, power, power_str
        else:
            if card[:2] == i:
                value = 4 * index1
                power = index1 + 1
                power_str = card[:2]
                for index2, k in enumerate(suit):
                    if card[2:3] == k:
                        value += index2
                        return card, value, power, power_str

def sort_hand(hand_value):
    ''' Função que organiza a mão em uma relação decrescente do poder das cartas.
    Isso é feito ao trocar as artas de lugar entre maior e menor, e a inversão no
    retorno da lista.
        Parâmetros:
        argumentos:
            hand_value (list)
        retorno:
            None
            '''
    for i in range(len(hand_value)):
        smallest = i
        for k in range(i, len(hand_value)):
            if hand_value[smallest].value > hand_value[k].value:
                smallest = k
        hand_value[i], hand_value[smallest] = hand_value[smallest], hand_value[i]
    return hand_value[::-1]

def main():
    player_numb = int(input())
    players = []  # [hand0, hand1, hand2, ...]
    for numb in range(player_numb):
        hand_str = input().split(', ')
        hand = []  # [card0, card1, car2, ...]
        for i in range(len(hand_str)):
            card_str, card_value, card_power, card_power_str = set_card_value(hand_str[i])
            card = Card(card_str, card_value, card_power, card_power_str)
            hand.append(card)
        sorted_hand = sort_hand(hand)
        player = Player(hand, numb + 1, sorted_hand)
        players.append(player)
    dare_plays = int(input())
    set_card = Card("aa", 60, -1, "a")
    pile = Pile([], set_card)

    game = True
    plays = 0
    while game:
        for p in range(len(players)):
            players[p].stamp_hand()
        pile.stamp_pile()

        first = True

        i = 0
        while i >= 0:

            if i - 1 < 0:
                last_player = player_numb - 1
            else:
                last_player = i - 1

            if first:
                bluff, left_limit, right_limit = players[i].binary_search(players[i].sorted_hand[len(players[i].sorted_hand) - 1])
                players[i].discard_cards(pile, bluff, left_limit, right_limit)
                pile.stamp_pile()
                plays += 1

            if not first:
                if plays == dare_plays:
                    plays = 0
                    print("Jogador ", i + 1, " duvidou.", sep='')
                    players[last_player].doubt(pile, players[i], bluff, set_card)

                    for p in range(len(players)):
                        players[p].stamp_hand()
                    pile.stamp_pile()

                if not players[last_player].sorted_hand:
                    print("Jogador ", last_player + 1, " é o vencedor!", sep='')
                    game = False
                    break

                bluff, left_limit, right_limit = players[i].binary_search(pile.last_card)
                players[i].discard_cards(pile, bluff, left_limit, right_limit)
                pile.stamp_pile()
                plays += 1

            first = False

            i += 1
            if i >= player_numb:
                i = 0

if __name__ == "__main__":
    main()
