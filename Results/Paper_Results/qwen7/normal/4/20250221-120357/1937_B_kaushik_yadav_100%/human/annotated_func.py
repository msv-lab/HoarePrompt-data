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
        
    #State: Output State: `i` is the length of string `a`, `ans` is the final concatenated string formed according to the given conditions, `counter` is the total count of consecutive matching characters between `a` and `b` (or the reset value if specific conditions are met), `j` is `len(a) - 1`, `work` is `False`, `t` is the initial value provided by the user, `a` is the final input string after all iterations, and `b` is the final input string after all iterations.
    #
    #Explanation: After all iterations of the loop have finished, the variable `i` will be the length of the final string `a` since it is not modified within the loop. The variable `ans` will contain the final concatenated string based on the conditions specified in the loop. The variable `counter` will hold the total count of consecutive matching characters between `a` and `b` (or the reset value if specific conditions are met). The variable `j` will be `len(a) - 1` because the loop increments `j` until it reaches the second last character of `a`. The variable `work` will be `False` because the loop exits when the condition `a[j + 1] != b[j]` and `a[j + 1] != '0'` or `b[j] != '1'` is met. The variables `t`, `a`, and `b` will retain their final values after all inputs have been processed.
#Overall this is what the function does:The function processes multiple test cases, where for each test case, it reads an integer `t` (number of test cases), an integer `n` (length of binary strings), and two binary strings `a` and `b` of length `n`. For each test case, it constructs a new string `ans` based on certain conditions comparing characters from `a` and `b`. Specifically, if the current character in `a` is greater than the next character in `a` and less than the corresponding character in `b`, it appends the character from `a`; otherwise, it appends the character from `b`. After constructing `ans`, it prints `ans` and then counts the number of consecutive matching characters between `a` and `b`, printing this count as well. The function ultimately outputs the constructed string `ans` and the count of consecutive matching characters for each test case.

