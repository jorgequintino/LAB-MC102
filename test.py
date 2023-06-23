hand_str = input()
hand = []
i = 0
while i < len(hand_str):
    if hand_str[i: i + 2] == "10":
        hand.append(hand_str[i: i + 3])
        i += 5
    else:
        hand.append(hand_str[i: i + 2])
        i += 4
print(hand)