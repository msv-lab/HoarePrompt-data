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
        
    #State: `t` is an integer such that 1 <= t <= 10^4, `n` is the last input integer, `a` is the last input string, `ans` is the number of non-overlapping occurrences of the substrings 'map' or 'pie' in `a`, and `i` is the length of `a` minus 2 or the index just after the last processed character that was part of a 'map' or 'pie' substring.
#Overall this is what the function does:The function `func` reads an integer `t` from the input, which represents the number of test cases. For each test case, it reads an integer `n` and a string `a` of length `n` from the input. The function then counts the number of non-overlapping occurrences of the substrings 'map' or 'pie' in `a` and prints this count. After processing all test cases, the function does not return any value, but the state of the program is such that `t` is an integer within the range 1 to 10^4, `n` is the last input integer, `a` is the last input string, and `ans` is the number of non-overlapping occurrences of 'map' or 'pie' in the last processed string `a`.

