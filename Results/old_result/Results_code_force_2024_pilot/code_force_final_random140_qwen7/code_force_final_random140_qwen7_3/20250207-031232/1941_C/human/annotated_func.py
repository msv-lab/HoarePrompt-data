#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4. For each test case, n is a positive integer such that 1 ≤ n ≤ 10^6, and s is a string of length n consisting of lowercase Latin letters. The sum of all n across all test cases does not exceed 10^6.
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
        
    #State: Output State: After the loop executes all iterations, `ans` will hold the total count of occurrences of the substrings 'map' and 'pie' in the string `a`. The variable `i` will be set to `len(a) - 2`, indicating that the loop has checked all possible 3-character substrings up to the second-to-last character of the string `a`. The variable `s` will be the last 3-character substring of `a` that was checked during the loop, which could be 'map', 'pie', or any other 3-character substring. The string `a` remains unchanged as it was in the initial state.
#Overall this is what the function does:The function processes multiple test cases, each consisting of a string `s` of length `n` (1 ≤ n ≤ 10^6) containing lowercase Latin letters. For each test case, the function counts and prints the number of occurrences of the substrings 'map' and 'pie'. After processing all test cases, the function prints the count for each case.

