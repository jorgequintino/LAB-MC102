class Player:
    def __init__(self, hand):
        self._hand = hand

    def discard_cards(self):
        #  remove said card out of his hand
        #  probably a hand.remove()
        pass

    def play():
        #  
        pass
    
    def doubt(self, doubted, dare_plays):
        if doubted == dare_plays:

        pass

    def binary_search(self, card):
        # e quando ele não tem a carta?
        if card == self.hand[len(self.hand // 2)]:
            return len(self.hand) // 2
        elif card < self.hand[len(self.hand // 2)]:
            return self.binary_search(self.hand[:len(self.hand // 2)])
        else:
            return self.binary_search(self.hand[len(self.hand) // 2:])
        
    def sort_hand(self, hand_value):
        for i in range(len(hand_value) - 1):
            smallest = i
            for k in range(i, len(hand_value)):
                if hand_value[smallest] > hand_value[k]:
                    smallest = k
            hand_value[i], hand_value[smallest] = hand_value[smallest], hand_value[i]
        return hand_value[:-1]

    def stamp_hand(self):
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

        # print()
        return hand_print

    @property
    def hand(self):
        return self._hand

    @hand.setter
    def hand(self, hand):
        self._hand = hand

class Pile:
    def __init__(self, pile_list):
        self._card = pile_list

    def add_pile(self, card):
        self.pile_list = self.pile_list.append(card)
        return self.pile_list

    def clean_pile(self):
        self.pile_list = self.pile_list.remove()
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
    def pile(self):
        return self.pile

    @pile.setter
    def pile(self, pile):
        self._pile = pile

class Card:
    def __init__(self, card, value):
        self._card = card
        self._card_value = value

    def set_card_value(self, card):
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

    @property
    def card(self):
        return self._card

    @card.setter
    def card(self, card):
        self._card = card

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value

def main():
    player_numb = int(input())
    players = []  # [hand0, hand1, hand2, ...]
    for _ in range(player_numb):
        hand_str = input().split(', ')
        hand = []  # [card0, card1, car2, ...]
        for i in range(len(hand_str)):
            card_str, card_value = Card.set_card_value(hand_str[i])
            card = Card(card_str, card_value)
            hand.append(card)
        player = Player(hand)
        players.append(player.sort_hand(hand))
    dare_plays = int(input())
    
    pile = Pile([])


if __name__ == "__main__":
    main()
