#State of the program right berfore the function call: a is a list of integers where each integer from 1 to n appears at most twice, and n is a positive integer such that 1 ≤ n ≤ 2 · 10^5.
def func_1(a, n):
    count_a = {}
    for num in a:
        if num in count_a:
            count_a[num] += 1
        else:
            count_a[num] = 1
        
    #State: `count_a` is a dictionary where each key is an integer from 1 to n, and the value associated with each key is the number of times that integer appears in the list `a`. Each integer from 1 to n appears at most twice in `a`, so the values in `count_a` will be either 1 or 2.
    max_score = 0
    for num in range(1, n + 1):
        if num in count_a:
            if count_a[num] == 2:
                max_score += 1
        
    #State: `max_score` is the number of integers from 1 to n that appear exactly twice in the list `a`.
    return max_score
    #The program returns the number of integers from 1 to n that appear exactly twice in the list `a`.
#Overall this is what the function does:The function `func_1` accepts a list `a` of integers and a positive integer `n`. It returns the count of integers from 1 to n that appear exactly twice in the list `a`. The function does not modify the input list `a` or the integer `n`. After the function concludes, the final state of the program is that the variable `max_score` holds the number of integers from 1 to n that appear exactly twice in the list `a`.

