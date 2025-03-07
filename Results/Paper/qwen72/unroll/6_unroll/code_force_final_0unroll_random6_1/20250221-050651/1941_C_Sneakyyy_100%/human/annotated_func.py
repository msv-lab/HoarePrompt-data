#State of the program right berfore the function call: The function should take two parameters: an integer t (1 ≤ t ≤ 10^4) representing the number of test cases, and a list of tuples, each containing an integer n (1 ≤ n ≤ 10^6) and a string s of length n, where s consists of lowercase Latin letters. The sum of n over all test cases does not exceed 10^6.
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
        
    #State: The variable `ans` will contain the number of occurrences of the substrings "map" or "pie" in the input string `a` for each test case, and `i` will be equal to the length of the string `a` for each test case. The loop will print the value of `ans` for each test case.
#Overall this is what the function does:The function reads an integer `t` indicating the number of test cases. For each test case, it reads an integer `n` and a string `s` of length `n` consisting of lowercase Latin letters. It then counts the number of occurrences of the substrings "map" or "pie" in the string `s`. After processing all test cases, it prints the count of these substrings for each test case. The function does not return any value; it only prints the results.

