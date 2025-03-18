#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4. For each test case, n is an integer such that 2 <= n <= 2 * 10^5. The first binary string a_{11} a_{12} ... a_{1n} consists of n characters, each of which is either '0' or '1'. The second binary string a_{21} a_{22} ... a_{2n} also consists of n characters, each of which is either '0' or '1'. The sum of n over all test cases does not exceed 2 * 10^5.
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
        
    #State: For each test case, the output consists of two lines: the first line is the constructed string `ans` and the second line is the length of the longest contiguous segment where `a[j + 1] == b[j]` or `a[j + 1] == '0'` and `b[j] == '1'`.
#Overall this is what the function does:The function processes `t` test cases, each consisting of two binary strings `a` and `b` of length `n`. For each test case, it constructs a new string `ans` by alternating characters from `a` and `b` based on specific conditions, and then determines the length of the longest contiguous segment where `a[j + 1]` equals `b[j]` or `a[j + 1]` is '0' and `b[j]` is '1'. It outputs the constructed string `ans` and the length of this segment for each test case.

