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

pile_list = ["KP", "QP", "10E", "6E", "4C", "2C"]
pile_str = ""
for card_pile in pile_list:
    pile_str += " " + card_pile
print("Pilha:", sep='')