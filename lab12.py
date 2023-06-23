class Player:
    def __init__(self, hand):
        self._hand = hand

    def set_hand(self):
        pass

    def cards_value(self):
        pass

    def discard_cards(self):
        pass

    def play():
        pass

    @property
    def hand(self):
        return self._hand

    @hand.setter
    def hand(self, hand):
        self._hand = hand

class Card:
    def __init__(self, hand) -> None:
        self._hand = hand

        pass

    def set_cards_value(self, hand):
        set = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
        suit = ["O", "E", "C", "P"]
        hand_value = []
        for index1, i in enumerate(set):
            value = 0
            for card in hand:
                if i != "10":
                    if card[:1] == i:
                        if index1 == 0:
                            value = 0
                        else:
                            value = 2 * (index1 + 1)
                        for index2, k in enumerate(suit):
                            value += index2
                            hand_value.append(value)
                else:
                    if card[:2] == i:
                        if index1 == 0:
                            value = 0
                        else:
                            value = 2 * (index1 + 1)
                        for index2, k in enumerate(suit):
                            value += index2
                            hand_value.append(value)
        return hand_value

    def place_cards_in_line():
        pass

    @property
    def hand(self):
        return self._hand

    @hand.setter
    def hand(self, hand):
        self._hand = hand

def main():
    player_numb = int(input())
    players = []  # [hand0, hand1, hand2, ...]
    for _ in range(player_numb):
        hand_str = input()
        hand = []  # [car0, card1, car2, ...]
        i = 0
        while i < len(hand_str):
            if hand_str[i: i + 2] == "10":
                hand.append(hand_str[i: i + 3])
                i += 5
            else:
                hand.append(hand_str[i: i + 2])
                i += 4
        players.append(Player(hand, ))
    dare_plays = int(input())
    