#State of the program right berfore the function call: The input consists of multiple test cases. The first line contains a single integer t (1 ≤ t ≤ 100) representing the number of test cases. Each of the next t lines contains two integers n and m (1 ≤ n, m ≤ 100), where n is the number of moves Nikita can make and m is the desired number of cubes in the tower.
def func_1():
    n, m = map(int, input().split())
    if ((n - m) % 2 == 0 and n - m >= 0) :
        print('Yes')
        #This is printed: Yes
    else :
        print('No')
        #This is printed: No
    #State: The input consists of multiple test cases. The first line contains a single integer `t` (1 ≤ `t` ≤ 100) representing the number of test cases. Each of the next `t` lines contains two integers `n` and `m` (1 ≤ `n`, `m` ≤ 100), where `n` is the number of moves Nikita can make and `m` is the desired number of cubes in the tower. For each test case, if the difference between `n` and `m` is non-negative and even, the current test case satisfies the condition `(n - m) % 2 == 0 and n - m >= 0`. Otherwise, either `n - m` is not divisible by 2 or `n - m` is less than 0.
#Overall this is what the function does:The function processes multiple test cases, each consisting of two integers `n` and `m`. For each test case, it determines if the difference between `n` and `m` is non-negative and even, printing "Yes" if true and "No" otherwise.

