#State of the program right berfore the function call: n is an integer such that 1 ≤ n ≤ 40, and s is a string such that 1 ≤ |s| ≤ n, containing only the characters '0' and '1'.
def func():
    n = int(input())

s = input()

count = 0
    for i in range(2 ** n):
        t = bin(i)[2:].zfill(n)
        
        if all(t[i:i + len(s)] == s or t[i + len(s):] + t[:i] == s for i in range(n)):
            count += 1
        
    #State of the program after the  for loop has been executed: `count` is the total number of integers `i` from 0 to \(2^n - 1\) such that the binary string representation of `i` of length `n` satisfies the condition that either a substring of length `len(s)` or a circular shift of this substring equals `s`. `n` and `s` remain unchanged.
    print(count)
#Overall this is what the function does:The function `func` accepts two parameters: `n` (an integer such that 1 ≤ n ≤ 40) and `s` (a string such that 1 ≤ |s| ≤ n, containing only the characters '0' and '1'). The function calculates and prints the number of integers `i` from 0 to \(2^n - 1\) such that the binary string representation of `i` of length `n` contains a substring of length `|s|` or a circular shift of this substring equal to `s`. The function does not return a value; instead, it prints the result directly.

