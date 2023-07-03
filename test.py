# hand_str = input()
# hand = []
# i = 0
# while i < len(hand_str):
#     if hand_str[i: i + 2] == "10":
#         hand.append(hand_str[i: i + 3])
#         i += 5
#     else:
#         hand.append(hand_str[i: i + 2])
#         i += 4
# print(hand)


# d = input().split(', ')
# print(d)
# # y = d.split(', ')
# # print(y)

# pile_list = ["KP", "QP", "10E", "6E", "4C", "2C"]
# pile_str = ""
# # for card_pile in pile_list:
# #     pile_str += " " + card_pile
# # print("Pilha:", sep='')
# f = 0 // 4
# d = 1 // 4
# z = 4 // 4
# g = 5 // 4
# h = 7 // 4
# k = 8 // 4
# print(f, d, z, g, h, k)

# cards_discarded = []
#             # procurar outras cartas daquele valor (resto  divisão inteirapor 4)
#             last_card = self.sorted_hand[len(self.sorted_hand) - 1]
#             cards_discarded.append(last_card)
#             search = []
#             for possible_card in self.sorted_hand:
#                 if (possible_card // 4) == (last_card // 4):
#                     search.append(possible_card)
#             for k in range(len(search)):
#                 index = self.binary_search(k)
#                 if index != -1:
#                     amount_cards_discarded.append(index)
#             for m in amount_cards_discarded:
#                 pile.pile_list.append(m)
#             # descartar todas essas cartas


# cards_discarded = []
#         # procurar outras cartas daquele valor (resto  divisão inteira por 4)
#         last_card = self.sorted_hand[len(self.sorted_hand) - 1]
#         cards_discarded.append(last_card)
#         # adaptar para o power
#         for card in self.sorted_hand:
#             if (card // 4) == (last_card // 4):
#                 cards_discarded.append(last_card)
#         for card_discarded in cards_discarded:
#             pile.pile_list.append(card_discarded)
#             pile.last_card = card_discarded
#             self.sorted_hand.remove(card_discarded)
#             # descartar todas essas cartas

d = "kfekfkdkflkjfdh"
print(d[2:5])

d = 0 % 3
f = 1 % 3
g = 2 % 3
print(d, f, g)