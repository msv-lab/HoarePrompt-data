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
        
    #State of the program after the loop has been executed: k is an integer such that k <= 0, n is an integer such that the length of str(n) is at least |k| + 1.
#Overall this is what the function does:The function processes an integer `k` (where \(1 \leq k \leq 10^{12}\)) and returns the \((k+1)\)-th character of the smallest integer whose length is at least \(|k|\). If \(k\) is greater than the length of any integer encountered, the function adjusts \(k\) accordingly until it finds a suitable integer. The final state of the program is such that \(k \leq 0\) and \(n\) is the smallest integer whose length is at least \(|k| + 1\), with the character at index \(k\) printed. Potential edge cases include when \(k\) is zero or negative, where the function ensures \(k\) becomes non-positive and prints the first character of the smallest integer whose length is at least \(|k| + 1\).

