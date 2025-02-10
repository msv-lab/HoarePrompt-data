#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4. For each test case, n is an integer such that 2 ≤ n ≤ 2 \cdot 10^5, and two binary strings a_{11}a_{12}…a_{1n} and a_{21}a_{22}…a_{2n} are given, where each a_{ij} is either 0 or 1. The sum of all n values across all test cases does not exceed 2 \cdot 10^5.
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
        
    #State: All variables outside the loop remain unchanged. After all iterations, `i` equals `len(a)`, `work` is `False`, `j` equals `len(a) - 1`, `counter` is reset to `1` after each full iteration of `t`, and `ans` is a concatenated string based on the conditions specified in the loop for each iteration.
#Overall this is what the function does:The function processes multiple test cases. For each test case, it reads an integer \( n \) and two binary strings \( a \) and \( b \) of length \( n \). It constructs a new string \( ans \) based on specific conditions involving characters from \( a \) and \( b \). Additionally, it counts the number of positions where \( a \) and \( b \) have consecutive matching '0' or '1' characters, printing both the constructed string \( ans \) and the count. The function prints these results for each test case and does not return any value.

