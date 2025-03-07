#State of the program right berfore the function call: n is a positive integer, and a is a list of n non-negative integers such that the sum of all elements in a is divisible by n.
def func_1(n, a):
    total_water = sum(a)
    if (total_water % n != 0) :
        return 'No'
        #The program returns 'No'
    #State: `total_water` is the sum of all elements in `a`, and `n` is a positive integer, and `a` is a list of `n` non-negative integers such that the sum of all elements in `a` is divisible by `n`, and `total_water % n == 0`
    target = total_water // n
    container = 0
    for water in a:
        container += water - target
        
        if container < 0:
            return 'No'
        
    #State: Output State: `total_water` is the sum of all elements in `a`, `n` is a positive integer, `a` is a list of `n` non-negative integers such that the sum of all elements in `a` is divisible by `n`, `target` is `total_water // n`, and `container` is 0 or a negative number if any `water - target` makes the `container` less than 0 during the loop execution. If at any point `container` becomes less than 0, the function returns 'No'. Otherwise, `container` remains 0.
    return 'Yes'
    #The program returns 'Yes'
#Overall this is what the function does:The function accepts two parameters: `n`, a positive integer, and `a`, a list of `n` non-negative integers where the sum of all elements in `a` is divisible by `n`. It calculates the target amount of water each element should have (`total_water // n`). Then, it iterates through the list `a`, adjusting a cumulative difference (`container`) between the current element and the target. If at any point the cumulative difference becomes negative, the function returns 'No'. If the cumulative difference never goes negative, the function returns 'Yes'.

