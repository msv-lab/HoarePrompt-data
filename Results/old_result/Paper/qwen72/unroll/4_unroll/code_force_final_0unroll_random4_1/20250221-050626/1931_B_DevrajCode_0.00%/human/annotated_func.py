#State of the program right berfore the function call: n is a positive integer such that 1 <= n <= 2 \cdot 10^5, and a is a list of n integers where 0 <= a_i <= 10^9, and the sum of a_i is divisible by n.
def func_1(n, a):
    total_water = sum(a)
    if (total_water % n != 0) :
        return 'No'
        #The program returns 'No'
    #State: `n` is a positive integer such that 1 <= n <= 2 \cdot 10^5, `a` is a list of n integers where 0 <= a_i <= 10^9, and the sum of a_i is divisible by n. `total_water` is equal to the sum of all elements in `a`, and `total_water % n` is equal to 0.
    target = total_water // n
    container = 0
    for water in a:
        container += water - target
        
        if container < 0:
            return 'No'
        
    #State: `container` is 0.
    return 'Yes'
    #The program returns 'Yes'
#Overall this is what the function does:The function `func_1` accepts a positive integer `n` and a list of `n` integers `a`. It checks if the sum of the integers in `a` is divisible by `n` and if it is possible to redistribute the integers in `a` such that each element equals the average of the sum. If the sum of `a` is not divisible by `n` or if redistribution is not possible, the function returns 'No'. If the redistribution is possible, the function returns 'Yes'.

