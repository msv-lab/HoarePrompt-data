#State of the program right berfore the function call: The input consists of multiple test cases. The first line contains an integer t (1 ≤ t ≤ 10^4) representing the number of test cases. For each test case, the first line contains an integer n (2 ≤ n ≤ 2 · 10^5) representing the length of the grid. The next two lines contain binary strings of length n, representing the top and bottom rows of the grid, respectively. The sum of n over all test cases does not exceed 2 · 10^5.
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
        
    #State: For each test case, the output consists of the constructed string `ans` followed by the count of consecutive matches.
#Overall this is what the function does:The function processes multiple test cases, each consisting of two binary strings of equal length. For each test case, it constructs a new string based on specific rules and prints this string followed by the count of consecutive matching characters starting from the first position of the constructed string.

