#State of the program right berfore the function call: n is a positive integer (1 ≤ n ≤ 2 · 10^5), and a is a list of n integers (0 ≤ a_i ≤ 10^9) where the sum of a_i is divisible by n.
def func_1(n, a):
    total_water = sum(a)
    if (total_water % n != 0) :
        return 'No'
        #The program returns 'No'
    #State: *`n` is a positive integer (1 ≤ n ≤ 2 · 10^5), `a` is a list of n integers (0 ≤ a_i ≤ 10^9) where the sum of a_i is divisible by n, `total_water` is the sum of all elements in the list `a`, and `total_water % n` is equal to 0
    target = total_water // n
    container = 0
    for water in a:
        container += water - target
        
        if container < 0:
            return 'No'
        
    #State: `container` is 0.
    return 'Yes'
    #The program returns the string 'Yes'.
#Overall this is what the function does:The function `func_1` accepts a positive integer `n` and a list of `n` integers `a` where the sum of `a` is divisible by `n`. It checks whether it is possible to balance the water levels in the containers represented by the list `a` such that each container has the same amount of water. If it is possible to balance the water levels without any container having a negative amount of water during the process, the function returns 'Yes'. Otherwise, it returns 'No'. After the function concludes, the input parameters `n` and `a` remain unchanged, and the function returns either 'Yes' or 'No'.

