l = [7, 2, 1, 4]
for i in range(len(l) - 1):
    k = 0
    trocou = False
    for j in range(len(l) - 1, i, -1):
        if l[j-1] > l[j]:
            l[j-1], l[j] = l[j], l[j-1]
            trocou = True
            k += 1
    if not trocou:
        print(k)
        break