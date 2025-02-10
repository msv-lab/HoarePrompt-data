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
        
    #State: After the loop executes all iterations, `x` is 0, `y` is 0, `t` is 0, `_` is `t-1`, `l1` and `l2` are lists containing the binary representations of the last `x` and `y` inputs in reverse order, respectively. If the lengths of `l1` and `l2` were unequal, the shorter list was padded with a 0 to match the length of the longer list. `n` is the length of the longer list, `cnt` is the number of matching bits from the start of both lists up to the first differing bit or `n` if all bits matched, and `i` is the index of the first differing bit or `n` if all bits matched.
#Overall this is what the function does:The function reads an integer `t` indicating the number of test cases. For each test case, it reads two non-negative integers `x` and `y`. It then computes the longest common prefix in the binary representation of `x` and `y`, and prints `2` raised to the power of the length of this common prefix. The function does not return any value; it only prints the results. After processing all test cases, the function terminates.

