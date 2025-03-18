#State of the program right berfore the function call: a is a list of integers representing the integers on the cards in your hand, and n is an integer representing the number of cards you and Nene receive in the beginning of the game. It is guaranteed that the length of the list a is n, and each integer in the list a is between 1 and n, inclusive, and appears at most twice.
def func_1(a, n):
    count_a = {}
    for num in a:
        if num in count_a:
            count_a[num] += 1
        else:
            count_a[num] = 1
        
    #State: Output State: The final state of `count_a` will be a dictionary where each key is a unique integer from the list `a`, and the corresponding value is the count of how many times that integer appeared in the list `a`.
    #
    #In this specific case, after the loop has executed all its iterations, the dictionary `count_a` will contain each distinct number from the list `a` as a key, with the value being the total count of occurrences of that number in the list. Since we know that after 3 iterations, the last number encountered (`num`) is 2 and its count is 1, it means 2 is one of the numbers in the list `a`. However, without the full list `a`, we can't specify the exact counts for all numbers, but we know the process continues until every number in `a` has been processed.
    #
    #For example, if `a` was `[1, 2, 2, 3, 4, 2]`, then `count_a` would be `{1: 1, 2: 3, 3: 1, 4: 1}` after the loop completes.
    max_score = 0
    for num in range(1, n + 1):
        if num in count_a:
            if count_a[num] == 2:
                max_score += 1
        
    #State: The final value of `max_score` is 2, `num` is n, `n` must be greater than or equal to 3, and `num` (which is now `n`) must be in `count_a` with a value of 2.
    return max_score
    #The program returns 2
#Overall this is what the function does:The function accepts a list of integers `a` representing the integers on the cards in your hand and an integer `n` representing the number of cards you and Nene receive at the beginning of the game. It returns the count of integers in `a` that appear exactly twice. Given the constraints, the function will always return 2.

