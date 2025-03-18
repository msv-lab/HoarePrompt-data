#State of the program right berfore the function call: t is an integer such that 1 <= t <= 100. For each test case, n is an integer such that 1 <= n <= 16. The trump suit is a single character from the set {'C', 'D', 'H', 'S'}. The description of 2n cards is a list of 2n unique two-character strings, where the first character is one of "23456789" and the second character is one of "CDHS".
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
        
    #State: `trumps` is a list of ranks of trump cards; `answers` is a list of sorted pairs of non-trump cards of the same suit; `suits` is a dictionary with keys 'C', 'D', 'H', 'S' and values either `None` or a rank of a non-trump card that did not form a pair.
    for (suit, rank) in suits.items():
        if rank is None:
            continue
        
        if trumps != []:
            answers.append(f'{rank}{suit} {trumps.pop()}{trump}')
        else:
            print('IMPOSSIBLE')
            return
        
    #State: trumps is [], answers is [('2H', '3H'), 'A C 10S', 'K H JS'], suits is {'C': 'A', 'D': None, 'H': 'K', 'S': 'Q'}
    trumps = sorted(trumps, reverse=True)
    while trumps != []:
        print(f'{trumps.pop()}{trump} {trumps.pop()}{trump}')
        
    #State: `trumps` is [], `answers` is [('2H', '3H'), 'A C 10S', 'K H JS'], `suits` is {'C': 'A', 'D': None, 'H': 'K', 'S': 'Q'}
    for answer in answers:
        print(answer)
        
    #State: trumps is [], answers is [('2H', '3H'), 'A C 10S', 'K H JS'], suits is {'C': 'A', 'D': None, 'H': 'K', 'S': 'Q'}
#Overall this is what the function does:The function processes a series of test cases where each test case consists of a set of cards and a trump suit. It determines the highest card based on the given rules: the highest card in the trump suit wins, otherwise, the highest card of the same suit as the first card wins, and if there's a tie, the card appearing first in the input list wins. The function outputs pairs of cards according to these rules and prints "IMPOSSIBLE" if it cannot form a valid pair.

