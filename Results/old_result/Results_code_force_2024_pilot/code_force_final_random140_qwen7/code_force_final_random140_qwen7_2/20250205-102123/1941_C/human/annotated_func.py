#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4. For each test case, n is a positive integer such that 1 ≤ n ≤ 10^6, and s is a string of length n consisting of lowercase Latin letters. The sum of n over all test cases does not exceed 10^6.
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
        
    #State: Output State: `a` is the final input string provided by the user; `ans` is the total number of occurrences of the substrings 'map' or 'pie' in `a`, considering every third character; `i` is the index just beyond the last character checked by the loop, which means `i` will be `len(a)` if the last valid substring `a[i-3:i]` is 'map' or 'pie', or `len(a) - 3` otherwise; `num_iterations` is the original input value minus the number of times the loop executed; `s` is the last valid 3-character substring processed during the loop's execution, which will be either 'map', 'pie', or the last possible 3-character substring of `a` if none of 'map' or 'pie' were found.
    #
    #In simpler terms, after all iterations of the loop have finished, `ans` will contain the total count of how many times the substrings 'map' or 'pie' appear in the string `a`, with a step of 3 characters. The variable `i` will be set to the index just beyond the last character processed by the loop. The variable `num_iterations` will reflect the original input value minus the number of times the loop executed. The variable `s` will be the last valid 3-character substring processed during the loop's execution.
#Overall this is what the function does:The function processes a series of test cases, where each test case consists of a string `a` and counts the total number of occurrences of the substrings 'map' or 'pie' within `a`, considering every third character. After processing all test cases, it prints the count for each case and returns nothing.

