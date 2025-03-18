#State of the program right berfore the function call: t is an integer such that 1 <= t <= 100. For each test case, n is an integer such that 1 <= n <= 16, trump_suit is a character that is one of "CDHS". There are 2n cards, each card is a string of length 2, where the first character is a rank from "23456789" and the second character is a suit from "CDHS". All cards are distinct.
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
        
    #State: - `t` remains the same.
    #- `n` remains the same.
    #- `trump_suit` remains the same.
    #- `cards` remains the same.
    #- `trumps`: Contains the sorted ranks of all cards that are of the trump suit.
    #- `answers`: Contains the pairs of cards (not of the trump suit) from the same suit, sorted by rank.
    #- `suits`: Contains `None` for all suits, as any stored cards would have been paired and added to `answers`.
    #
    #Output State:
    for (suit, rank) in suits.items():
        if rank is None:
            continue
        
        if trumps != []:
            answers.append(f'{rank}{suit} {trumps.pop()}{trump}')
        else:
            print('IMPOSSIBLE')
            return
        
    #State: `t` remains the same. `n` remains the same. `trump_suit` remains the same. `cards` remains the same. `trumps`: []. `answers`: [processed pairs]. `suits`: {all suits: None}.
    trumps = sorted(trumps, reverse=True)
    while trumps != []:
        print(f'{trumps.pop()}{trump} {trumps.pop()}{trump}')
        
    #State: `t` remains the same; `n` remains the same; `trump_suit` remains the same; `cards` remains the same; `trumps`: []; `answers`: [processed pairs]; `suits`: {all suits: None}.
    for answer in answers:
        print(answer)
        
    #State: t remains the same; n remains the same; trump_suit remains the same; cards remains the same; trumps: []; answers: [processed pairs]; suits: {all suits: None}.
#Overall this is what the function does:The function processes a set of cards for a given number of test cases, identifies pairs of non-trump cards from the same suit, and pairs any remaining single cards with the highest available trump cards. It outputs these pairs and indicates if it's impossible to pair all cards due to insufficient trump cards.

