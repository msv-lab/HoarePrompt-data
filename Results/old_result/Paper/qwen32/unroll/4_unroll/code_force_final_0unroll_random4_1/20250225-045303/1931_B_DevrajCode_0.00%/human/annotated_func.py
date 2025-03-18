#State of the program right berfore the function call: n is an integer such that 1 ≤ n ≤ 2 · 10^5, and a is a list of n integers such that 0 ≤ a_i ≤ 10^9. The sum of a_i is divisible by n.
def func_1(n, a):
    total_water = sum(a)
    if (total_water % n != 0) :
        return 'No'
        #The program returns 'No'
    #State: `n` is an integer such that 1 ≤ n ≤ 2 · 10^5, and `a` is a list of `n` integers such that 0 ≤ a_i ≤ 10^9. The sum of `a_i` is divisible by `n`. `total_water` is the sum of the list `a`, and `total_water % n` equals 0.
    target = total_water // n
    container = 0
    for water in a:
        container += water - target
        
        if container < 0:
            return 'No'
        
    #State: container is 0.
    return 'Yes'
    #The program returns the string 'Yes'
#Overall this is what the function does:The function checks if it is possible to redistribute the water in the list `a` among `n` containers such that each container ends up with the same amount of water, which is the average of the total water. It returns 'Yes' if such redistribution is possible without any container having a negative amount of water at any point during the redistribution; otherwise, it returns 'No'.

