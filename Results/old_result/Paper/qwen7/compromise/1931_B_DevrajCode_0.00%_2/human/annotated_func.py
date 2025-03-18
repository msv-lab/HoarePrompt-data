#State of the program right berfore the function call: n is a positive integer, and a is a list of n integers where each integer represents the amount of water in the corresponding container. The sum of all integers in the list a is divisible by n.
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
        
    #State: Output State: `total_water` is the sum of all integers in the list `a`, `n` is a positive integer, `target` is the integer division of `total_water` by `n`, and `container` is the result after adding each element in `a` minus `target` to it, returning 'No' if at any point `container` becomes less than 0.
    return 'Yes'
    #The program returns 'Yes'
#Overall this is what the function does:The function accepts a positive integer `n` and a list `a` of `n` integers. It calculates the total amount of water and checks if it can be evenly distributed among the containers represented by the list. If the total water is not divisible by `n`, or if during the distribution process the remaining water in any container becomes negative, the function returns 'No'. Otherwise, it returns 'Yes', indicating the water can be evenly distributed.

