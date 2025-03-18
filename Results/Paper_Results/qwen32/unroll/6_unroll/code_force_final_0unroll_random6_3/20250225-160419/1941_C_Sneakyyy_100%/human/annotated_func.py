#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each of the t test cases, n is an integer such that 1 ≤ n ≤ 10^6, and s is a string of length n consisting of lowercase Latin letters. The sum of n over all test cases does not exceed 10^6.
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
        
    #State: For each of the t test cases, the variable `ans` holds the count of non-overlapping occurrences of the substrings 'map' or 'pie' in the string `s` of length `n`. The variables `t`, `n`, and `s` retain their initial values as provided in the input, and no other variables are affected outside the loop.
#Overall this is what the function does:The function processes multiple test cases, where each test case consists of a string `s` of length `n`. It counts the number of non-overlapping occurrences of the substrings 'map' or 'pie' in each string and prints this count for each test case.

