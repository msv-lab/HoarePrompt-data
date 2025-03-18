#State of the program right berfore the function call: n is an integer such that 1 ≤ n ≤ 2 * 10^5, and a is a list of n integers where each integer a_j satisfies 0 ≤ a_j < 2^31.
def func_1(n, a):
    res = 0
    count = {}
    for num in a:
        if num not in count:
            count[(1 << 31) - 1 ^ num] = count.get((1 << 31) - 1 ^ num, 0) + 1
            res += 1
        else:
            count[num] -= 1
            if count[num] == 0:
                del count[num]
        
    #State: `res` is the number of unique numbers in the list `a` with an odd count, `count` is a dictionary containing the counts of numbers that have not been fully paired.
    return res
    #The program returns `res`, which is the number of unique numbers in the list `a` with an odd count.
#Overall this is what the function does:The function takes an integer `n` and a list `a` of `n` integers, and returns the count of unique numbers in the list `a` that appear an odd number of times.

