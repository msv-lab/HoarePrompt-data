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
        
    #State: A series of integers, each representing the number of occurrences of 'map' or 'pie' in the respective test case's string.
#Overall this is what the function does:The function processes a series of test cases. For each test case, it counts and prints the number of non-overlapping occurrences of the substrings 'map' or 'pie' in a given string of lowercase Latin letters.

