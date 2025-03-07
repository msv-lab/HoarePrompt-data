#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, n is an integer such that 1 ≤ n ≤ 2 · 10^5, and a is a list of n integers where each integer a_j satisfies 0 ≤ a_j < 2^31. The sum of n over all test cases does not exceed 2 · 10^5.
def func_1(n, a):
    res = 0
    count = {}
    for num in a:
        if num not in count:
            count[num ^ (1 << 31) - 1] = count.get(num ^ (1 << 31) - 1, 0) + 1
            res += 1
        else:
            count[num] -= 1
        
    #State: `res` is the number of unique numbers in `a` after considering the bitwise flipped version of each number, and `count` is a dictionary where each key is a number from `a` or its bitwise flipped version, and the value is the net count of occurrences after the loop.
    return res
    #The program returns `res`, which is the number of unique numbers in `a` after considering the bitwise flipped version of each number.
#Overall this is what the function does:The function `func_1` takes an integer `n` and a list `a` of `n` integers, where each integer is between 0 and 2^31 - 1. It calculates and returns the count of unique numbers in the list `a` after considering each number and its bitwise flipped version.

