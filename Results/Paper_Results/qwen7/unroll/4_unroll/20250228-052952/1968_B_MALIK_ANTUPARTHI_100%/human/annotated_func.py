#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, n and m are integers such that 1 ≤ n, m ≤ 2 ⋅ 10^5. a is a binary string of length n, and b is a binary string of length m. The sum of all n values across all test cases does not exceed 2 ⋅ 10^5, and similarly, the sum of all m values does not exceed 2 ⋅ 10^5.
def func():
    a = int(input())
    for i in range(a):
        b, c = map(int, input().split())
        
        d = input()
        
        e = input()
        
        k = 0
        
        for j in range(b):
            if d[j] in e[k:]:
                k = e[k:].index(d[j]) + 1 + k
                if k == c or j == b - 1:
                    k = j + 1
                    break
            else:
                k = j
                break
        
        print(k)
        
    #State: Output State: t is an integer such that 1 ≤ t ≤ 10^4, a is an integer input from the user, each k is an integer determined by the loop's logic based on the inputs b, c, d, and e for each iteration of the outer loop.
    #
    #The value of `k` for each iteration of the outer loop depends on the specific inputs `b`, `c`, `d`, and `e`. After all iterations of the outer loop have finished, `t` and `a` will retain their initial values, but each `k` will reflect the result of the inner loop's logic for the corresponding `i` in the range of `a`.
#Overall this is what the function does:The function processes multiple test cases, where for each test case, it accepts two integers \( b \) and \( c \), and two binary strings \( d \) and \( e \). It then determines an integer \( k \) based on the logic of finding the first occurrence of \( d \) within \( e \) considering the constraints defined by \( b \) and \( c \). The function prints \( k \) for each test case and retains the initial values of \( t \) and \( a \) after completing all test cases.

