#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4. For each test case, n is a positive integer such that 1 ≤ n ≤ 10^6, and s is a string consisting of lowercase Latin letters with length n. The sum of all n across all test cases does not exceed 10^6.
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
        
    #State: Output State: t is a positive integer such that 1 ≤ t ≤ 10^4. For each test case, n is a positive integer such that 1 ≤ n ≤ 10^6, and s is a string consisting of lowercase Latin letters with length n. The sum of all n across all test cases does not exceed 10^6. Additionally, for each test case, ans is an integer representing the number of occurrences of the substrings 'map' or 'pie' in the string a.
#Overall this is what the function does:The function processes multiple test cases, where for each test case, it reads an integer `n`, a string `s` of length `n`, and then counts the number of occurrences of the substrings 'map' or 'pie' in `s`. For each test case, it prints the count of these substrings and does not return any value.

