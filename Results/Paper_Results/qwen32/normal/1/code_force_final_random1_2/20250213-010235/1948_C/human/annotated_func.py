#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, n is an even integer such that 2 ≤ n ≤ 2 · 10^5. The first and second lines of each test case contain strings of length n consisting only of '<' and '>' characters. The sum of n across all test cases does not exceed 2 · 10^5.
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
        
    #State: Yes Yes ... Yes
#Overall this is what the function does:The function processes multiple test cases, each consisting of two strings of equal even length containing only '<' and '>' characters. For each test case, it checks if there exists any position where the character in one string is '<' and the character in the corresponding or adjacent position in the other string is also '<'. If such a position is found, it outputs 'No'; otherwise, it outputs 'Yes'.

