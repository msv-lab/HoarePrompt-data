#State of the program right berfore the function call: a is a list of n integers where each integer is between 1 and n (inclusive), and each integer from 1 to n appears at most twice in the list.
def func_1(a, n):
    count_a = {}
    for num in a:
        if num in count_a:
            count_a[num] += 1
        else:
            count_a[num] = 1
        
    #State: Output State: `count_a` is a dictionary where the keys are integers from 1 to n and the values are the counts of each integer in the list `a`, with each integer's count being at most 2.
    max_score = 0
    for num in range(1, n + 1):
        if num in count_a:
            if count_a[num] == 2:
                max_score += 1
        
    #State: Output State: `count_a` is a dictionary where the keys are integers from 1 to n and the values are the counts of each integer in the list `a`, with each integer's count being at most 2; `max_score` is the sum of 1 for each integer in `count_a` whose value is 2.
    return max_score
    #The program returns max_score which is the sum of 1 for each integer in count_a whose value is 2
#Overall this is what the function does:The function accepts a list `a` of `n` integers, where each integer is between 1 and `n` (inclusive), and each integer from 1 to `n` appears at most twice in the list. It creates a dictionary `count_a` to count the occurrences of each integer in `a`. Then, it calculates `max_score` as the number of integers in `a` that appear exactly twice. Finally, it returns `max_score`.

