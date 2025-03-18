#State of the program right berfore the function call: a is a list of integers where each integer from 1 through n appears at most 2 times, and n is an integer such that 1 <= n <= 2 * 10^5. The length of the list a is exactly n.
def func_1(a, n):
    count_a = {}
    for num in a:
        if num in count_a:
            count_a[num] += 1
        else:
            count_a[num] = 1
        
    #State: count_a is a dictionary where each key is an integer from 1 through n, and each value is the count of occurrences of that integer in the list a, which can be either 1 or 2.
    max_score = 0
    for num in range(1, n + 1):
        if num in count_a:
            if count_a[num] == 2:
                max_score += 1
        
    #State: `count_a` is a dictionary where each key is an integer from 1 through n, and each value is the count of occurrences of that integer in the list a, which can be either 1 or 2; `max_score` is the count of integers from 1 to n that have a value of 2 in `count_a`.
    return max_score
    #The program returns the count of integers from 1 to n that have a value of 2 in `count_a`.
#Overall this is what the function does:The function accepts a list `a` of integers and an integer `n`. The list `a` contains integers from 1 through `n` where each integer appears at most 2 times. The function returns the count of integers from 1 to `n` that appear exactly 2 times in the list `a`.

