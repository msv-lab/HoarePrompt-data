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
                k = e.index(d[j]) + 1
                if k == c or j == b - 1:
                    k = j + 1
                    break
            else:
                k = j
                break
        
        print(k)
        
    #State: Output State: `b` is less than or equal to 0, `c` is an integer from the input, `i` is equal to the sum of `a` (the total number of iterations the loop was supposed to run), `k` is set to `a` (since the loop runs `a` times and `k` is updated accordingly in each iteration), `d` is an input string, `e` is an input string, and `j` is `a` (as the loop runs `a` times and `j` reaches `a-1` in the last iteration).
    #
    #Explanation: After the loop completes all its iterations, the variable `b` will be less than or equal to 0 because it gets decremented in each iteration until it reaches 0. The variable `c` remains unchanged as it is not modified within the loop. The variable `i` will be equal to `a`, which is the total number of iterations the loop was supposed to run. The variable `k` will be set to `a` because it is updated in each iteration of the loop and reaches the value of `a` after all iterations. The variables `d` and `e` remain unchanged as they are not modified within the loop. The variable `j` will be equal to `a` since it runs from 0 to `b-1` in each iteration of the outer loop and `b` becomes 0 after `a` iterations.
#Overall this is what the function does:The function processes multiple test cases, where for each test case, it accepts two integers \( n \) and \( m \) (such that \( 1 \leq n, m \leq 2 \cdot 10^5 \)), and two binary strings \( a \) and \( b \) (where \( a \) has length \( n \) and \( b \) has length \( m \)). For each test case, it finds the smallest index \( k \) in string \( b \) where the substring of \( a \) up to the current index matches a substring of \( b \). If no match is found, it prints the length of \( b \). The function returns nothing but prints the result for each test case.

