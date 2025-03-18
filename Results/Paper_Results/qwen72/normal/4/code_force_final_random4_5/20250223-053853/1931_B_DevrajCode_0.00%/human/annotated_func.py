#State of the program right berfore the function call: n is a positive integer (1 ≤ n ≤ 2 · 10^5), and a is a list of n non-negative integers (0 ≤ a_i ≤ 10^9) where the sum of a_i is divisible by n.
def func_1(n, a):
    total_water = sum(a)
    if (total_water % n != 0) :
        return 'No'
        #The program returns 'No'
    #State: n is a positive integer (1 ≤ n ≤ 2 · 10^5), a is a list of n non-negative integers (0 ≤ a_i ≤ 10^9) where the sum of a_i is divisible by n, total_water is the sum of all elements in the list a, and total_water % n is equal to 0.
    target = total_water // n
    container = 0
    for water in a:
        container += water - target
        
        if container < 0:
            return 'No'
        
    #State: `container` is 0.
    return 'Yes'
    #The program returns 'Yes'.
#Overall this is what the function does:The function `func_1` accepts a positive integer `n` and a list `a` of `n` non-negative integers, where the sum of the integers in `a` is divisible by `n`. It returns 'No' if at any point during the iteration over the elements of `a`, the cumulative difference between each element and the target value (which is the average of the elements in `a`) becomes negative. If the cumulative difference is non-negative for all elements, the function returns 'Yes'.

