#State of the program right berfore the function call: n is a positive integer, and a is a list of non-negative integers of length n such that the sum of all elements in a is divisible by n.
def func_1(n, a):
    total_water = sum(a)
    if (total_water % n != 0) :
        return 'No'
        #The program returns 'No'
    #State: `total_water` is the sum of all elements in `a`, `n` is a positive integer, and `a` is a list of non-negative integers of length `n` such that the sum of all elements in `a` is divisible by `n`, and `total_water % n == 0`
    target = total_water // n
    container = 0
    for water in a:
        container += water - target
        
        if container < 0:
            return 'No'
        
    #State: Output State: `container` is the sum of all elements in `a` minus `n` times `target`, `total_water` is the sum of all elements in `a`, `n` is a positive integer, `target` is `total_water // n`.
    #
    #In natural language, after the loop executes all its iterations, the `container` variable will hold the value of the total water (sum of all elements in `a`) minus `n` times the target value (`total_water // n`). The `total_water` remains unchanged as it is the sum of all elements in `a`, and `n` and `target` also remain unchanged as they are not modified within the loop.
    return 'Yes'
    #The program returns 'Yes'
#Overall this is what the function does:The function accepts two parameters: `n`, a positive integer, and `a`, a list of non-negative integers of length `n` such that the sum of all elements in `a` is divisible by `n`. It calculates the target amount of water each element in `a` should have by dividing the total sum of `a` by `n`. Then, it iterates through the list `a`, adjusting a `container` variable which tracks the difference between the current sum and `n` times the target. If at any point the `container` becomes negative, the function returns 'No'. If the loop completes without the `container` becoming negative, the function returns 'Yes'.

