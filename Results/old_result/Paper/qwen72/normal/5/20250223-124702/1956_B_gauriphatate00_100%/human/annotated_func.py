#State of the program right berfore the function call: a is a list of integers of length n, where 1 ≤ n ≤ 2 · 10^5, and each integer a_i in a satisfies 1 ≤ a_i ≤ n. Each integer from 1 to n appears in the list a at most 2 times.
def func_1(a, n):
    count_a = {}
    for num in a:
        if num in count_a:
            count_a[num] += 1
        else:
            count_a[num] = 1
        
    #State: `count_a` is a dictionary where each key is an integer from the list `a`, and the value associated with each key is the count of how many times that integer appears in the list `a`. The list `a` remains unchanged.
    max_score = 0
    for num in range(1, n + 1):
        if num in count_a:
            if count_a[num] == 2:
                max_score += 1
        
    #State: `count_a` remains the same, and `max_score` is the number of keys in `count_a` that have a value of 2.
    return max_score
    #The program returns the number of keys in `count_a` that have a value of 2.
#Overall this is what the function does:The function `func_1` accepts a list `a` of integers and an integer `n`. It returns the count of integers in `a` that appear exactly 2 times. The list `a` remains unchanged.

