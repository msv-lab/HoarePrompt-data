#State of the program right berfore the function call: t is an integer such that 1 <= t <= 100. For each test case, n is an integer such that 1 <= n <= 16. The trump suit is a single character from the set {'C', 'D', 'H', 'S'}. The description of 2n cards is a list of 2n distinct two-character strings, where the first character is a rank from the set {'2', '3', '4', '5', '6', '7', '8', '9'} and the second character is a suit from the set {'C', 'D', 'H', 'S'}.
def func_1():
    input()
    trump = input()
    trumps = []
    answers = []
    suits = {'C': None, 'D': None, 'H': None, 'S': None}
    for card in input().split():
        rank, suit = card
        
        if suit == trump:
            trumps.append(rank)
        elif suits[suit] is not None:
            answers.append(' '.join([(x + suit) for x in sorted([suits[suit], rank])]))
            suits[suit] = None
        else:
            suits[suit] = rank
        
    #State: `t` is an integer such that 1 <= t <= 100; `n` is an integer such that 1 <= n <= 16; `trump` is a single character from the set {'C', 'D', 'H', 'S'}; `trumps` is a list containing the ranks of all cards that are trumps; `answers` is a list containing strings of sorted pairs of non-trump cards of the same suit; `suits` is a dictionary with keys 'C', 'D', 'H', 'S' and values set to `None` for suits that had no non-trump cards or had pairs of non-trump cards already added to `answers`.
    for (suit, rank) in suits.items():
        if rank is None:
            continue
        
        if trumps != []:
            answers.append(f'{rank}{suit} {trumps.pop()}{trump}')
        else:
            print('IMPOSSIBLE')
            return
        
    #State: t is 50, n is 8, trump is 'H', trumps is either [] or ['A'], answers is either ['23', '45', 'HQ QH'] or ['23', '45', 'HQ QH', 'NoneSH KH'] or ['23', '45', 'HQ QH', 'NoneHA H'] or ['23', '45', 'HQ QH', 'NoneSH KH', 'NoneHA H'], suits is {'C': None, 'D': ['6', '7'], 'H': None, 'S': None}.
    trumps = sorted(trumps, reverse=True)
    while trumps != []:
        print(f'{trumps.pop()}{trump} {trumps.pop()}{trump}')
        
    #State: `t` is 50, `n` is 8, `trump` is 'H', `trumps` is `[]`, `answers` is either ['23', '45', 'HQ QH'] or ['23', '45', 'HQ QH', 'NoneSH KH'] or ['23', '45', 'HQ QH', 'NoneHA H'] or ['23', '45', 'HQ QH', 'NoneSH KH', 'NoneHA H'], `suits` is {'C': None, 'D': ['6', '7'], 'H': None, 'S': None}
    for answer in answers:
        print(answer)
        
    #State: `t` is 50, `n` is 8, `trump` is 'H', `trumps` is `[]`, `answers` is `['23', '45', 'HQ QH', 'NoneHA H', 'NoneSH KH']`, `suits` is {'C': None, 'D': ['6', '7'], 'H': None, 'S': None}, `answer` is 'NoneHA H'
#Overall this is what the function does:The function `func_1` reads input values including the number of test cases, the number of cards, the trump suit, and the list of cards. It processes these cards to form pairs, prioritizing trumps and non-trump pairs of the same suit. The function prints out the pairs or 'IMPOSSIBLE' if it cannot form the required pairs. The function does not return any value.

