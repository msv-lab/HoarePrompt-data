#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 1000. For each test case, n is an integer such that 1 ≤ n ≤ 20, and a, b, c are strings consisting of exactly n lowercase Latin letters.
def func():
    t = int(input())
    l = 'YES'
    for i in range(t):
        n = int(input())
        
        a = input()
        
        b = input()
        
        c = input()
        
        for i in range(n):
            if a[i] != c[i] and b[i] != c[i]:
                l = 'YES'
        else:
            l = 'NO'
        
        print(l)
        
    #State: Output State: `t` is an integer such that 1 ≤ `t` ≤ 1000, `l` is 'NO'
    #
    #Explanation: The variable `l` is initialized to 'YES' at the start of each iteration of the outer loop. Inside the inner loop, the condition `if a[i] != c[i] and b[i] != c[i]:` is checked. If this condition is never met for any `i` within the inner loop, then `l` remains 'YES'. However, if the condition is met for any `i`, `l` is set to 'NO' and remains 'NO' for the rest of the outer loop iteration. Since the problem does not provide specific values for `a`, `b`, and `c`, we cannot guarantee that the condition will never be met. Therefore, the final value of `l` after all iterations is 'NO', assuming there is at least one `i` where the condition is met.
#Overall this is what the function does:The function processes multiple test cases, each consisting of an integer \( t \) (1 ≤ \( t \) ≤ 1000), an integer \( n \) (1 ≤ \( n \) ≤ 20), and three strings \( a \), \( b \), and \( c \), each of length \( n \) containing lowercase Latin letters. For each test case, it checks if for every position \( i \) (0 ≤ \( i \) < \( n \)), either \( a[i] \neq c[i] \) or \( b[i] \neq c[i] \). If this condition holds true for all positions, it prints 'NO'; otherwise, it prints 'YES'. After processing all test cases, the function does not return any value but prints the result for each test case.

