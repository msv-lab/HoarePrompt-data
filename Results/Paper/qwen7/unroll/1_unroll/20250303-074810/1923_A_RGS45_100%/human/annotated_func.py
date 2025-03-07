#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 1000; for each test case, n is an integer such that 2 ≤ n ≤ 50; the second line of each test case contains n integers a_1, a_2, ..., a_n where each a_i is either 0 or 1, indicating whether the i-th cell is free (0) or contains a chip (1); in each test case, at least one cell contains a chip.
def func():
    t = int(input(''))
    for _ in range(t):
        n = int(input(''))
        
        arr = ''.join(input('').split())
        
        x = arr.find('1')
        
        y = arr[::-1].find('1')
        
        z = arr[x:n - y]
        
        print(z.count('0'))
        
    #State: After running the loop for `t` iterations, the output state will consist of the count of '0's in the substring of `arr` from index `x` to `n-y`, where `x` is the first occurrence of '1' from the left, and `y` is the first occurrence of '1' from the right in the string `arr`.
#Overall this is what the function does:The function processes multiple test cases, each consisting of an integer n and a sequence of n binary digits. For each test case, it finds the first and last positions of '1' in the sequence, extracts the substring between these positions, and counts the number of '0's in this substring. It then prints the count for each test case.

