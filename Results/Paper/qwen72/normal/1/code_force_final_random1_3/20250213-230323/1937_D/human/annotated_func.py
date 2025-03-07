#State of the program right berfore the function call: s is a string of length n (1 ≤ n ≤ 5 · 10^5) consisting of characters '<' and '>'.
def func_1(s):
    n = len(s)
    A = []
    idx_A = []
    for i in range(0, n):
        if s[i] == '>':
            if len(idx_A) == 0:
                A.append(0)
            else:
                x = A[len(A) - 1] + (i - idx_A[len(idx_A) - 1]) * len(idx_A)
                A.append(x)
            idx_A.append(i)
        
    #State: After the loop executes all iterations, `s` remains a string of length `n` (1 ≤ n ≤ 5 · 10^5) consisting of characters '<' and '>', `n` is the length of `s`. The list `A` contains the cumulative counts of '>' characters encountered, adjusted by their positions and the number of previous '>' characters. The list `idx_A` contains the indices of all '>' characters in `s`.
    B = []
    idx_B = []
    for j in range(0, n):
        i = n - 1 - j
        
        if s[i] == '<':
            if len(idx_B) == 0:
                B.append(0)
            else:
                x = B[len(B) - 1] + (idx_B[len(B) - 1] - i) * len(idx_B)
                B.append(x)
            idx_B.append(i)
        
    #State: After the loop executes all iterations, `s` remains a string of length `n` (1 ≤ n ≤ 5 · 10^5) consisting of characters '<' and '>', `n` is the length of `s`. The list `A` contains the cumulative counts of '>' characters encountered, adjusted by their positions and the number of previous '>' characters. The list `idx_A` contains the indices of all '>' characters in `s`. The list `B` contains the cumulative counts of '<' characters encountered from the end of the string, adjusted by their positions and the number of previous '<' characters. The list `idx_B` contains the indices of all '<' characters in `s` in reverse order. The variable `j` is `n`, and the variable `i` is `-1`.
    l = 0
    r = len(B)
    for i in range(0, n):
        if s[i] == '>':
            if l < r:
                a = A[l]
                x = r - (l + 2)
                b = B[r - 1]
                if x >= 0:
                    b = b - B[x]
                    b = b - (idx_B[x] - idx_B[r - 1]) * (x + 1)
                b = (idx_B[r - 1] - i) * (l + 1)
                print(a * 2 + b * 2 + i + 1, end=' ')
            elif r == 0:
                print(n - i, end=' ')
            else:
                a = B[r - 1] + (idx_B[r - 1] - i) * r
                b = A[l - 1]
                if l - r > 0:
                    b = b - A[l - r - 1]
                    b = b - (idx_A[l - 1] - idx_A[l - r - 1]) * (l - r)
                b = b + (i - idx_A[l - 1]) * r
                print(a * 2 + b * 2 + (n - i), end=' ')
            l += 1
        else:
            r -= 1
            if l <= r:
                if l == 0:
                    print(i + 1, end=' ')
                else:
                    a = A[l - 1]
                    a = a + (i - idx_A[l - 1]) * l
                    b = B[r]
                    if r - l >= 0:
                        b = b - B[r - l]
                        b = b - (idx_B[r - l] - i) * (r - l)
                    b = b + (idx_B[r] - i) * l
                    print(a * 2 + b * 2 + i + 1, end=' ')
            elif r == 0:
                print(n - i + (i - idx_A[l - 1]) * 2, end=' ')
            else:
                a = B[r]
                b = A[l - 1]
                if l - r - 1 > 0:
                    b = b - A[l - r - 2]
                    b = b - (idx_A[l - 1] - idx_A[l - r - 2]) * (l - r - 1)
                b = b + (i - idx_A[l - 1]) * (r + 1)
                print(a * 2 + b * 2 + (n - i), end=' ')
        
    #State: After the loop executes all iterations, `i` is `n-1`, `l` is the number of '>' characters in `s`, and `r` is 0. The values of `s`, `n`, `A`, `idx_A`, `B`, and `idx_B` remain unchanged.
#Overall this is what the function does:The function `func_1` takes a string `s` consisting of characters '<' and '>' and calculates the minimum number of swaps required to balance the string. It processes the string to compute cumulative counts of '>' and '<' characters, adjusted by their positions and the number of previous occurrences. The function prints the minimum number of swaps needed for each character position in the string to achieve a balanced state, where no '<' character appears before a '>' character without being matched. The original string `s` and its length `n` remain unchanged throughout the function's execution.

