#State of the program right berfore the function call: s is a string of length n (1 <= n <= 5 * 10^5), consisting only of the characters '<' and '>'.
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
        
    #State: Output State: The final output state after the loop executes all its iterations will be as follows:
    #
    #- `s` is a string of length `n`.
    #- `i` will be equal to `n` because the loop runs from `0` to `n-1` and increments `i` each time.
    #- `A` will contain the cumulative sum of distances between '>' characters, starting from the last occurrence of '>' in `idx_A` and multiplied by the count of occurrences so far, plus the index difference.
    #- `idx_A` will be a list containing all indices where the character in `s` is '>', in the order they appear in the string.
    #
    #In simpler terms, `A` will store the sum of distances from the last '>' to the current '>', multiplied by the number of '>' seen so far, and `idx_A` will be a list of all indices where `s` has a '>'.
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
        
    #State: Postcondition: `j` is `n-1`, `i` is `0`. `idx_B` is a list containing all indices where `s` has a '<', and `B` is a list where each element is calculated based on the formula `B[len(B) - 1] + (idx_B[len(B) - 1] - i) * len(idx_B)` for each '<' encountered, starting with `0` if `idx_B` is initially empty.
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
        
    #State: i is 3, j is n-1, l is 3, r is 0, B is [0, 6, 18], idx_B is [1, 3, 5], a is 0, b is 0, n is n.
#Overall this is what the function does:The function processes a string `s` consisting only of '<' and '>' characters. It calculates and prints a series of values based on the positions of these characters in the string. Specifically, it computes and outputs a formula involving the cumulative distances between '>' and '<' characters, adjusted by their respective counts and positions. The function does not return any value; instead, it prints the computed values directly.

