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
            elif a[j + 1] == '0' and b[j] == '1':
                counter = 1
            else:
                break
        
        print(counter)
        
    #State: After executing the loop for all iterations, `t` test cases will have been processed. For each test case, two outputs will be printed: the first is a string `ans` constructed based on the characters from strings `a` and `b`, and the second is an integer `counter` representing the number of consecutive positions where `a[j+1]` equals `b[j]` or `a[j+1]` is '0' and `b[j]` is '1'. The values of `t` and `n` will be reduced accordingly, and all other variables will be reset at the start of each new test case.
#Overall this is what the function does:The function processes multiple test cases, each consisting of an integer `t` (number of test cases), an integer `n` (length of binary strings), and two binary strings `a` and `b` of length `n`. For each test case, it constructs a new string `ans` by alternating characters from `a` and `b` under specific conditions. Additionally, it counts the number of consecutive positions where `a[j+1]` equals `b[j]` or `a[j+1]` is '0' and `b[j]` is '1', and prints both `ans` and the count for each test case.

