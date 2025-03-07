#State of the program right berfore the function call: s is a string of length n (1 ≤ n ≤ 5 ⋅ 10^5), consisting only of the characters '<' and '>'.
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
        
    #State: Output State: The final output state after the loop executes all iterations will be such that `i` is equal to `n-1`, meaning the loop has iterated through all indices of the string `s`. The variable `A` will contain a series of integers where each element is calculated based on the conditions inside the loop. Specifically, each element in `A` will be the sum of the previous element in `A` plus `(current_index - last_index_in_idx_A) * length_of_idx_A` if the current character in `s` is '>', or it will simply be the previous value of `A` if the current character is not '>'. The list `idx_A` will contain all the indices of the string `s` where the character is '>', in the order they appear.
    #
    #In natural language, the output state will be characterized by `i` being equal to the length of the string `s` minus one, `A` being a list of integers calculated according to the rules described above, and `idx_A` being a list of all indices in `s` where the character is '>', in the order they appear.
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
        
    #State: Output State: `i` is equal to `n-1`, `j` is 4, `n` must be greater than 0, `A` is a list of integers, `idx_A` is a list of all indices in `s` where the character is '>', in the order they appear; `B` is a list of integers, `idx_B` is a list of all indices in `s` where the character is '<', in the order they appear, and now `idx_B` contains all the indices `i` where `s[i] == '<'`.
    #
    #This means that after the loop has executed all its iterations, `i` will have reached `n-1` (since it starts from `n-1` and decreases by 1 in each iteration until `j` reaches `n`). The variable `j` will be 4 because the loop runs from `0` to `n-1`. The conditions for `n` being greater than 0 and the lists `A`, `idx_A`, `B`, and `idx_B` remain as described, with `idx_B` containing all indices where the character in `s` is '<'.
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
        
    #State: i is 3, n is greater than 0, l is 3, r is 0, a is 1, b is -1.
#Overall this is what the function does:The function accepts a string `s` consisting only of '<' and '>' characters. It calculates and prints a sequence of values based on the positions of '<' and '>' in the string. Specifically, it first processes the string from left to right to compute and store values in `A` and `idx_A`, and then processes the string from right to left to compute and store values in `B` and `idx_B`. Finally, it iterates through the string again, using the computed values in `A`, `B`, `idx_A`, and `idx_B` to determine and print a series of integers. These integers are derived from the positions and counts of '<' and '>' characters in the string, and their calculations involve arithmetic operations based on the indices and lengths of these characters.

