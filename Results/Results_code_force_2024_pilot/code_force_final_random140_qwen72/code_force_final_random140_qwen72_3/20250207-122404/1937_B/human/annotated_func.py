#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4, representing the number of test cases. For each test case, n is an integer such that 2 ≤ n ≤ 2 × 10^5, and a_{11}a_{12}...a_{1n} and a_{21}a_{22}...a_{2n} are binary strings of length n, where each character is either '0' or '1'. The sum of n over all test cases does not exceed 2 × 10^5.
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
        
    #State: After the loop executes all iterations, `t` is 0 (since it represents the number of remaining test cases to process, and all have been processed). For each test case, `n` is the input integer, `a` and `b` are the stripped input strings, `i` is `len(a)`, `work` is either True or False depending on the final iteration's conditions, `ans` is the final concatenated string based on the conditions within the loop, `j` is `len(a) - 2`, and `counter` is the final count based on the conditions inside the loop.
#Overall this is what the function does:The function reads multiple test cases, each consisting of two binary strings of equal length. For each test case, it constructs a new string by alternating characters from the two input strings based on specific conditions. It then prints this constructed string. Additionally, it calculates and prints a counter value based on the comparison of consecutive characters between the two input strings. After processing all test cases, the function completes without returning any value, leaving the input variables `t`, `n`, `a`, `b`, `i`, `work`, `ans`, `j`, and `counter` in their final states as described in the postconditions.

