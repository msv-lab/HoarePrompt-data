#State of the program right berfore the function call: n is a positive integer (1 ≤ n ≤ 2 · 10^5), and a is a list of n non-negative integers (0 ≤ a_i ≤ 10^9) such that the sum of a_i is divisible by n.
def func_1(n, a):
    total_water = sum(a)
    if (total_water % n != 0) :
        return 'No'
        #The program returns 'No'
    #State: *`n` is a positive integer (1 ≤ n ≤ 2 · 10^5), `a` is a list of n non-negative integers (0 ≤ a_i ≤ 10^9) such that the sum of a_i is divisible by n, `total_water` is the sum of the elements in `a`, and `total_water % n == 0`
    target = total_water // n
    container = 0
    for water in a:
        container += water - target
        
        if container < 0:
            return 'No'
        
    #State: `container` is 0, `n`, `a`, `total_water`, and `target` remain unchanged.
    return 'Yes'
    #The program returns 'Yes'
#Overall this is what the function does:The function `func_1` accepts a positive integer `n` and a list `a` of `n` non-negative integers, where the sum of the integers in `a` is divisible by `n`. It returns 'No' if it is not possible to redistribute the elements of `a` such that no container (element in `a`) ever has less than the target amount of water (the average sum of elements in `a` divided by `n`), and 'Yes' if such a redistribution is possible. After the function concludes, the variables `n`, `a`, `total_water`, and `target` remain unchanged, and `container` is 0.

