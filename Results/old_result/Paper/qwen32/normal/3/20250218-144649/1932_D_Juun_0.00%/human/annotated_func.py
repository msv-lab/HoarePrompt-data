#State of the program right berfore the function call: t is an integer such that 1 <= t <= 100. For each test case, n is an integer such that 1 <= n <= 16, trump is a character from the set {'C', 'D', 'H', 'S'}, and cards is a list of 2n distinct two-character strings where each string consists of a rank from '2' to '9' and a suit from 'C', 'D', 'H', 'S'.
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
        
    #State: - After all cards are processed, `trumps` will contain the ranks of all cards that have the trump suit.
    #   - `answers` will contain strings representing pairs of cards from non-trump suits, sorted by rank.
    #   - `suits` will have `None` for all suits that had at least one card processed (i.e., all suits that were part of pairs in `answers`).
    #
    #Given this understanding, the final output state can be described as:
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
        
    #State: `trumps` is an empty list, `answers` contains all the formatted strings created during the loop's execution, and `suits` has `None` for all suits that had at least one card processed.
    trumps = sorted(trumps)
    while trumps != []:
        print(f'{trumps.pop()}{trump} {trumps.pop()}{trump}')
        
    #State: `trumps` is `[]`, `answers` contains all the formatted strings created during the loop's execution, and `suits` has `None` for all suits that had at least one card processed.
    for answer in answers:
        print(answer)
        
    #State: `trumps` is `[]`, `answers` contains all the formatted strings created during the loop's execution, and `suits` has `None` for all suits that had at least one card processed.
#Overall this is what the function does:The function `func_1` reads input values including the trump suit and a list of cards. It processes the cards to form pairs, prioritizing cards of the trump suit. It prints pairs of cards, ensuring that if a card of a non-trump suit is left unpaired, it is paired with the highest available trump card. If there are leftover trump cards that cannot be paired, it prints them in descending order. The function does not return any value and outputs the results directly.

