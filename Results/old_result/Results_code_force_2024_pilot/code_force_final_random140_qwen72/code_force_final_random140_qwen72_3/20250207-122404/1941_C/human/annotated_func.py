#State of the program right berfore the function call: t is an integer where 1 ≤ t ≤ 10^4, representing the number of test cases. For each test case, n is an integer where 1 ≤ n ≤ 10^6, representing the length of the string s, and s is a string of length n consisting of lowercase Latin letters. The sum of n over all test cases does not exceed 10^6.
def func():
    for _ in range(int(input())):
        a = input()
        
        ans = 0
        
        i = 0
        
        while i < len(a) - 2:
            s = a[i:i + 3]
            print(s)
            if s == 'map' or s == 'pie':
                i += 3
                ans += 1
            else:
                i += 1
        
        print(ans)
        
    #State: After the loop has executed all iterations, `t` remains an integer where \(1 \leq t \leq 10^4\), `a` is the string representation of the last input, `i` is equal to the length of `a` (since the loop exits when `i` is no longer less than `len(a) - 2`), and `ans` is the total count of occurrences of the substrings 'map' or 'pie' found in `a` during the loop's execution for each test case.
#Overall this is what the function does:The function reads an integer `t` indicating the number of test cases. For each test case, it reads a string `s` and counts the occurrences of the substrings 'map' or 'pie' within `s`. It prints the count for each test case. After processing all test cases, the function does not return any value, but the state includes `t` remaining an integer within the range [1, 10^4], `a` being the last input string, `i` being the length of `a`, and `ans` being the count of 'map' or 'pie' substrings found in `a` for the last test case.

