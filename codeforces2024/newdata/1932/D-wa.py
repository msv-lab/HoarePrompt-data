def createSortedSuitPile(cardPile):
    s, c, d, h = [], [], [], []
    for card in cardPile:
        if card[1] == "S":
            s.append(card)
        elif card[1] == "C": c.append(card)
        elif card[1] == "D": d.append(card)
        elif card[1] == "H": h.append(card)
    s.sort(key = lambda x : int(x[0]))
    c.sort(key = lambda x : int(x[0]))
    d.sort(key = lambda x : int(x[0]))
    h.sort(key = lambda x : int(x[0]))
    # print(f's = {s}')
    # print(f'c = {c}')
    # print(f'd = {d}')
    # print(f'h = {h}')
    return s, c, d, h

def findTrumpCardPile(trump, s, c, d, h):
    if trump == "S": return s
    elif trump ==  "C": return c
    elif trump ==  "D": return d
    elif trump ==  "H": return h

def solveSuit(suit, trump, i):
    l = 0
    r = len(suit) - 1
    res = []
    flag = True
    while l < r:
        res.append((suit[r], suit[l]))
        l += 1
        r -= 1
    
    # In this case, we need to solve by taking a trump card
    if l == r and i < len(trump):
        res.append((trump[i], suit[l]))
        i += 1
    elif i >= len(trump):
        flag = False
    
    return res, i, flag

def createResPile(s, c, d, h, trump, n):
    res = []
    # Solve Suit wise
    # Solving S suit
    remaining = []
    if trump == "S":
        trumpSuit = s
        remaining.append(c)
        remaining.append(d)
        remaining.append(h)
    elif trump == "C":
        remaining = [s, d, h]
        trumpSuit = c
    elif trump == "D":
        remaining = [c, s, h]
        trumpSuit = d
    elif trump == "H":
        remaining = [c, d, s]
        trumpSuit = h
    
    i = 0
    # print(f'remaining = {remaining}')
    for suit in remaining:
        # print(f'suit = {suit}')
        resSuit, i, flag = solveSuit(suit, trumpSuit, i)
        # print(f'resSuir = {resSuit}, i = {i}, res = {res}')
        if not flag: return res, False
        for pair in resSuit:
            res.append(pair)
    
    if i < len(trumpSuit):
        resSuit, i, flag = solveSuit(trumpSuit[i:], trumpSuit, i)
        for pair in resSuit:
            res.append(pair)

    return res, True

for _ in range(int(input())):
    n = int(input())
    trump = input()
    cardPile = list(map(str, input().split(' ')))

    s, c, d, h = createSortedSuitPile(cardPile)

    cnt = n//2
    res, flag = createResPile(s, c, d, h, trump, n)
    if not flag:
        print("IMPOSSIBLE")
    else:
        for pair in res:
            c1, c2 = pair
            print(c2, c1)