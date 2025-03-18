#State of the program right berfore the function call: t is an integer such that 1 <= t <= 100. For each test case, n is an integer such that 1 <= n <= 16. The trump suit is a single character from the set {'C', 'D', 'H', 'S'}. The description of 2n cards is a list of 2n unique two-character strings, where the first character is a rank from the set {'2', '3', '4', '5', '6', '7', '8', '9'} and the second character is a suit from the set {'C', 'D', 'H', 'S'}.
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
        
    #State: `trumps` is a list of ranks of trump cards, `answers` is a list of sorted rank pairs for non-trump suits, and `suits` is a dictionary with suits that had unpaired cards mapped to their ranks and other suits mapped to `None`.
    for (suit, rank) in suits.items():
        if rank is None:
            continue
        
        if trumps != []:
            answers.append(f'{rank}{suit} {trumps.pop()}{trump}')
        else:
            print('IMPOSSIBLE')
            return
        
    #State: trumps = [], answers = ['2H 3H', '4S 5S', 'AH K', 'CK Q', 'SQ J'], suits = {'H': 'A', 'D': None, 'C': 'K', 'S': 'Q'}
    trumps = sorted(trumps)
    while trumps != []:
        print(f'{trumps.pop()}{trump} {trumps.pop()}{trump}')
        
    #State: trumps is [], answers is ['2H 3H', '4S 5S', 'AH K', 'CK Q', 'SQ J'], suits is {'H': 'A', 'D': None, 'C': 'K', 'S': 'Q'}
    for answer in answers:
        print(answer)
        
    #State: trumps is [], answers is ['2H 3H', '4S 5S', 'AH K', 'CK Q', 'SQ J'], suits is {'H': 'A', 'D': None, 'C': 'K', 'S': 'Q'}
#Overall this is what the function does:The function `func_1` processes a set of card pairs for a given number of test cases, taking into account a specified trump suit. It outputs pairs of cards, ensuring that each non-trump suit has its highest-ranked pair matched, and any remaining unpaired cards are matched with the highest-ranked trump cards. If there are not enough trump cards to match all unpaired cards, it outputs "IMPOSSIBLE". The function does not return a value but prints the results directly.

