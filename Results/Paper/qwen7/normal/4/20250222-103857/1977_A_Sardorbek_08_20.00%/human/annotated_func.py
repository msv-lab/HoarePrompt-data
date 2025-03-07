#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 100, and each test case consists of two positive integers n and m such that 1 ≤ n, m ≤ 100.
def func():
    a = int(input())
    for i in range(a):
        b, c = map(int, input().split())
        
        q = b, c
        
        if b == c:
            print('YES')
        elif b < c:
            print('NO')
        elif a % 2 == b % 2:
            print('Yes')
        else:
            print('No')
        
    #State: Postcondition: `t` is a positive integer such that 1 ≤ t ≤ 100, `a` is an input integer, `i` is equal to `a`, `b` is an integer obtained from the last input split, `c` is an integer obtained from the second last input split, `q` is a tuple containing (`b`, `c`). The values of `t`, `a`, `i`, `b`, `c`, and `q` remain unchanged regardless of the conditions within the loop.
#Overall this is what the function does:The function processes multiple test cases, each consisting of two positive integers \( n \) and \( m \) (where \( 1 \leq n, m \leq 100 \)), and prints 'YES' if \( n \) equals \( m \), 'NO' if \( n \) is less than \( m \), 'Yes' if both \( n \) and \( m \) have the same parity (both even or both odd), and 'No' otherwise. The function does not return any value but prints the results for each test case.

