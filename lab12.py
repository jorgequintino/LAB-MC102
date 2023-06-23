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

    def binary_search(self, card):
        if card == self.hand[len(self.hand // 2)]:
            return len(self.hand) // 2
        elif card < self.hand[len(self.hand // 2)]:
            return self.binary_search(self.hand[:len(self.hand // 2)])
        else:
            return self.binary_search(self.hand[len(self.hand) // 2:])
        
    def stamp_hand(self):
        pass

    @property
    def hand(self):
        return self._hand

    @hand.setter
    def hand(self, hand):
        self._hand = hand

class Pile:
    def __init__(self, card):
        self._card = card

    def add_pile():
        #  pegar as cartas descartadas dos players 
        #  
        pass

    def clean_pile():
        pass

    def stamp_pile():
        pass

    @property
    def card(self):
        return self._card

    @card.setter
    def card(self, card):
        self._card = card

class Cards:
    def __init__(self, cards):
        pass

    def something_card_in_hand():
        pass

    def set_cards_value(self):
        set = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
        suit = ["O", "E", "C", "P"]
        hand_value = []
        for card in self.hand:
            for index1, i in enumerate(set):
                value = 0
                if i != "10":
                    if card[:1] == i:
                        value = 4 * index1
                        for index2, k in enumerate(suit):
                            if card[1:2] == k:
                                value += index2
                                hand_value.append(value)
                else:
                    if card[:2] == i:
                        value = 4 * index1
                        for index2, k in enumerate(suit):
                            if card[2:3] == k:
                                value += index2
                                hand_value.append(value)
        return hand_value

    def sort_cards(self, hand_value):
        for i in range(len(hand_value) - 1):
            smallest = i
            for k in range(i, len(hand_value)):
                if hand_value[smallest] > hand_value[k]:
                    smallest = k
            hand_value[i], hand_value[smallest] = hand_value[smallest], hand_value[i]
        return hand_value

    def stamp_cards(self):
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

def main():
    player_numb = int(input())
    players = []  # [hand0, hand1, hand2, ...]
    for _ in range(player_numb):
        hand_str = input()
        hand = []  # [card0, card1, car2, ...]
        i = 0
        while i < len(hand_str):
            if hand_str[i: i + 2] == "10":
                hand.append(hand_str[i: i + 3])
                i += 5
            else:
                hand.append(hand_str[i: i + 2])
                i += 4
        #  talvez usar a classe cards para fazer funcionar melhor na hora de add na lista de players
        cards = Cards.set_cards_value(hand)
        cards = Cards.sort_cards(hand)
        players.append(Player(cards))

    dare_plays = int(input())


if __name__ == "__main__":
    main()
