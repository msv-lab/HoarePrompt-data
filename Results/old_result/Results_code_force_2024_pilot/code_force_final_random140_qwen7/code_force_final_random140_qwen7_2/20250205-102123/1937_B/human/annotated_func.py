#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, n is an integer such that 2 ≤ n ≤ 2 \cdot 10^5, and two binary strings a_{11}a_{12}…a_{1n} and a_{21}a_{22}…a_{2n} are given, where each a_{ij} is either 0 or 1. The sum of all n values across all test cases does not exceed 2 \cdot 10^5.
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
        
    #State: Output State: The loop has completed all its iterations. Therefore, `counter` will hold the maximum number of consecutive times the condition `a[j + 1] == '0' and b[j] == '1'` was met throughout the entire string `a`. The variable `i` will be equal to the length of `a`, indicating that all characters in `a` have been processed. The variable `work` will remain `False` since the loop exits when `i` reaches the end of `a`. The variable `j` will be equal to `len(a) - 2`, as the loop runs from `0` to `len(a) - 2`. The variable `t` will be decremented to `0`, indicating that all `t` iterations of the outer loop have completed. The strings `ans` will contain the result of the comparisons made during the loop, and `n` will remain unchanged as it was not modified within the loop.
#Overall this is what the function does:The function processes multiple test cases. For each test case, it reads an integer \( t \) (number of test cases), an integer \( n \) (length of binary strings), and two binary strings \( a \) and \( b \). It then constructs a new string \( ans \) by comparing corresponding characters of \( a \) and \( b \) according to specific rules. After constructing \( ans \), it prints the string. Additionally, it counts the maximum number of consecutive times a specific condition (\( a[j + 1] == '0' \) and \( b[j] == '1' \)) is met in the string \( a \) and prints this count. Finally, it ensures all test cases are processed and outputs the results accordingly.

