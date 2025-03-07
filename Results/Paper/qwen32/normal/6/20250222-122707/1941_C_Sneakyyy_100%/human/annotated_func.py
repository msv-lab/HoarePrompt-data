#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4. For each test case, n is an integer such that 1 <= n <= 10^6, and s is a string of length n consisting of lowercase Latin letters. The sum of n over all test cases does not exceed 10^6.
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
        
    #State: t is an integer such that 1 <= t <= 10^4, n is an input integer, a is a string entered by the user, i is the final index such that i < len(a) - 2 after the loop terminates for all test cases, ans is the total number of times 'map' or 'pie' appears in non-overlapping segments of length 3 within the string a for all test cases.
#Overall this is what the function does:The function processes multiple test cases, where each test case consists of an integer `n` and a string `s` of length `n`. For each test case, it counts the number of non-overlapping occurrences of the substrings 'map' and 'pie' within the string `s` and prints this count.

