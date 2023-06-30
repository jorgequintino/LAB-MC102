class Player:
    def __init__(self, hand, numb, sorted_hand):
        self._hand = hand
        self._numb = numb
        self._sorted_hand = sorted_hand

    def discard_last_card(self, pile):
        cards_discarded = []
        # procurar outras cartas daquele valor (resto  divisão inteirapor 4)
        last_card = self.sorted_hand[len(self.sorted_hand) - 1]
        cards_discarded.append(last_card)
        for card in self.sorted_hand:
            if (card // 4) == (last_card // 4):
                cards_discarded.append(last_card)
        for card_discarded in cards_discarded:
            pile.pile_list.append(card_discarded)
            pile.last_card = card_discarded
            self.sorted_hand.remove(card_discarded)
            # descartar todas essas cartas

    def discard_cards(self, pile):
        if pile.pile_list != []:
            # revisar o binary
            if self.binary_search(pile.last_card) != -1:
                cards_checked = []
                # card_checked_index = []
                for card in self.sorted_hand:
                    if (card // 4) == (pile.last_card // 4):
                        cards_checked.append(card)
                    # verificar s e da problema fazer em um loop só
                for card_checked in cards_checked:
                    pile.pile_list.append(card_checked)
                    pile.last_card = card_checked
                    self.sorted_hand.remove(card_checked)
                
            else:
                self.discard_last_card()
        else:
            self.discard_last_card()
        return 1  # usar como contador

    def doubt(self, doubted, dare_plays, pile, player):
        if pile.last_card // 4 >= x:  # descobrir x
            player.numb
            pass

    def binary_search(self, card):
        beginning = 0
        end = len(self.sorted_hand) - 1
        while beginning <= end:
            middle = (beginning + end) // 2
            if self.sorted_hand[middle].card_value == card:
                return middle
            elif self.sorted_hand[middle].card_value > card:
                beginning = middle + 1
            else:
                end = middle - 1
        return -1

    def stamp_hand(self, hand):
        set = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
        suit = ["O", "E", "C", "P"]
        hand_print = {}

        for index1, i in enumerate(set):
            value = 0
            if i != "10":
                value = 4 * index1
                for index2, k in enumerate(suit):
                    value += index2
                    hand_print[value] = i + k
            else:
                value = 4 * index1
                for index2, k in enumerate(suit):
                    value += index2
                    hand_print[value] = i + k

        print("Jogador ", self.numb, sep='')
        hand_cards = ""
        for i in hand_print:
            # se a chave é igual ao valor da carta na mão
            hand_cards += " " + hand_print[i]
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
        self.sorted_hand = sorted_hand

class Pile:
    def __init__(self, pile_list, last_card, sorted_pile):
        self._pile_list = pile_list
        self._last_card = last_card
        self._sorted_pile = sorted_pile

    def add_pile(self, card):
        self.pile_list.append(card)
        return self.pile_list

    def clean_pile(self):
        # reset last card
        self.pile_list = []
        return self.pile_list

    def stamp_pile(self):
        if self.pile_list == []:
            print("Pilha:", sep='')
        else:
            pile_str = ""
            for card_pile in self.pile_list:
                pile_str += " " + card_pile
            print("Pilha:", pile_str, sep='')

    @property
    def pile_list(self):
        return self._pile_list

    @pile_list.setter
    def pile(self, pile):
        self._pile = pile

class Card:
    def __init__(self, card, value):
        self._card = card
        self._card_value = value

    # def __str__(self):
    #     return str(self.card)

    @property
    def card(self):
        return self._card

    @card.setter
    def card(self, card):
        self._card = card

    @property
    def card_value(self):
        return self._card_value

    @card_value.setter
    def card_value(self, value):
        self._card_value = value

def set_card_value(card):
    set = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    suit = ["O", "E", "C", "P"]
    for index1, i in enumerate(set):
        value = 0
        if i != "10":
            if card[:1] == i:
                value = 4 * index1
                for index2, k in enumerate(suit):
                    if card[1:2] == k:
                        value += index2
                        return card, value
        else:
            if card[:2] == i:
                value = 4 * index1
                for index2, k in enumerate(suit):
                    if card[2:3] == k:
                        value += index2
                        return card, value

def sort_hand(hand_value):
    for i in range(len(hand_value)):
        smallest = i
        for k in range(i, len(hand_value)):
            if hand_value[smallest].card_value > hand_value[k].card_value:
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
            card_str, card_value = set_card_value(hand_str[i])
            card = Card(card_str, card_value)
            hand.append(card)
        sorted_hand = sort_hand(hand)
        player = Player(hand, numb + 1, sorted_hand)
        players.append(player)
    dare_plays = int(input())

    doubted = 0
    pile = Pile([], -1, [])
    doubted += player.discard_cards(pile)

if __name__ == "__main__":
    main()
