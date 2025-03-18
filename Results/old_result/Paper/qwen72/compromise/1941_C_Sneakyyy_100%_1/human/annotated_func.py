#State of the program right berfore the function call: The function should take two parameters: an integer t (1 ≤ t ≤ 10^4) representing the number of test cases, and a list of strings s where each string s[i] has a length n (1 ≤ n ≤ 10^6) and consists of lowercase Latin letters. The sum of all n values across all test cases does not exceed 10^6.
def func():
    for _ in range(int(input())):
        n = int(input())
        
        a = input()
        
        ans = 0
        
        i = 0
        
        while i < len(a) - 2:
            s = a[i:i + 3]
            if s == 'map' or s == 'pie':
                i += 3
                ans += 1
            else:
                i += 1
        
        print(ans)
        
    #State: The loop has completed all iterations. For each test case, `ans` is the number of non-overlapping occurrences of the substrings 'map' or 'pie' in the corresponding input string `a`. The variable `i` is the length of the last processed string `a` minus 2 or greater. The loop has processed `t` test cases, where `t` is the initial number of test cases provided.
#Overall this is what the function does:The function processes a series of test cases, where each test case consists of a string. It counts the number of non-overlapping occurrences of the substrings 'map' or 'pie' in each string and prints the count for each test case. The function does not return any value; it only prints the results. After the function concludes, the input has been fully processed, and the counts for all test cases have been printed.

