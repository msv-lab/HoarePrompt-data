#State of the program right berfore the function call: The input consists of multiple test cases. The first line contains a single integer t (1 ≤ t ≤ 100) representing the number of test cases. Each of the next t lines contains two integers n and m (1 ≤ n, m ≤ 100) where n is the number of moves and m is the desired number of cubes in the tower.
def func_1():
    n, m = map(int, input().split())
    if ((n - m) % 2 == 0 and n - m >= 0) :
        print('Yes')
        #This is printed: Yes
    else :
        print('No')
        #This is printed: No
    #State: `n` is the number of moves from the input, `m` is the desired number of cubes in the tower from the input. If the difference between `n` and `m` is even and non-negative, then the current value of `n - m` is even and greater than or equal to 0. Otherwise, either `(n - m) % 2 != 0` or `n - m < 0`.
#Overall this is what the function does:The function reads multiple test cases from the input, where each test case consists of two integers, `n` and `m`. For each test case, it determines if it is possible to achieve exactly `m` cubes in the tower using `n` moves, under the condition that the difference `n - m` is even and non-negative. It prints "Yes" if the condition is met, otherwise "No".

