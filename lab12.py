class Player:
    def __init__(self, hand):
        self._hand = hand

    def set_hand(self):
        pass

    def pile():
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

class Card(Player):
    def __init__(self, hand):
        super().__init__(hand)

    def set_cards_value(self, hand):
        set = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
        suit = ["O", "E", "C", "P"]
        hand_value = []
        hand_print = {}
        for card in hand:
            # criar dicionário cuja chave é o valor usado no código para poder imprimir as cartas pela escrita normal.
            value = 0
            for index1, i in enumerate(set):
                if i != "10":
                    if card[:1] == i:
                        if index1 == 0:
                            value = 0
                        else:
                            value = 2 * (index1 + 1)
                        for index2, k in enumerate(suit):
                            if card[1:2] == k:
                                value += index2
                                hand_value.append(value)
                                hand_print[value] = i + k
                else:
                    if card[:2] == i:
                        if index1 == 0:
                            value = 0
                        else:
                            value = 2 * (index1 + 1)
                        for index2, k in enumerate(suit):
                            if card[2:3] == k:
                                value += index2
                                hand_value.append(value)
                                hand_print[value] = i + k
        return hand_value, hand_print

    def sort_hand(self, hand_value):
        for i in range(len(hand_value) - 1):
            smallest = i
            for k in range(i, len(hand_value)):
                if hand_value[smallest] > hand_value[k]:
                    smallest = k
            hand_value[i], hand_value[smallest] = hand_value[smallest], hand_value[i]
        return hand_value

    def binary_search(self, card):
        if card == self.hand[len(self.hand // 2)]:
            return len(self.hand) // 2
        elif card < self.hand[len(self.hand // 2)]:
            return self.binary_search(self.hand[:len(self.hand // 2)])
        else:
            return self.binary_search(self.hand[len(self.hand) // 2:])

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
        players.append(Player(hand, ))
    dare_plays = int(input())


if __name__ == "__main__":
    main()
