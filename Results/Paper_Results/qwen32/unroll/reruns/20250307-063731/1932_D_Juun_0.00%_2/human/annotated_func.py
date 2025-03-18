#State of the program right berfore the function call: t is an integer such that 1 <= t <= 100. For each test case, n is an integer such that 1 <= n <= 16. The trump suit is a single character from the set {'C', 'D', 'H', 'S'}. The 2n cards are provided as a list of 2n unique two-character strings, where the first character is a rank from the set {'2', '3', '4', '5', '6', '7', '8', '9'} and the second character is a suit from the set {'C', 'D', 'H', 'S'}.
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
        
    #State: `trumps` is a list of ranks of all cards of the trump suit, and `answers` is a list of strings representing pairs of non-trump cards in sorted order. The `suits` dictionary will have all values set to `None` as all suits either had their cards paired or were trump cards.
    for (suit, rank) in suits.items():
        if rank is None:
            continue
        
        if trumps != []:
            answers.append(f'{rank}{suit} {trumps.pop()}{trump}')
        else:
            print('IMPOSSIBLE')
            return
        
    #State: `trumps` is an empty list, `answers` contains strings representing pairs of non-trump cards with one card from the original `trumps` list, and `suits` remains a dictionary with all values set to `None`.
    trumps = sorted(trumps)
    while trumps != []:
        print(f'{trumps.pop()}{trump} {trumps.pop()}{trump}')
        
    #State: `trumps` is an empty list, `answers` contains strings representing pairs of non-trump cards with one card from the original `trumps` list, and `suits` remains a dictionary with all values set to `None`.
    for answer in answers:
        print(answer)
        
    #State: `trumps` is an empty list, `answers` contains strings representing pairs of non-trump cards with one card from the original `trumps` list (unchanged), `suits` remains a dictionary with all values set to `None` (unchanged).
#Overall this is what the function does:The function processes a series of test cases where each test case consists of a number of cards and a trump suit. It pairs cards of the same suit and pairs remaining non-trump cards with the highest available trump cards. If there are not enough trump cards to pair with all non-trump cards, it prints "IMPOSSIBLE". Otherwise, it prints all pairs of cards.

