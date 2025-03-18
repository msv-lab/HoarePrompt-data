#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 100. For each test case, n is an integer such that 1 ≤ n ≤ 16, the trump suit is one of "CDHS", and the description of 2n cards consists of 2n two-character strings where the first character is the rank of the card ("23456789") and the second character is the suit of the card ("CDHS"). All cards are unique within each test case.
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
        
    #State: All cards have been processed, and the final state of the variables is as follows:
    for (suit, rank) in suits.items():
        if rank is None:
            continue
        
        if trumps != []:
            answers.append(f'{rank}{suit} {trumps.pop()}{trump}')
        else:
            print('IMPOSSIBLE')
            return
        
    #State: All cards have been processed, `suits` is an empty dictionary, `trumps` is an empty list, and `answers` is a list containing strings formatted as 'rank{suit} trumps.pop()trump' for each iteration executed.
    trumps = sorted(trumps)
    while trumps != []:
        print(f'{trumps.pop()}{trump} {trumps.pop()}{trump}')
        
    #State: Output State: `suits` is an empty dictionary, `trumps` is an empty list, and `answers` is a list containing strings formatted as 'rank{suit} trumps.pop()trump' for each iteration executed.
    #
    #Explanation: After the loop executes all its iterations, `trumps` will be an empty list because the `while` loop continues to pop elements from `trumps` until it is empty. The `suits` dictionary remains empty as there are no operations that modify it within the loop. The `answers` list collects the printed statements from each iteration of the loop, which follow the format 'rank{suit} trumps.pop()trump'.
    for answer in answers:
        print(answer)
        
    #State: `suits` is an empty dictionary, `trumps` is an empty list, and `answers` is a list containing strings formatted as 'rank{suit} trumps.pop()trump' for each iteration executed.
#Overall this is what the function does:The function processes a set of card descriptions and a trump suit. It determines the order of play based on the given rules and prints the sequence of moves. If there are remaining trumps after processing all cards, it prints pairs of trumps in descending order. The function does not return any value.

