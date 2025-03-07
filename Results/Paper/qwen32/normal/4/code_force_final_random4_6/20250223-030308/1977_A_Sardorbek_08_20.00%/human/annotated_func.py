#State of the program right berfore the function call: The input consists of multiple test cases. The first line contains a single integer t (1 ≤ t ≤ 100) representing the number of test cases. Each of the next t lines contains two integers n and m (1 ≤ n, m ≤ 100), where n is the number of moves Nikita can make, and m is the desired number of cubes in the tower after those moves.
def func():
    a = int(input())
    for i in range(a):
        b, c = map(int, input().split())
        
        q = b, c
        
        if b == c:
            print('YES')
        elif b < c:
            print('NO')
        elif a % 2 == b % 2:
            print('Yes')
        else:
            print('No')
        
    #State: `i` is equal to `a`, and `b`, `c`, and `q` hold the values from the last test case. The values of `a` remain unchanged.
#Overall this is what the function does:The function processes multiple test cases, each consisting of two integers `n` and `m`. It determines for each test case whether it is possible to achieve exactly `m` cubes in a tower using `n` moves, and prints 'YES' or 'NO' accordingly.

