#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4; for each test case, n is an integer such that 2 ≤ n ≤ 2⋅10^5 and n is even; each test case consists of two strings of length n, where each character in the strings is either '<' or '>', representing the arrows in the first and second rows of the grid respectively.
def func():
    t = int(input())
    for _ in range(t):
        n = int(input())
        
        a = input()
        
        b = input()
        
        for i in range(1, n, 2):
            if i + 1 < n and a[i] == b[i + 1] == '<' or a[i] == b[i - 1] == '<':
                print('No')
                break
        else:
            print('yes')
        
    #State: Output State: `t` is an integer between 1 and 10^4; for each value of `t`, there is a corresponding `n` and two strings `a` and `b` such that after executing the loop, if for every `n` and corresponding `a`, `b`, the condition `i + 1 < n and a[i] == b[i + 1] == '<'` or `a[i] == b[i - 1] == '<'` is never met for any odd index `i` in the range from 1 to `n-1`, then 'yes' is printed; otherwise, 'No' is printed for that particular `n`, `a`, and `b`.
#Overall this is what the function does:The function processes multiple test cases, each consisting of an integer \( t \) (number of test cases), an integer \( n \) (length of two string arrays), and two strings \( a \) and \( b \) (each of length \( n \), containing only '<' or '>'). For each test case, it checks if it's possible to move from the first row to the second row following the arrows represented by the characters in \( a \) and \( b \) without any conflicts. If a conflict is found, it prints 'No'; otherwise, it prints 'Yes' after checking all test cases.

