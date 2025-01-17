#State of the program right berfore the function call: t is a positive integer representing the number of test cases, where each test case consists of n (the number of containers) and a list of n integers a_1, a_2, ..., a_n representing the initial amounts of water in each container. It is also guaranteed that the sum of a_i for each test case is divisible by n, and the sum of n across all test cases does not exceed 2 \cdot 10^5.
def func():
    for s in [*open(0)][2::2]:
        a = *map(int, s.split()),
        
        u = sum(a) // len(a)
        
        d = f = 0
        
        for x in a:
            d += x - u
            f |= d
        
        print('YNEOS'[f < 0::2])
        
    #State of the program after the  for loop has been executed: `t` is a positive integer, for each test case, `a` is a list of `n` integers, `u` is the average of the elements in `a`, `d` is the cumulative sum of the differences between each element in `a` and `u`, `f` is the bitwise OR of all values of `d` calculated in each iteration, and the output is 'Y' if `f` is not less than 0, or 'N' if `f` is less than 0.
#Overall this is what the function does:The function processes multiple test cases, each consisting of an integer \( n \) and a list of \( n \) integers representing the initial amounts of water in each container. For each test case, it calculates the average amount of water per container, then computes the cumulative sum of the differences between each container's water amount and the average. It also maintains a bitwise OR of these differences. After processing all test cases, the function prints 'Y' if the bitwise OR of the differences is non-negative, otherwise it prints 'N'. The function reads the number of test cases from standard input, and for each test case, it reads \( n \) and the list of water amounts.

