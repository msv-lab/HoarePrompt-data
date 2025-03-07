#State of the program right berfore the function call: n is a positive integer representing the number of containers, and a is a list of n non-negative integers representing the initial amounts of water in each container. The sum of the elements in a is divisible by n.
def func_1(n, a):
    total_water = sum(a)
    if (total_water % n != 0) :
        return 'No'
        #The program returns 'No'
    target = total_water // n
    container = 0
    for water in a:
        container += water - target
        
        if container < 0:
            return 'No'
        
    #State: Output State: The `container` variable will hold the final value after all elements in the list `a` have been processed by the loop. Specifically, for each element `water` in the list `a`, the `container` is updated by adding `water - target`. After all iterations, if the `container` is still greater than or equal to 0, the function does not return anything; otherwise, it returns 'No'.
    #
    #In natural language, the `container` will accumulate the net difference between each element in `a` and the `target` value. If at any point during these additions the `container` becomes negative, the function will terminate and return 'No'. If the loop completes without the `container` becoming negative, the final value of `container` is the output state.
    return 'Yes'
    #The program returns 'Yes' if the container remains non-negative after processing all elements in list `a` by subtracting the `target` from each element, and returns 'No' if the container becomes negative at any point.
#Overall this is what the function does:The function accepts a positive integer `n` and a list `a` of `n` non-negative integers. It calculates a target value which is the average amount of water per container. Then, it iterates through the list `a`, adjusting a running total based on the difference between each element and the target. If at any point the running total becomes negative, the function returns 'No', indicating that it's not possible to evenly distribute the water among the containers without some container having less than the target amount. If the running total remains non-negative throughout the iteration, the function returns 'Yes', indicating that the water can be evenly distributed.

