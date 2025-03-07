def func_1():
    input()
    trump = input()
    trumps = []
    answers = []
    suits = {'C': None, 'D': None, 'H': None, 'S': None}
    for card in input().split():
        (rank, suit) = card
        if suit == trump:
            trumps.append(rank)
        elif suits[suit] is not None:
            answers.append(' '.join([x + suit for x in sorted([suits[suit], rank])]))
            suits[suit] = None
        else:
            suits[suit] = rank
    for (suit, rank) in suits.items():
        if rank is None:
            continue
        if trumps != []:
            answers.append(f'{rank}{suit} {trumps.pop()}{trump}')
        else:
            print('IMPOSSIBLE')
            return
    trumps = sorted(trumps)
    while trumps != []:
        print(f'{trumps.pop()}{trump} {trumps.pop()}{trump}')
    for answer in answers:
        print(answer)
for _ in range(int(input())):
    func_1()