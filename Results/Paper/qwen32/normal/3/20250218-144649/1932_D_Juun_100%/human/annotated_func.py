#State of the program right berfore the function call: The input consists of multiple test cases. For each test case, the first line contains an integer n (1 ≤ n ≤ 16), representing the number of rounds. The second line contains a single character representing the trump suit ('C', 'D', 'H', or 'S'). The third line contains 2n distinct two-character strings, each representing a card in the format <rank><suit>, where rank is one of '2', '3', '4', '5', '6', '7', '8', '9' and suit is one of 'C', 'D', 'H', 'S'.
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
        
    #State: trumps is ['2', '4', '6', '7'], answers is ['3C 5C'], suits is {'C': None, 'D': '8', 'H': None, 'S': None}
    for (suit, rank) in suits.items():
        if rank is None:
            continue
        
        if trumps != []:
            answers.append(f'{rank}{suit} {trumps.pop()}{trump}')
        else:
            print('IMPOSSIBLE')
            return
        
    #State: trumps is ['2', '4', '6'], answers is ['3C 5C', '8D 7'], suits is {'C': None, 'D': '8', 'H': None, 'S': None}
    trumps = sorted(trumps, reverse=True)
    while trumps != []:
        print(f'{trumps.pop()}{trump} {trumps.pop()}{trump}')
        
    #State: `trumps` is `[]`, `answers` is `['3C 5C', '8D 7']`, `suits` is `{'C': None, 'D': '8', 'H': None, 'S': None}`.
    for answer in answers:
        print(answer)
        
    #State: `trumps` is `[]`, `answers` is `['3C 5C', '8D 7', 'new_answer']`, `answer` is `'new_answer'`, `suits` is `{'C': None, 'D': '8', 'H': None, 'S': None}`
#Overall this is what the function does:The function `func_1` processes a series of test cases, each consisting of a number of rounds, a trump suit, and a list of cards. It determines pairs of cards to be played according to the rules involving the trump suit and prints these pairs. The function does not return any value and outputs the results directly.

