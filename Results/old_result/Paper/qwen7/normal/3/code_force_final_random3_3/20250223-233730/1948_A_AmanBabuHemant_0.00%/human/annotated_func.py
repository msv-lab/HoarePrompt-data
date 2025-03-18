#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 50, and for each test case, n is an integer such that 1 ≤ n ≤ 50.
def func():
    t = int(input())
    for _ in range(t):
        n = int(input())
        
        if n % 2:
            print('NO')
        else:
            s = '110' * (n // 2)
            if len(s) < 200:
                print('YES')
                print(s)
            else:
                print('NO')
        
    #State: After all iterations of the loop have finished, `t` must be equal to the initial value of `t`, `n` is an integer for each iteration, and if `n` is odd, it remains odd. If `n` is even, it remains even. Additionally, `s` is a string consisting of '110' repeated `n//2` times for each even `n`, with the length of `s` being either less than 200 or 200 or more for each iteration.
#Overall this is what the function does:The function processes multiple test cases, each defined by an integer `n`. For each `n`, it checks if `n` is odd or even. If `n` is odd, it prints 'NO'. If `n` is even and the resulting string `s` (consisting of '110' repeated `n//2` times) has a length less than 200, it prints 'YES' followed by `s`; otherwise, it prints 'NO'. The function ultimately ensures that for each test case, it provides a binary outcome ('YES' or 'NO') based on the conditions specified.

