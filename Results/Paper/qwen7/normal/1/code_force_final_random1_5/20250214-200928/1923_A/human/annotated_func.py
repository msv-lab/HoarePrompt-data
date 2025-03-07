#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 1000. For each test case, n is an integer such that 2 ≤ n ≤ 50, and the second line contains a list of n integers a_1, a_2, ..., a_n where each a_i is either 0 or 1. Additionally, in each test case, at least one cell contains a chip.
def func():
    t = int(input(''))
    for _ in range(t):
        n = int(input(''))
        
        arr = ''.join(input('').split())
        
        x = arr.find('1')
        
        y = arr[::-1].find('1')
        
        z = arr[x:n - y]
        
        print(z.count('0'))
        
    #State: Output State: The value of `t` is an integer such that 1 ≤ t ≤ 1000; `n` is the integer input by the user for each iteration; `arr` is the string obtained by joining the input string split by spaces for each iteration; `x` is the index of the first occurrence of '1' in `arr` for the last iteration; `y` is the index of the first occurrence of '1' in `arr[::-1]` for the last iteration; `z` is a substring of `arr` starting from index `x` and ending just before the index `n - y` for the last iteration; `_` is `t-1` (indicating the loop has completed `t-1` iterations); `x` is updated to the index of the first occurrence of '1' in `arr` for the last iteration.
    #
    #In simpler terms, after all iterations of the loop have finished, `t` will still be within the range 1 to 1000, `n` will be the integer input for the last iteration, `arr` will be the string for the last iteration, `x` will be the index of the first '1' in `arr` from the last iteration, `y` will be the index of the first '1' from the end in `arr` from the last iteration, `z` will be the substring from `x` to `n-y` from the last iteration, `_` will indicate the loop has run `t-1` times, and `x` will be the index of the first '1' in `arr` from the last iteration.
#Overall this is what the function does:The function processes a series of test cases. For each test case, it reads an integer t (1 ≤ t ≤ 1000), followed by an integer n (2 ≤ n ≤ 50) and a list of n binary values. It then finds the first occurrence of '1' from the start and the end of the binary string, extracts the substring between these occurrences, and counts the number of zeros in this substring. The function prints the count of zeros for each test case and returns nothing.

