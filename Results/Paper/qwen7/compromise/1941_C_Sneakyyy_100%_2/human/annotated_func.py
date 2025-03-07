#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4. For each test case, n is a positive integer such that 1 ≤ n ≤ 10^6, and the string s consists of lowercase Latin letters with length n. The sum of all n across all test cases does not exceed 10^6.
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
        
    #State: `ans` is the total number of occurrences of the substrings 'map' or 'pie' in the string `a`, `i` is equal to `len(a)`, and `s` is the last possible substring of `a` of length 3, which could be 'map' or 'pie', or does not exist if no such substrings were found throughout the iterations.
#Overall this is what the function does:The function processes multiple test cases, where each test case consists of a positive integer `t` (1 ≤ t ≤ 10^4) and a string `s` of lowercase Latin letters with length `n` (1 ≤ n ≤ 10^6). For each test case, it counts and prints the total number of non-overlapping occurrences of the substrings 'map' or 'pie' within the string `s`. After processing all test cases, it prints the count for each case.

