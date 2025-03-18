#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, n is an even integer such that 2 ≤ n ≤ 2 \cdot 10^5. The first and second lines of each test case contain strings of length n consisting of '<' and '>' characters only. The sum of n over all test cases does not exceed 2 \cdot 10^5.
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
        
    #State: A series of 'No' or 'Yes' responses, one for each test case.
#Overall this is what the function does:The function processes multiple test cases, each consisting of two strings of equal even length containing only '<' and '>' characters. For each test case, it determines if there exists any pair of consecutive positions in the strings where both strings have '<' characters in a specific pattern, and prints 'No' if such a pattern is found; otherwise, it prints 'Yes'.

