#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4. For each test case, n is a positive integer such that 1 ≤ n ≤ 10^6, and s is a string of length n consisting of lowercase Latin letters. The sum of n over all test cases does not exceed 10^6.
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
        
    #State: Output State: t is a positive integer such that 1 ≤ t ≤ 10^4. For each test case, n is a positive integer such that 1 ≤ n ≤ 10^6, and s is a string of length n consisting of lowercase Latin letters. The sum of n over all test cases does not exceed 10^6. Additionally, ans is an integer representing the number of occurrences of the substrings 'map' or 'pie' in the input string a, after executing the loop for all test cases.
#Overall this is what the function does:The function processes multiple test cases, where each test case consists of a positive integer `t` (1 ≤ t ≤ 10^4), an integer `n` (1 ≤ n ≤ 10^6), and a string `s` of length `n` consisting of lowercase Latin letters. For each test case, it counts the number of occurrences of the substrings 'map' or 'pie' in the input string `s`. After processing all test cases, it prints the count for each test case.

