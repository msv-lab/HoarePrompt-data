#State of the program right berfore the function call: a is a list of integers of length n, where 1 ≤ n ≤ 2 · 10^5, and each integer a_i satisfies 1 ≤ a_i ≤ n. Each integer from 1 to n appears in the list a at most 2 times. n is a positive integer.
def func_1(a, n):
    count_a = {}
    for num in a:
        if num in count_a:
            count_a[num] += 1
        else:
            count_a[num] = 1
        
    #State: `count_a` is a dictionary where each key is an integer from the list `a`, and the value associated with each key is the number of times that integer appears in the list `a`. The length of the list `a` remains `n`, and each integer from 1 to n appears at most 2 times in the list.
    max_score = 0
    for num in range(1, n + 1):
        if num in count_a:
            if count_a[num] == 2:
                max_score += 1
        
    #State: `max_score` is the number of integers in the list `a` that appear exactly twice.
    return max_score
    #The program returns the number of integers in the list `a` that appear exactly twice.
#Overall this is what the function does:The function `func_1` accepts a list `a` of integers and a positive integer `n`. It returns the count of integers in `a` that appear exactly twice. The function does not modify the input list `a` or the integer `n`.

