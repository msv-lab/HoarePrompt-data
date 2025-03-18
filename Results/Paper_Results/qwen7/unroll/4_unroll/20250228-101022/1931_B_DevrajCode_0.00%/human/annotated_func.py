#State of the program right berfore the function call: n is a positive integer, and a is a list of n integers where each integer represents the amount of water in the corresponding container. The sum of all integers in the list is divisible by n.
def func_1(n, a):
    total_water = sum(a)
    if (total_water % n != 0) :
        return 'No'
        #The program returns 'No'
    #State: `total_water` is the sum of all integers in list `a`, and `n` is a positive integer, and `a` is a list of `n` integers where each integer represents the amount of water in the corresponding container. The sum of all integers in the list is divisible by `n`, and `total_water % n == 0`
    target = total_water // n
    container = 0
    for water in a:
        container += water - target
        
        if container < 0:
            return 'No'
        
    #State: Output State: `total_water` is the sum of all integers in list `a`, `n` is a positive integer, `a` is a list of `n` integers where each integer represents the amount of water in the corresponding container, `target` is `total_water // n`, `container` is the sum of `(water - target)` for each `water` in list `a`. If any `(water - target)` makes `container` negative during the loop, the loop returns 'No'.
    return 'Yes'
    #The program returns 'Yes'
#Overall this is what the function does:The function accepts two parameters: `n`, a positive integer, and `a`, a list of `n` integers representing the amount of water in each of `n` containers. It calculates the average amount of water per container and checks if redistributing the water according to this average would result in any container having less than zero water. If any container ends up with less than zero water during the redistribution process, the function returns 'No'. Otherwise, it returns 'Yes'. The function returns 'No' in Case_1 and 'Yes' in Case_2.

