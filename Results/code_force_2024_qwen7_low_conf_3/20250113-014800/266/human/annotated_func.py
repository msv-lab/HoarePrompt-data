#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4; for each test case, n is an integer such that 2 ≤ n ≤ 2 \cdot 10^5 and n is even; each test case consists of two strings, each of length n, where each character in the strings is either "<" or ">".
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
        
    #State of the program after the  for loop has been executed: `t` is an integer such that \(1 \leq t \leq 10^4\), `n` is an odd integer, `a` and `b` are strings of length `n` consisting of "<" and ">". If the loop completes without breaking, it prints 'yes', otherwise it prints 'No'.
#Overall this is what the function does:The function processes multiple test cases, each consisting of an integer \(t\) (such that \(1 \leq t \leq 10^4\)), an integer \(n\) (such that \(2 \leq n \leq 2 \cdot 10^5\) and \(n\) is even), and two strings \(a\) and \(b\) of length \(n\) where each character is either "<" or ">". For each test case, the function checks if there exists any index \(i\) (where \(1 \leq i < n-1\) and \(i\) is odd) such that \(a[i] = '<'\) and either \(b[i+1] = '<'\) or \(b[i-1] = '<'\). If such an index is found, the function prints 'No' and terminates the current test case. If no such index is found for any test case, the function prints 'Yes'. The function does not handle cases where the strings contain characters other than "<" or ">".

