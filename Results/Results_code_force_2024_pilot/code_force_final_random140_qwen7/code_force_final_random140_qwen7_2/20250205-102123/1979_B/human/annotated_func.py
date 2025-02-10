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
        
    #State: All iterations of the loop have been executed, meaning `i` is equal to `n`, `cnt` is incremented by 1 for each index `i` where `l1[i]` equals `l2[i]`, and the loop has either continued until all elements were checked or broken if there was a mismatch.
#Overall this is what the function does:The function processes a series of test cases, each containing a positive integer \( t \) (1 ≤ \( t \) ≤ 10^4) and two distinct non-negative integers \( x \) and \( y \) (0 ≤ \( x \), \( y \) ≤ 10^9). For each test case, it converts \( x \) and \( y \) into their binary representations, pads them to the same length, and then counts the number of matching bits from the most significant bit to the least significant bit. Finally, it prints \( 2 \) raised to the power of the count of matching bits.

