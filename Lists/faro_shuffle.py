cards = input().split()
shuffle = int(input())

length = len(cards)
mid = int(length / 2)

for i in range(0, shuffle):
    list1 = []
    for p in range(0, mid):
        list1.append(cards[p])
        list1.append(cards[mid])
        mid += 1
    cards = list1
    mid = int(length / 2)

print(list1)
