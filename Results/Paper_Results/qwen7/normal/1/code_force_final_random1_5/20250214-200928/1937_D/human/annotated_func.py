#State of the program right berfore the function call: s is a string of length n (1 ≤ n ≤ 5 ⋅ 10^5), consisting only of characters '<' and '>'.
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
        
    #State: Output State: The output state after the loop executes all the iterations is as follows: `s` is a string of length `n`, `A` is a list containing the cumulative values calculated based on the positions of '>' characters in `s`, and `idx_A` is a list containing the indices of '>' characters in `s`. Specifically, each element in `A` represents the sum of the lengths of all segments between '>' characters up to that point, and each element in `idx_A` contains the indices where '>' characters are found.
    #
    #For example, if `s` is "><>>><", the final states would be:
    #- `A` would be `[0, 1, 3, 6, 9, 11, 15]`
    #- `idx_A` would be `[0, 2, 4, 5, 6]`
    #
    #This means that after processing all characters in `s`, `A` captures the total length of segments between '>' characters cumulatively, and `idx_A` records the positions of all '>' characters in the string.
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
        
    #State: After the loop executes all iterations, `j` will be `n-1`, `i` will be `0`, `idx_B` will contain all indices where `s` has a '<' character from the last to the first, and `B` will be a list where each element is calculated as `B[len(B) - 1] + (idx_B[len(B) - 1] - i) * len(idx_B)` for each iteration.
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
        
    #State: All iterations of the loop have been executed, with `i` equal to `n`, `l` equal to `r + 1` (since `l` will be incremented until it exceeds `r`), and `r` equal to `-1`. The values of `a` and `b` will depend on the final conditions of `l` and `r`.
#Overall this is what the function does:The function processes a string `s` consisting of characters '<' and '>' to calculate and print a series of values. For each character in `s`, if it is '>', it computes a value based on the cumulative lengths of segments between '>' characters and prints it. If the character is '<', it computes a different value based on the cumulative lengths of segments between '<' characters and also prints it. The function does not return any value but modifies the output directly through printing.

