#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4. For each test case, n is an integer such that 2 ≤ n ≤ 2 \cdot 10^5, and two binary strings a_{11}a_{12}…a_{1n} and a_{21}a_{22}…a_{2n} are provided, where each a_{ij} is either 0 or 1. The sum of all n values across all test cases does not exceed 2 \cdot 10^5.
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
        
    #State: Output State: t is an integer between 1 and 10^4 (inclusive), n is an integer between 2 and 2 * 10^5 (inclusive), and after all iterations of the loop, `t` is updated to the value of `int(input())`, `a` and `b` are strings obtained from user input, `ans` is a string constructed during the loop, and `counter` is an integer representing the count of consecutive matching characters between `a` and `b` excluding certain conditions, with the final values determined by the loop's logic.
#Overall this is what the function does:The function processes multiple test cases, each consisting of an integer `t` (number of test cases), an integer `n` (length of binary strings), and two binary strings `a` and `b` of length `n`. For each test case, it constructs a new string `ans` by selectively appending characters from `a` and `b` based on specific conditions. After constructing `ans`, it prints the string and then counts the number of consecutive matching characters between `a` and `b` under certain conditions, printing the count. The function updates the input `t` to the next test case and repeats the process until all test cases are processed.

