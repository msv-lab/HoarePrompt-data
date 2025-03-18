#State of the program right berfore the function call: The input consists of an integer t (1 ≤ t ≤ 100) representing the number of test cases. Each of the next t lines contains two integers n and m (1 ≤ n, m ≤ 100) representing the number of moves and the desired number of cubes in the tower, respectively.
def func_1():
    n, m = map(int, input().split())
    if (n >= m) :
        print('Yes')
        #This is printed: Yes
    else :
        print('No')
        #This is printed: No
    #State: `n` and `m` are integers where `n` represents the number of moves and `m` represents the desired number of cubes in the tower. If `n` is greater than or equal to `m`, then `n` is greater than or equal to `m`. Otherwise, `n` is less than `m`.
#Overall this is what the function does:The function reads an integer `t` representing the number of test cases. For each test case, it reads two integers `n` and `m`, where `n` is the number of moves and `m` is the desired number of cubes in the tower. It then prints "Yes" if `n` is greater than or equal to `m`, otherwise it prints "No".

