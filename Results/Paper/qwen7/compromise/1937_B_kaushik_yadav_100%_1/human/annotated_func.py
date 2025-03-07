#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4. For each test case, n is an integer such that 2 ≤ n ≤ 2 \cdot 10^5, and two binary strings of length n are provided representing the values of a_{1j} and a_{2j} for 1 ≤ j ≤ n. The sum of all n values across all test cases does not exceed 2 \cdot 10^5.
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
        
    #State: Output State: `counter` is the maximum value it reached during all iterations of the loop, which could be any integer between 1 and the length of `a` (inclusive), depending on the sequence of characters in `a` and `b`. `i` is equal to the length of `a`, indicating that the entire string `a` has been processed. `n` is the initial input integer, `a` is the initial string input, `b` is the second string input, `ans` is the final concatenated string formed by adding characters from `a` and `b` according to the conditions specified within the loop, `work` is a boolean which retains its final value (either True or False) from the last iteration, and `j` is equal to `len(a) - 1`, indicating the last character of `a` was processed.
#Overall this is what the function does:The function processes multiple test cases, each consisting of a positive integer \( t \), an integer \( n \), and two binary strings of length \( n \). For each test case, it constructs a new string \( ans \) by concatenating characters from the two input strings based on specific conditions. After processing all test cases, it prints the constructed string \( ans \) for each case and outputs the maximum consecutive count of matching characters between the two input strings.

