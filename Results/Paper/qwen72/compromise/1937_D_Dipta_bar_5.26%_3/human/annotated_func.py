#State of the program right berfore the function call: s is a string consisting of characters '<' and '>', and its length n is a positive integer such that 1 <= n <= 5 * 10^5.
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
        
    #State: `A` is a list containing the cumulative counts of '>' characters from the start of the string `s` up to each position where a '>' character is found, and `idx_A` is a list containing the indices of all '>' characters in the string `s`. The length of `A` and `idx_A` is equal to the number of '>' characters in `s`.
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
        
    #State: `A` remains unchanged, `idx_A` remains unchanged, `B` is `[0, 1]`, `idx_B` is `[5, 4]`.
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
        
    #State: `A` remains unchanged, `idx_A` remains unchanged, `B` is `[0, 1]`, `idx_B` is `[5, 4]`, `l` is the number of `>` characters in `s`, `r` is `2 -` the number of `<` characters in `s`.
#Overall this is what the function does:The function `func_1` accepts a string `s` consisting of characters '<' and '>', and prints a sequence of integers representing the number of balanced pairs of '<' and '>' that can be formed by considering each position in the string. The function does not return any value; instead, it outputs the results directly to the console. After the function concludes, the string `s` remains unchanged, and the lists `A`, `idx_A`, `B`, and `idx_B` contain intermediate values used for the computation, but they are not accessible to the user. The final state of the program is that the sequence of integers has been printed, and the function has completed its execution.

