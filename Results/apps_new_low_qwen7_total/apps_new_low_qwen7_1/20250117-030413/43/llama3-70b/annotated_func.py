#State of the program right berfore the function call: n is an integer such that 1 ≤ n ≤ 40, and s is a string such that 1 ≤ |s| ≤ n, containing only the characters '0' and '1'.
def func():
    n = int(input())

s = input()

count = 0
    for i in range(2 ** n):
        t = bin(i)[2:].zfill(n)
        
        if all(t[i:i + len(s)] == s or t[i + len(s):] + t[:i] == s for i in range(n)):
            count += 1
        
    #State of the program after the  for loop has been executed: `i` is 4095, `n` is an integer such that 1 ≤ n ≤ 40, `t` is a binary representation of `i` with leading zeros to make it length `n`, and `count` is the number of integers `j` in the range `0` to `2^n - 1` (inclusive) such that for every index `i` in the range `0` to `n - 1`, the substring `t[i:i + len(s)]` is equal to `s` or the concatenation of the substring `t[i + len(s):]` and the prefix `t[:i]` is equal to `s`.
    print(count)
#Overall this is what the function does:The function accepts an integer `n` such that \(1 \leq n \leq 40\) and a string `s` containing only '0's and '1's with a length between 1 and `n`. It then checks all possible binary strings of length `n` to see if they contain a specific substring pattern defined by `s`. Specifically, for each binary string, it verifies if either the substring of length `len(s)` starting at index `i` or the concatenation of the substring from index `i + len(s)` to the end and the prefix from the start to index `i` matches `s`. The function counts how many such binary strings satisfy this condition and prints the count. The final state of the program after the function concludes is that the variable `count` contains the total number of valid binary strings, and this count is printed. Potential edge cases include when `n` is at its minimum (1) or maximum (40), and when `s` is very short or very long relative to `n`.

