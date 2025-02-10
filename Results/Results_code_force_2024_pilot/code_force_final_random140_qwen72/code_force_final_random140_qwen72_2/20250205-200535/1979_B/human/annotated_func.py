#State of the program right berfore the function call: x and y are distinct non-negative integers such that 0 ≤ x, y ≤ 10^9.
def func():
    t = int(input())
    for _ in range(t):
        x, y = map(int, input().split())
        
        l1, l2 = [], []
        
        while x:
            l1.append(x % 2)
            x //= 2
        
        while y:
            l2.append(y % 2)
            y //= 2
        
        if len(l2) < len(l1):
            l2.append(0)
        elif len(l1) < len(l2):
            l1.append(0)
        
        n = len(l1)
        
        if len(l2) < len(l1):
            n = len(l2)
        
        cnt = 0
        
        for i in range(n):
            if l1[i] == l2[i]:
                cnt += 1
            else:
                break
        
        print(2 ** cnt)
        
    #State: After the loop executes all iterations, `x` and `y` are both 0, `t` is 0 (indicating that the loop has completed its specified number of iterations), `_` is a placeholder and not explicitly set, `l1` and `l2` are lists containing the binary representations of the last `x` and `y` inputs in reverse order, respectively, with equal lengths. The variable `n` is the length of `l1`, and `cnt` is the number of leading matching bits between `l1` and `l2` up to the point where they differ or until the end of the shorter list, whichever comes first.
#Overall this is what the function does:The function reads an integer `t` indicating the number of test cases. For each test case, it reads two non-negative integers `x` and `y` (0 ≤ x, y ≤ 10^9). It then computes the number of leading matching bits in the binary representations of `x` and `y`. Finally, it prints 2 raised to the power of the count of these leading matching bits. After processing all test cases, the function completes, and the variables `x` and `y` are both 0, `t` is 0, and the lists `l1` and `l2` contain the binary representations of the last `x` and `y` inputs in reverse order, respectively, with equal lengths. The variable `n` is the length of these lists, and `cnt` is the number of leading matching bits.

