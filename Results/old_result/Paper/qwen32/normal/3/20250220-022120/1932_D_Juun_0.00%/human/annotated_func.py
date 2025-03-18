#State of the program right berfore the function call: The input consists of an integer t (1 ≤ t ≤ 100) representing the number of test cases. For each test case, there are three lines: an integer n (1 ≤ n ≤ 16) representing the number of rounds, a single character representing the trump suit ('C', 'D', 'H', or 'S'), and a space-separated list of 2n distinct cards where each card is represented by a two-character string. The first character of each card is a rank ('2', '3', '4', '5', '6', '7', '8', '9') and the second character is a suit ('C', 'D', 'H', 'S').
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
        
    #State: `trumps` contains all ranks of trump cards, `answers` contains all sorted pairs of non-trump cards, `suits` contains `None` for suits with pairs and possibly one remaining rank, `t` and `n` remain unchanged.
    for (suit, rank) in suits.items():
        if rank is None:
            continue
        
        if trumps != []:
            answers.append(f'{rank}{suit} {trumps.pop()}{trump}')
        else:
            print('IMPOSSIBLE')
            return
        
    #State: `trumps` is empty if there were enough trump cards, `answers` contains all sorted pairs of non-trump cards plus one entry for each non-`None` rank in `suits` (or fewer if `trumps` was exhausted), `suits` remains unchanged, and `t` and `n` remain unchanged.
    #
    #Output State:
    trumps = sorted(trumps)
    while trumps != []:
        print(f'{trumps.pop()}{trump} {trumps.pop()}{trump}')
        
    #State: `trumps` is an empty list, `answers` contains all sorted pairs of non-trump cards plus one entry for each non-`None` rank in `suits` (or fewer if `trumps` was exhausted); `suits` remains unchanged; `t` and `n` remain unchanged.
    for answer in answers:
        print(answer)
        
    #State: `trumps` is an empty list, `answers` contains all its entries, `suits` remains unchanged, `t` and `n` remain unchanged, `answer` is the last entry in `answers`.
#Overall this is what the function does:The function `func_1` processes a series of test cases involving cards and a trump suit. For each test case, it pairs non-trump cards and uses trump cards to pair any remaining unpaired cards. It prints the pairs of cards, and if there are insufficient trump cards to pair all remaining unpaired cards, it prints "IMPOSSIBLE". The function does not return any value explicitly and always returns `None` implicitly.

