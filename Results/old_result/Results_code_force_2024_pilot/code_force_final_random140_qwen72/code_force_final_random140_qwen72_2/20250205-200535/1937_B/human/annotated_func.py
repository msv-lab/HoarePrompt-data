#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4, representing the number of test cases. For each test case, n is an integer such that 2 ≤ n ≤ 2 × 10^5, and a_{11} a_{12} ... a_{1n} and a_{21} a_{22} ... a_{2n} are binary strings of length n, where each character is either '0' or '1'. The sum of n over all test cases does not exceed 2 × 10^5.
def func():
    input = sys.stdin.readline
    t = int(input())
    for _ in range(t):
        n = int(input())
        
        a = input().strip()
        
        b = input().strip()
        
        ans = ''
        
        i = 0
        
        work = True
        
        while i < len(a):
            if work:
                ans += a[i]
                if i + 1 < len(a) and b[i] < a[i + 1]:
                    work = False
                elif i + 1 == len(a):
                    ans += b[i]
                    break
                else:
                    i += 1
            else:
                ans += b[i]
                i += 1
        
        print(ans)
        
        counter = 1
        
        for j in range(len(a) - 1):
            if a[j + 1] == b[j]:
                counter += 1
            if a[j + 1] == '0' and b[j] == '1':
                counter = 1
        
        print(counter)
        
    #State: After the loop executes all the iterations, `t` is 0, `n` is the last input integer processed, `a` is the last input string stripped of leading and trailing whitespace, `b` is the last input string stripped of leading and trailing whitespace, `ans` is the final string that combines characters from `a` and `b` based on the conditions within the loop, `i` is `len(a)`, `work` is `False` if the loop encountered a condition where `b[i] < a[i + 1]` before reaching the end of `a`, otherwise `work` is `True`, `j` is `len(a) - 2`, and `counter` is the final value of `counter` after the loop completes. The final value of `counter` depends on the characters in `a` and `b` and how they match the conditions in the loop.
#Overall this is what the function does:The function processes a series of test cases, each consisting of two binary strings `a` and `b` of equal length. For each test case, it constructs a new string `ans` by interleaving characters from `a` and `b` based on specific conditions. It then prints the constructed string `ans`. Additionally, it calculates and prints a counter value that reflects the number of consecutive matching characters between `a` and `b` under certain conditions. The function does not return any values; it only prints the results for each test case.

