#State of the program right berfore the function call: The function should take two parameters: an integer t (1 ≤ t ≤ 10^4) representing the number of test cases, and a list of strings s_list where each string s in s_list has a length n (1 ≤ n ≤ 10^6) consisting of lowercase Latin letters. The sum of n over all test cases does not exceed 10^6.
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
        
    #State: After all iterations of the loop, `n` is an input integer greater than 0, `a` is the last input string, `ans` is the total number of occurrences of the substrings 'map' or 'pie' in `a`, and `i` is the final index after the loop has completed, which is `len(a) - 2` or greater.
#Overall this is what the function does:The function reads an integer `t` from the input, representing the number of test cases. For each test case, it reads an integer `n` and a string `a` from the input. It then counts the occurrences of the substrings 'map' or 'pie' in `a`, and prints the count for each test case. The function does not return any value; it only prints the results. After processing all test cases, the final state is that `n` is the last input integer, `a` is the last input string, and `ans` is the count of occurrences of 'map' or 'pie' in the last processed string.

