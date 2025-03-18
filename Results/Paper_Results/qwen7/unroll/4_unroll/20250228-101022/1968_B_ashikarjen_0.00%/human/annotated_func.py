#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, n and m are integers such that 1 ≤ n, m ≤ 2 ⋅ 10^5, and two binary strings a and b are provided where the length of a is n and the length of b is m. The sum of all n values does not exceed 2 ⋅ 10^5, and the sum of all m values does not exceed 2 ⋅ 10^5.
def func_1():
    n, m = map(int, input().split())
    a = input()
    b = input()
    k = 0
    j = 0
    for i in range(n):
        while j < m and b[j] != a[i]:
            j += 1
        
        if j < m:
            k += 1
            j += 1
        else:
            break
        
    #State: Output State: `t` is an integer such that 1 ≤ t ≤ 10^4; `n` is an integer obtained from the first space-separated integer input; `b` is a string obtained from the input; `k` is an integer representing the number of times the condition `b[j] == a[i]` was true for all `i` in `range(n)` and before `j` reached `m`; `j` is an integer representing the position in string `b` after the loop has executed.
    print(k)
    #This is printed: k (where k is the count of occurrences where b[j] == a[i] for all i in range(n) and before j reached m)
#Overall this is what the function does:For each test case, the function reads integers \( n \) and \( m \), and two binary strings \( a \) and \( b \). It then counts the number of positions in string \( b \) where the characters match those in string \( a \) up to the current position in \( a \), without exceeding the length of \( b \). Finally, it prints the total count of such matching positions across all test cases.

