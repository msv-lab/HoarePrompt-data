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
        
    #State: After the loop executes all iterations, `i` will be `n-1` (the last index of the string `s`). The lists `A` and `idx_A` will contain elements based on the positions of '>' characters in the string `s`. For each position `i` where `s[i]` is '>', `idx_A` will store the index `i`, and `A` will store the calculated value `x` as defined in the loop. If there are no '>' characters in `s`, both `A` and `idx_A` will remain empty.
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
        
    #State: After the loop executes all iterations, `i` will be `-1`, `A` and `idx_A` will contain elements based on the positions of '>' characters in the string `s`, `B` will contain the calculated values for each position of '<' characters in the string `s`, and `idx_B` will contain the indices of these '<' characters. If there are no '<' characters in `s`, both `B` and `idx_B` will remain empty.
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
        
    #State: After the loop executes all iterations, `i` will be `-1`, `A` and `idx_A` will contain elements based on the positions of '>' characters in the string `s`, `B` will contain the calculated values for each position of '<' characters in the string `s`, and `idx_B` will contain the indices of these '<' characters. If there are no '<' characters in `s`, both `B` and `idx_B` will remain empty. `l` will be the number of '>' characters in `s`, and `r` will be 0.
#Overall this is what the function does:The function `func_1` takes a string `s` as input, where `s` consists only of the characters '<' and '>'. It processes the string to calculate and print a series of integers. Each integer represents a specific calculation based on the positions of '<' and '>' characters in the string. The function does not return any value; instead, it prints the results directly. The final state of the program after the function concludes is that the string `s` remains unchanged, and the lists `A`, `idx_A`, `B`, and `idx_B` contain intermediate values used in the calculations. The printed output is a sequence of integers that reflect the processed state of the string `s`.

