#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. Each test case consists of an integer n such that 1 ≤ n ≤ 10^6, followed by a string s of length n consisting of lowercase Latin letters. The sum of n over all test cases does not exceed 10^6.
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
        
    #State: the count of 'map' and 'pie' substrings in the last processed string `a`.
#Overall this is what the function does:The function processes a series of test cases, where each test case consists of a string of lowercase Latin letters. For each string, it counts the number of non-overlapping occurrences of the substrings 'map' and 'pie', and prints the count for each test case.

