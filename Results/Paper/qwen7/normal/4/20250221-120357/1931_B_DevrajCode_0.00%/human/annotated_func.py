#State of the program right berfore the function call: n is a positive integer, and a is a list of n non-negative integers such that the sum of the integers in a is divisible by n.
def func_1(n, a):
    total_water = sum(a)
    if (total_water % n != 0) :
        return 'No'
        #The program returns 'No'
    #State: `total_water` is equal to the sum of the integers in list `a`, `n` is a positive integer, and a is a list of `n` non-negative integers such that the sum of the integers in `a` is divisible by `n`, and `total_water % n == 0`
    target = total_water // n
    container = 0
    for water in a:
        container += water - target
        
        if container < 0:
            return 'No'
        
    #State: Output State: The total_water remains equal to the sum of the integers in list `a`, `n` is a positive integer, `target` is `total_water // n`, and `container` is adjusted such that it is never less than 0 throughout the entire execution of the loop. If at any point during the loop's execution, the `container` becomes less than 0, the function returns 'No'. If the loop completes without the `container` becoming negative, the function does not return anything and the final value of `container` is 0.
    #
    #This means that after all iterations of the loop, if the loop did not return 'No' due to `container` becoming negative, the `container` variable will be 0. Otherwise, if `container` became negative at any point, the function would have returned 'No' before completing all iterations.
    return 'Yes'
    #The program returns 'Yes'
#Overall this is what the function does:The function `func_1` accepts two parameters: a positive integer `n` and a list `a` of `n` non-negative integers whose sum is divisible by `n`. It checks if it's possible to distribute the water in the list `a` such that no container ever has a negative amount of water. If at any point during the distribution, a container has a negative amount of water, the function returns 'No'. If the distribution can be done without any container having a negative amount of water, the function returns 'Yes'.

