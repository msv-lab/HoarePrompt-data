#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4. For each test case, n is a positive integer such that 1 ≤ n ≤ 10^6, and the string s consists of lowercase Latin letters with a total length sum not exceeding 10^6.
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
        
    #State: Output State: t is a positive integer such that 1 ≤ t ≤ 10^4. For each test case, n is a positive integer such that 1 ≤ n ≤ 10^6, and the string s consists of lowercase Latin letters with a total length sum not exceeding 10^6. After executing the loop, ans is an integer representing the number of occurrences of the substrings 'map' or 'pie' in the input string a.
#Overall this is what the function does:The function processes a series of test cases. For each test case, it reads a positive integer `n` and a string `s` consisting of lowercase Latin letters. It then counts and prints the number of non-overlapping occurrences of the substrings 'map' and 'pie' within the string `s`.

