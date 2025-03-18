#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4, representing the number of test cases. For each test case, n is an integer such that 1 ≤ n ≤ 10^6, representing the length of the string s, and s is a string of length n consisting of lowercase Latin letters. The sum of n over all test cases does not exceed 10^6.
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
        
    #State: After the loop has executed all iterations, `_` remains a placeholder, `int(input())` must be greater than 0 (ensured by the constraint 1 ≤ t ≤ 10^4). For each test case, `a` is a string containing the user's input. The variable `i` will be equal to the length of `a` or greater, depending on how many times the condition `s == 'map' or s == 'pie'` was met. The variable `ans` will be the total number of occurrences of the substrings 'map' or 'pie' found in `a`. The variable `s` will be the last valid substring of length 3 processed by the loop, or it may not exist if no valid substring was found.
#Overall this is what the function does:The function reads multiple test cases, where each test case consists of a string `a` of lowercase Latin letters. For each test case, it counts the number of non-overlapping occurrences of the substrings "map" or "pie" in the string `a` and prints this count. The function does not return any value; it only prints the results. After processing all test cases, the function completes, and the program state includes the printed counts for each test case.

