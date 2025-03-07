#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4, n is an integer such that 1 ≤ n ≤ 10^6, and s is a string of length n consisting of lowercase Latin letters. The sum of n over all test cases does not exceed 10^6.
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
        
    #State: For each test case, the variable `ans` will hold the number of occurrences of the substrings 'map' or 'pie' in the string `a`. The variable `i` will be equal to the length of the string `a` or one less than the length of the string `a` if the last two characters do not form a valid substring to check. The values of `t` and `n` will remain unchanged. The string `s` will remain unchanged as it is not modified within the loop.
#Overall this is what the function does:The function `func` reads multiple test cases from standard input. For each test case, it reads an integer `n` representing the length of a string `a`, and then reads the string `a` itself. The function counts the number of occurrences of the substrings 'map' or 'pie' in `a` and prints this count. The function does not return any value. After the function concludes, the variable `ans` holds the count of the substrings 'map' or 'pie' for each test case, and the variable `i` will be equal to the length of the string `a` or one less than the length of the string `a` if the last two characters do not form a valid substring to check. The values of `t` and `n` remain unchanged, and the string `s` is not used within the function.

