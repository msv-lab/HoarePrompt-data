#State of the program right berfore the function call: n is an integer such that 1 ≤ n ≤ 2 ⋅ 10^5, and a is a list of n integers where 0 ≤ a_i ≤ 10^9. The sum of the elements in a is divisible by n.
def func_1(n, a):
    total_water = sum(a)
    if (total_water % n != 0) :
        return 'No'
        #The program returns 'No'
    #State: `n` is an integer such that 1 ≤ n ≤ 2 ⋅ 10^5, `a` is a list of `n` integers where 0 ≤ a_i ≤ 10^9, the sum of the elements in `a` is divisible by `n`, `total_water` is the sum of the elements in `a`, and `total_water % n` is equal to 0
    target = total_water // n
    container = 0
    for water in a:
        container += water - target
        
        if container < 0:
            return 'No'
        
    #State: container is 0.
    return 'Yes'
    #The program returns 'Yes'
#Overall this is what the function does:The function `func_1` accepts an integer `n` and a list `a` of `n` integers. It returns 'Yes' if it is possible to redistribute the elements of `a` such that each element becomes equal to the average of the list, otherwise it returns 'No'.

