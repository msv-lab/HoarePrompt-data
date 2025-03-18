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
        
    #State: All variables outside the loop remain unchanged. `i` is equal to the sum of `a` and the total number of iterations the loop executed, `b` is the last value input by the user, `c` is the last value input by the user, `d` is the last input string, and `e` is the last input string. `j` is equal to `b`, and `k` is either `b` or the position in string `e` where `d[b-1]` is found plus one, provided that either `k` equals `c` or `j` equals `b - 1`. If neither condition is met, `k` is set to `b`.
#Overall this is what the function does:The function processes multiple test cases, where for each test case, it accepts two integers \( n \) and \( m \) (with \( 1 \leq n, m \leq 2 \cdot 10^5 \)), and two binary strings \( a \) and \( b \) (of lengths \( n \) and \( m \) respectively). For each character in string \( a \), it finds the position in string \( b \) where the character first appears, and returns the position of the last character of \( a \) in \( b \) or the position where the character would appear if it were not found, ensuring the returned value is within the bounds of \( b \).

