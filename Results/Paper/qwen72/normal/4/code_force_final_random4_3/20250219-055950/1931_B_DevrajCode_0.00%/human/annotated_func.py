#State of the program right berfore the function call: n is a positive integer (1 ≤ n ≤ 2 · 10^5), and a is a list of n integers (0 ≤ a_i ≤ 10^9) where the sum of a_i is divisible by n.
def func_1(n, a):
    total_water = sum(a)
    if (total_water % n != 0) :
        return 'No'
        #The program returns 'No'
    #State: *`n` is a positive integer (1 ≤ n ≤ 2 · 10^5), `a` is a list of n integers (0 ≤ a_i ≤ 10^9) where the sum of a_i is divisible by n, `total_water` is the sum of all elements in `a`, and `total_water % n == 0`
    target = total_water // n
    container = 0
    for water in a:
        container += water - target
        
        if container < 0:
            return 'No'
        
    #State: `n` is a positive integer (1 ≤ n ≤ 2 · 10^5), `a` is a list of n integers (0 ≤ a_i ≤ 10^9) where the sum of a_i is divisible by n, `total_water` is the sum of all elements in `a`, `total_water % n == 0`, `target` is equal to `total_water // n`, `container` is 0, and the loop has executed `n` times.
    return 'Yes'
    #The program returns 'Yes'
#Overall this is what the function does:The function `func_1` accepts a positive integer `n` and a list of `n` integers `a`, where the sum of the integers in `a` is divisible by `n`. It checks if it is possible to redistribute the integers in `a` such that each element in `a` equals the average of the sum of `a` divided by `n`. If at any point during the redistribution process the cumulative difference between the current element and the target average becomes negative, the function returns 'No'. If the redistribution is possible without any negative cumulative differences, the function returns 'Yes'.

