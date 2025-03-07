#State of the program right berfore the function call: n is an integer such that 1 <= n <= 2 * 10^5, and a is a list of integers of length n where 0 <= a_i <= 10^9. The sum of a_i is divisible by n.
def func_1(n, a):
    total_water = sum(a)
    if (total_water % n != 0) :
        return 'No'
        #The program returns 'No'
    #State: `n` is an integer such that 1 <= n <= 2 * 10^5, and `a` is a list of integers of length `n` where 0 <= `a_i` <= 10^9. The sum of `a_i` is divisible by `n`. `total_water` is the sum of the elements in `a`, and `total_water % n` is equal to 0.
    target = total_water // n
    container = 0
    for water in a:
        container += water - target
        
        if container < 0:
            return 'No'
        
    #State: container is 0.
    return 'Yes'
    #The program returns 'Yes'
#Overall this is what the function does:The function checks if it's possible to redistribute the water in the containers such that each container has the same amount of water, given that the total amount of water is divisible by the number of containers. It returns 'Yes' if redistribution is possible without any container having a negative amount of water at any point during the process; otherwise, it returns 'No'.

