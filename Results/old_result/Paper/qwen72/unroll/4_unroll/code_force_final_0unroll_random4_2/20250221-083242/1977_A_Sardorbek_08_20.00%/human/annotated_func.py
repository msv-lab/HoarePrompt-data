#State of the program right berfore the function call: The function `func` is expected to take two integers, `n` and `m`, as input where 1 ≤ n, m ≤ 100, representing the number of moves and the desired number of cubes in the tower, respectively.
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
        
    #State: The variables `n` and `m` remain unchanged. The loop iterates `a` times, and for each iteration, it reads two integers `b` and `c` from the input. Depending on the values of `b` and `c`, it prints 'YES' if `b == c`, 'NO' if `b < c`, 'Yes' if `a % 2 == b % 2`, and 'No' otherwise. The variables `b`, `c`, and `q` are updated in each iteration, but their final values are not defined as they depend on the last input provided.
#Overall this is what the function does:The function `func` reads an integer `a` from the input, representing the number of test cases. For each test case, it reads two integers `b` and `c` from the input. It then prints 'YES' if `b` is equal to `c`, 'NO' if `b` is less than `c`, 'Yes' if `a % 2` is equal to `b % 2`, and 'No' otherwise. The function does not modify the initial input parameters `n` and `m`, and it does not return any value. After the function concludes, the variables `a`, `b`, `c`, and `q` are in the state they were in after the last iteration of the loop, but their specific final values depend on the last input provided.

