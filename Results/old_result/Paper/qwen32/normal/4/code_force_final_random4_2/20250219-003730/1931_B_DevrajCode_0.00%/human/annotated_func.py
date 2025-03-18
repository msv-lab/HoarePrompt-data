#State of the program right berfore the function call: n is an integer such that 1 <= n <= 2 * 10^5, and a is a list of integers of length n where 0 <= a_i <= 10^9. The sum of a_i is divisible by n.
def func_1(n, a):
    total_water = sum(a)
    if (total_water % n != 0) :
        return 'No'
        #The program returns 'No'
    #State: `n` is an integer such that 1 <= n <= 2 * 10^5, `a` is a list of integers of length n where 0 <= a_i <= 10^9, the sum of a_i is divisible by n, and `total_water` is the sum of all elements in `a`. Additionally, `total_water` is divisible by `n`.
    target = total_water // n
    container = 0
    for water in a:
        container += water - target
        
        if container < 0:
            return 'No'
        
    #State: container is 0.
    return 'Yes'
    #The program returns 'Yes'
#Overall this is what the function does:The function accepts an integer `n` and a list of integers `a` of length `n`. It checks if the sum of the elements in `a` is divisible by `n` and if it's possible to distribute the elements in `a` such that each element is equal to the average of the sum of `a` divided by `n` without any element going below zero during the distribution process. If both conditions are met, it returns 'Yes'; otherwise, it returns 'No'.

