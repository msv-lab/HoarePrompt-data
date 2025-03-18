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
        
    #State: Output State: The loop has executed all its iterations, meaning `i` is equal to `n`. The variable `n` is the length of the string `s`. The list `A` contains `n` elements, where each element is calculated based on the conditions within the loop. Specifically, each element in `A` represents the cumulative sum of the distances from the last occurrence of '>' up to the current index `i`, adjusted by the length of `idx_A`. The list `idx_A` contains all indices in `s` where the character is '>', and its length is equal to the number of '>' characters in `s`.
    #
    #In simpler terms, after the loop completes all its iterations, `i` will be equal to `n`, `A` will have `n` elements reflecting the described calculation, and `idx_A` will contain all positions in `s` where the character is '>'.
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
        
    #State: After the loop executes all iterations, `n` is the length of the string `s`, `j` is 0, and `i` is `n - 1`. The list `idx_B` contains all indices in `s` where the character is '<', and `B` is a list containing the cumulative sums of the distances from the last occurrence of '>' up to the current index `i`, adjusted by the length of `idx_A`.
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
        
    #State: i is 0, l is n, r is 0.
#Overall this is what the function does:The function `func_1` accepts a string `s` consisting of characters '<' and '>', and calculates and prints a series of values based on the balance of '<' and '>' characters in the string. Specifically, it computes and prints values derived from the cumulative distances of '<' and '>' characters from their last occurrences, adjusting these distances by the count of such characters encountered so far. The function processes the string from both ends, considering the distances in both directions, and outputs the calculated values for each character in the string.

