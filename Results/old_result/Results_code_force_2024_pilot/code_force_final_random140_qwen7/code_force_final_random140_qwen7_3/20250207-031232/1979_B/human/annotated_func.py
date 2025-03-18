#State of the program right berfore the function call: t is a positive integer such that 1 <= t <= 10^4, and for each test case, x and y are distinct non-negative integers such that 0 <= x, y <= 10^9.
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
        
    #State: The loop has completed all its iterations. The variable `i` is equal to `n-1`, `cnt` is the total number of positions where `l1` and `l2` match from the start up to position `n-1`. The variable `total` is still 0, and the lists `l1` and `l2` are populated with the binary representations of the last input integers `x` and `y` respectively, with any necessary leading zeros added to make their lengths equal.
#Overall this is what the function does:The function processes a series of test cases, where for each case, it takes two distinct non-negative integers \(x\) and \(y\). It converts these integers into their binary representations, ensures both have the same length by padding with leading zeros if necessary, and then counts the number of matching bits from the start of both binary strings. Finally, it prints \(2\) raised to the power of the count of matching bits.

