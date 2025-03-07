#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^3, and for each test case, n is an integer such that 3 ≤ n ≤ 10^5. Additionally, the sum of all n values across all test cases does not exceed 10^5.
def func():
    for i in range(int(input())):
        n = [int(i) for i in input().split()][0]
        
        p = [0] * n
        
        ind = n
        
        for i in range(0, n, 2):
            p[i] = ind
            ind -= 2
        
        ind = 1 + n % 2
        
        for i in range(1, n, 2):
            p[i] = ind
            ind += 2
        
        print(*p)
        
    #State: Output State: The loop runs until `i` reaches the highest odd number less than `n` or `i` equals `n` if `n` is even. After all iterations, `ind` will be `1 + n % 2 + 2 * (number of iterations)`, and `i` will be the highest odd number less than `n` or `n` if `n` is even. The list `p` will contain values such that `p[i]` for even indices is `ind + 2 * (number of iterations / 2)` and for odd indices is `ind + 2 * ((number of iterations + 1) / 2)`.
    #
    #To calculate the exact output state after the loop completes all iterations:
    #- `i` will be the largest odd number less than `n` if `n` is even, otherwise `n-1` if `n` is odd.
    #- `ind` will be `1 + n % 2 + 2 * (number of iterations)`, which simplifies to `1 + n % 2 + n // 2` since the number of iterations is `n // 2` if `n` is even and `(n - 1) // 2` if `n` is odd.
    #- The list `p` will be filled such that for even indices, `p[i] = ind + 2 * (i // 2)`, and for odd indices, `p[i] = ind + 2 * ((i + 1) // 2)`.
    #
    #For example, if `n` is 11:
    #- `i` will be 10 (the largest odd number less than 11).
    #- `ind` will be `1 + 11 % 2 + 11 // 2 = 1 + 1 + 5 = 7`.
    #- The list `p` will be filled as follows:
    #  - `p[0] = 7`
    #  - `p[1] = 9`
    #  - `p[2] = 11`
    #  - `p[3] = 13`
    #  - `p[4] = 15`
    #  - `p[5] = 17`
    #  - `p[6] = 19`
    #  - `p[7] = 21`
    #  - `p[8] = 23`
    #  - `p[9] = 25`
    #  - `p[10] = 27`
    #
    #Therefore, the output state after the loop executes all iterations is:
    #Output State: `i` is 10, `ind` is 7, `n` is 11, `p[0]` is 7, `p[1]` is 9, `p[2]` is 11, `p[3]` is 13, `p[4]` is 15, `p[5]` is 17, `p[6]` is 19, `p[7]` is 21, `p[8]` is 23, `p[9]` is 25, `p[10]` is 27.
#Overall this is what the function does:The function processes multiple test cases, where each test case includes an integer \( n \) (3 ≤ \( n \) ≤ 10^5). For each test case, it constructs and prints a list \( p \) of length \( n \). The elements of \( p \) are filled such that for even indices, \( p[i] = 1 + n \% 2 + 2 \times \text{(number of iterations / 2)} \), and for odd indices, \( p[i] = 1 + n \% 2 + 2 \times \text{((number of iterations + 1) / 2)} \). The function does not return any value but prints the constructed list \( p \) for each test case.

