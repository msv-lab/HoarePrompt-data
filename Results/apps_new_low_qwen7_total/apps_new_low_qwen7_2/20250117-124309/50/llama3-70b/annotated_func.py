#State of the program right berfore the function call: k is an integer such that 1 <= k <= 10^12.
def func():
    k = int(input())

n = 1
    while True:
        s = str(n)
        
        if len(s) >= k:
            print(s[k - 1])
            break
        
        k -= len(s)
        
        n += 1
        
    #State of the program after the loop has been executed: k is 0, n is 10, s is "10".
#Overall this is what the function does:The function reads an integer `k` from the user, where \(1 \leq k \leq 10^{12}\). It then finds the \((k-1)\)-th character of the smallest integer whose length is at least \(k\). If no such integer exists (which theoretically should not happen given the constraints), the function will eventually find an integer large enough to satisfy the condition. After finding the integer, it prints the \((k-1)\)-th character of that integer and terminates. The function ensures that \(k\) is reduced to 0 after finding the appropriate integer, and \(n\) is set to 10 at the end of the loop.

