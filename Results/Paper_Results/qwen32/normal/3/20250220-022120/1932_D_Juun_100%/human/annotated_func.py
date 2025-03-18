#State of the program right berfore the function call: The input consists of integer t (1 ≤ t ≤ 100) representing the number of test cases. For each test case, there are three lines: an integer n (1 ≤ n ≤ 16) representing the number of rounds, a single character representing the trump suit ('C', 'D', 'H', or 'S'), and a string of 2n two-character strings representing the cards in the discard pile. Each card is uniquely identified by its rank ('2', '3', '4', '5', '6', '7', '8', '9') and suit ('C', 'D', 'H', 'S').
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
        
    #State: `trumps` contains all trump card ranks, `answers` contains all sorted non-trump card pairs, and `suits` contains `None` for all suits unless there was an odd number of non-trump cards for a particular suit, in which case it will have the last unpaired card's rank for that suit.
    for (suit, rank) in suits.items():
        if rank is None:
            continue
        
        if trumps != []:
            answers.append(f'{rank}{suit} {trumps.pop()}{trump}')
        else:
            print('IMPOSSIBLE')
            return
        
    #State: `trumps` is empty or contains remaining trump cards, `answers` contains all formed pairs, `suits` contains `None` for all suits that had non-None ranks.
    trumps = sorted(trumps, reverse=True)
    while trumps != []:
        print(f'{trumps.pop()}{trump} {trumps.pop()}{trump}')
        
    #State: `trumps` is an empty list, `answers` contains all formed pairs, `suits` contains `None` for all suits that had non-None ranks.
    for answer in answers:
        print(answer)
        
    #State: `trumps` is an empty list, `answers` is an empty list, `suits` contains `None` for all suits that had non-None ranks.
#Overall this is what the function does:The function processes a series of test cases, each consisting of a number of rounds, a trump suit, and a discard pile of cards. It pairs non-trump cards of the same suit and pairs any remaining unpaired non-trump cards with the highest remaining trump cards. If there are insufficient trump cards to pair all unpaired non-trump cards, it outputs "IMPOSSIBLE". Otherwise, it prints all card pairs, first the non-trump pairs and then the pairs involving trump cards, in a specified order.

