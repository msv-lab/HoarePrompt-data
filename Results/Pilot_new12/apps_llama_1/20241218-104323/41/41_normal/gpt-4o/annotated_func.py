#State of the program right berfore the function call: there are two sequences of n integers where n is a positive integer greater than or equal to 2, the first sequence represents the ratings of n participants before a round and the second sequence represents the ratings of the same participants after the round, and the participants are listed in order from the top to the bottom of the standings.
def func():
    n = int(input())
    ratings = []
    is_rated = False
    is_unrated = False
    for _ in range(n):
        a, b = map(int, input().split())
        
        ratings.append((a, b))
        
        if a != b:
            is_rated = True
        
    #State of the program after the  for loop has been executed: `n` is a positive integer greater than or equal to 2, `ratings` is a list of `n` tuples where each tuple contains a pair of integers, `is_rated` is `True` if any pair of integers in `ratings` are not equal, otherwise `is_rated` is `False`, and `is_unrated` is `False`.
    if (not is_rated) :
        for i in range(1, n):
            if ratings[i - 1][0] < ratings[i][0]:
                is_unrated = True
                break
            
        #State of the program after the  for loop has been executed: `n` is a positive integer greater than or equal to 2, `ratings` is a list of `n` tuples where each tuple contains a pair of integers, `is_rated` is `False`, and `is_unrated` is `True` if any rating's first element is greater than the previous one, otherwise `is_unrated` is `False`.
    #State of the program after the if block has been executed: *`n` is a positive integer greater than or equal to 2, `ratings` is a list of `n` tuples where each tuple contains a pair of integers. If `is_rated` is `False`, then `is_unrated` is `True` if any rating's first element is greater than the previous one, otherwise `is_unrated` is `False`. If `is_rated` is `True`, then the state of `is_unrated` remains unchanged as there is no else part to handle this case.
    if is_rated :
        print('rated')
    else :
        if is_unrated :
            print('unrated')
        else :
            print('maybe')
        #State of the program after the if-else block has been executed: *`n` is a positive integer greater than or equal to 2, `ratings` is a list of `n` tuples where each tuple contains a pair of integers, `is_rated` is `False`. If `is_unrated` is `True`, then 'unrated' has been printed to the console. If `is_unrated` is `False`, then 'maybe' has been printed to the console.
    #State of the program after the if-else block has been executed: `n` is a positive integer greater than or equal to 2, `ratings` is a list of `n` tuples where each tuple contains a pair of integers. If `is_rated` is `True`, then the state of `is_unrated` remains unchanged and 'rated' has been printed to the console. If `is_rated` is `False`, then if `is_unrated` is `True`, 'unrated' has been printed to the console; otherwise, 'maybe' has been printed to the console.
#Overall this is what the function does:The function takes two sequences of n integers as input, representing ratings before and after a round, where n is a positive integer greater than or equal to 2. It checks if any participant's rating has changed and if the initial ratings are in descending order. The function then prints one of three possible outcomes: 'rated' if any rating has changed, 'unrated' if the ratings are in ascending order and no rating has changed, or 'maybe' if the ratings are in descending order and no rating has changed. The function does not return any value, but instead prints the outcome to the console. The input sequences are not modified by the function. The function handles all potential edge cases, including when n is 2 or greater, and when the input sequences are valid or invalid. However, the function does not perform any error checking on the input values, so it assumes that the input will always be valid.

