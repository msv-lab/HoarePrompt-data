#State of the program right berfore the function call: a is a list of n integers where each integer from 1 through n appears at most 2 times, and n is an integer such that 1 <= n <= 2 * 10^5.
def func_1(a, n):
    count_a = {}
    for num in a:
        if num in count_a:
            count_a[num] += 1
        else:
            count_a[num] = 1
        
    #State: `count_a` is a dictionary where each key is a unique integer from the list `a`, and the corresponding value is the count of how many times that integer appears in `a`.
    max_score = 0
    for num in range(1, n + 1):
        if num in count_a:
            if count_a[num] == 2:
                max_score += 1
        
    #State: `count_a` remains the same as the initial state, and `max_score` is the total number of unique integers in `count_a` that have a count of 2.
    return max_score
    #The program returns the total number of unique integers in `count_a` that have a count of 2.
#Overall this is what the function does:The function accepts a list `a` of integers and an integer `n`. It returns the count of unique integers in the list `a` that appear exactly 2 times.

