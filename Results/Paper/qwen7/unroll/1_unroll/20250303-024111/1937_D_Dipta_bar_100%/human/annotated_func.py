#State of the program right berfore the function call: s is a string of length n consisting of characters '<' and '>', where 1 <= n <= 5 * 10^5.
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
        
    #State: Output State: `s` is a string of length `n` consisting of characters '<' and '>', `A` is a list containing integers where each element represents the cumulative sum of indices greater than the previous one encountered, `idx_A` is a list containing the indices of '>' characters in `s`.
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
        
    #State: Output State: `s` is a string of length `n` consisting of characters '<' and '>', `A` is a list containing integers where each element represents the cumulative sum of indices greater than the previous one encountered, `idx_A` is a list containing the indices of '>' characters in `s`, `B` is a list of integers calculated based on the positions of '<' and '>' characters in `s`, `idx_B` is a list containing the indices of '<' characters in `s`. 
    #
    #In the loop, for each index `i` from `n-1` to `0`, if `s[i]` is '<', we append `0` to `B` if `idx_B` is empty. Otherwise, we calculate `x` as `B[len(B) - 1] + (idx_B[len(B) - 1] - i) * len(idx_B)` and append `x` to `B`. We also append the current index `i` to `idx_B`.
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
                b = b + (idx_B[r - 1] - i) * (l + 1)
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
        
    #State: 13 13 9 7 9
#Overall this is what the function does:The function accepts a string `s` consisting of characters '<' and '>' and calculates and prints the value of a specific expression for each index in the string. The expression is based on the cumulative sums of indices of '>' and '<' characters and their positions. The function does not return any value but prints the calculated values for each index.

