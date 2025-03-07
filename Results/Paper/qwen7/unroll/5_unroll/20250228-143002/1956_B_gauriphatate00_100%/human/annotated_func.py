#State of the program right berfore the function call: a is a list of n integers where each integer is between 1 and n (inclusive), and each integer from 1 to n appears at most twice in the list.
def func_1(a, n):
    count_a = {}
    for num in a:
        if num in count_a:
            count_a[num] += 1
        else:
            count_a[num] = 1
        
    #State: Output State: `count_a` is a dictionary where the keys are the unique integers from the list `a`, and the values are the counts of how many times each integer appears in the list `a`. Each integer from 1 to n appears at most twice according to the problem statement.
    max_score = 0
    for num in range(1, n + 1):
        if num in count_a:
            if count_a[num] == 2:
                max_score += 1
        
    #State: Output State: `max_score` is the number of integers from 1 to n that appear exactly twice in the list `a`. `count_a` remains a dictionary where the keys are the unique integers from the list `a`, and the values are the counts of how many times each integer appears in the list `a`.
    return max_score
    #The program returns max_score, which is the number of integers from 1 to n that appear exactly twice in the list 'a'.
#Overall this is what the function does:The function accepts a list 'a' containing n integers, where each integer is between 1 and n (inclusive), and each integer from 1 to n appears at most twice in the list. It counts how many times each integer appears in the list and stores these counts in a dictionary. Then, it calculates the number of integers from 1 to n that appear exactly twice and returns this count.

