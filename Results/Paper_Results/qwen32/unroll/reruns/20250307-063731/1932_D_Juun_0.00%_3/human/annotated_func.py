#State of the program right berfore the function call: t is an integer such that 1 <= t <= 100. For each test case, n is an integer such that 1 <= n <= 16. The trump suit is a single character from the set {'C', 'D', 'H', 'S'}. The description of 2n cards is a list of 2n unique two-character strings where the first character is a rank from the set {'2', '3', '4', '5', '6', '7', '8', '9'} and the second character is a suit from the set {'C', 'D', 'H', 'S'}.
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
        
    #State: `t` is an integer such that 1 <= t <= 100; `n` is an integer such that 1 <= n <= 16; `trumps` is a list of ranks of cards that are trumps; `answers` is a list of sorted pairs of non-trump cards of the same suit; `suits` is a dictionary where each key's value is either `None` or the rank of an unpaired non-trump card of that suit.
    for (suit, rank) in suits.items():
        if rank is None:
            continue
        
        if trumps != []:
            answers.append(f'{rank}{suit} {trumps.pop()}{trump}')
        else:
            print('IMPOSSIBLE')
            return
        
    #State: t is an integer such that 1 <= t <= 100; n is an integer such that 1 <= n <= 16; trumps is a list of ranks of cards that are trumps and is empty; answers is a list of sorted pairs of non-trump cards of the same suit with additional pairs of non-trump and trump cards; suits is a dictionary where each key's value is either None or the rank of an unpaired non-trump card of that suit and is unchanged.
    trumps = sorted(trumps)
    while trumps != []:
        print(f'{trumps.pop()}{trump} {trumps.pop()}{trump}')
        
    #State: `t` is an integer such that 1 <= t <= 100; `n` is an integer such that 1 <= n <= 16; `trumps` is an empty list; `answers` is a list of sorted pairs of non-trump cards of the same suit with additional pairs of non-trump and trump cards; `suits` is a dictionary where each key's value is either None or the rank of an unpaired non-trump card of that suit and is unchanged.
    for answer in answers:
        print(answer)
        
    #State: t is an integer such that 1 <= t <= 100; n is an integer such that 1 <= n <= 16; trumps is an empty list; answers is a list of sorted pairs of non-trump cards of the same suit with additional pairs of non-trump and trump cards; suits is a dictionary where each key's value is either None or the rank of an unpaired non-trump card of that suit and is unchanged. The answers list has been printed, with each pair printed on a new line.
#Overall this is what the function does:The function processes a set of cards for a given number of test cases, identifies pairs of cards, and prints them according to specific rules involving a designated trump suit. For each test case, it pairs non-trump cards of the same suit, then pairs any remaining unpaired non-trump cards with the highest available trump cards. If there are insufficient trumps to pair all unpaired non-trump cards, it prints "IMPOSSIBLE". The function does not return a value but prints the pairs of cards.

