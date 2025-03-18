#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4, n is an integer such that 1 <= n <= 10^6, and s is a string of length n consisting of lowercase Latin letters. The sum of n over all test cases does not exceed 10^6.
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
        
    #State: t is an integer such that 1 <= t <= 10^4, n is an integer such that 1 <= n <= 10^6, and s is a string of length n consisting of lowercase Latin letters. The sum of n over all test cases does not exceed 10^6. For each test case, the loop prints the number of occurrences of the substrings 'map' or 'pie' in the string s.
#Overall this is what the function does:The function `func` processes multiple test cases. For each test case, it reads an integer `n` and a string `s` of length `n` consisting of lowercase Latin letters. It then counts the number of non-overlapping occurrences of the substrings 'map' or 'pie' in `s` and prints this count. The function does not return any value. After the function concludes, the state of the program remains as it was before the function call, except that the counts for each test case have been printed to the console.

