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
        
    #State: After the loop executes all iterations, the variable `n` must be greater than 0, `s` is a string of length `n` consisting of characters '<' and '>', `A` is a list containing the sum of distances between '>' characters with appropriate multiplicative factors, and `idx_A` is a list containing the indices of all '>' characters in `s`.
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
        
    #State: Output State: `B` is a list where each element is the cumulative sum of distances from the rightmost '>' character to all '<' characters encountered so far, multiplied by the number of '<' characters seen up to that point. `idx_B` is a list containing all the indices of '<' characters in the string `s`. `n` is greater than 0. `s` is a string of length `n` consisting of characters '<' and '>'. `A` is a list containing the sum of distances between '>' characters with appropriate multiplicative factors. `idx_A` is a list containing the indices of all '>' characters in `s`.
    #
    #This means that after the loop has executed all its iterations, `B` will contain the final calculated values based on the positions of '<' characters in `s`, and `idx_B` will hold the indices of all '<' characters found during the loop's execution.
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
        
    #State: i is 3, n must be greater than 0, l is greater than or equal to r, and depending on the value of s[i], l is either increased by 1 or r is decreased by 1.
#Overall this is what the function does:The function `func_1` accepts a string `s` consisting of characters '<' and '>' and returns a sequence of integers. For each character in `s`, it calculates and prints a value based on the balance of '<' and '>' characters up to that point. Specifically, it computes the cumulative sum of distances from the nearest '>' character to all '<' characters (and vice versa) and uses these sums to determine the output value. The function processes the string from both ends, updating indices and sums accordingly, and outputs the calculated values for each character in `s`.

