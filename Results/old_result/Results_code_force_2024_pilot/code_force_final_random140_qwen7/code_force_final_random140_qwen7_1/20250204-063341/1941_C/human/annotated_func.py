#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4. For each test case, n is a positive integer such that 1 ≤ n ≤ 10^6, and the string s consists of lowercase Latin letters and has length n. The sum of all n across all test cases does not exceed 10^6.
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
        
    #State: Output State: The loop will execute until `i` reaches `len(a) - 2`. After all iterations, the following will be true:
    #
    #- `a` remains the original input string.
    #- `t` remains a positive integer such that \(1 \leq t \leq 10^4\).
    #- `ans` is the total count of occurrences where the substring `s` (of length 3) starting from index `i` is either 'map' or 'pie'.
    #- `i` is set to `len(a) - 2` because the loop increments `i` by 1 or 3 each iteration and stops when `i` reaches `len(a) - 2`.
    #
    #In summary, `ans` will contain the total number of times the substrings 'map' or 'pie' appear in the input string `a`, and `i` will be the index just after the last valid substring of length 3 that was checked.
#Overall this is what the function does:The function processes multiple test cases, each containing a string `s` and an integer `t`. It counts the number of times the substrings 'map' or 'pie' appear in the string `s`. The function prints the count for each test case and outputs the total count of these substrings across all test cases. The original string `s` and the integer `t` remain unchanged after processing.

