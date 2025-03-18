#State of the program right berfore the function call: a is a list of integers representing the integers on the cards in your hand, and n is an integer representing the number of cards you and Nene receive in the beginning of the game. It is guaranteed that the length of a is n, and each integer from 1 through n appears in the sequence a at most 2 times.
def func_1(a, n):
    count_a = {}
    for num in a:
        if num in count_a:
            count_a[num] += 1
        else:
            count_a[num] = 1
        
    #State: `count_a` is a dictionary where each key is an element from the iterable `a` and the corresponding value is the frequency of that element in `a`.
    max_score = 0
    for num in range(1, n + 1):
        if num in count_a:
            if count_a[num] == 2:
                max_score += 1
        
    #State: The final value of `max_score` is 2, `num` is n, `n` is greater than or equal to 3, and `num` (which is n) is in `count_a`.
    return max_score
    #The program returns 2
#Overall this is what the function does:The function accepts a list of integers `a` and an integer `n`. It calculates the maximum score based on the frequency of each integer in the list `a`. If any integer appears exactly twice in the list, the score increases by 1. The function returns the final score, which is always 2 under the given conditions.

