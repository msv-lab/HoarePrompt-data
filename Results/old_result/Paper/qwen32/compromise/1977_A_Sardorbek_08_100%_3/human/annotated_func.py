#State of the program right berfore the function call: The input consists of multiple test cases. The first line contains an integer t (1 ≤ t ≤ 100) representing the number of test cases. Each of the next t lines contains two integers n and m (1 ≤ n, m ≤ 100), where n is the number of moves Nikita can make and m is the desired number of cubes in the tower.
def func():
    a = int(input())
    for i in range(a):
        b, c = map(int, input().split())
        
        q = b, c
        
        if b == c:
            print('YES')
        elif b < c:
            print('NO')
        elif b % 2 == c % 2:
            print('Yes')
        else:
            print('No')
        
    #State: a series of print statements ('YES', 'NO', 'Yes', or 'No') corresponding to each test case, with variables `a`, `n`, and `m` unchanged in their initial state representation.
#Overall this is what the function does:The function processes multiple test cases, each consisting of two integers `n` and `m`. It determines if it is possible to build a tower with exactly `m` cubes using `n` moves and prints "YES", "NO", "Yes", or "No" based on the conditions specified. The input parameters `n` and `m` remain unchanged after processing each test case.

