#State of the program right berfore the function call: The function should take two parameters: an integer t (1 ≤ t ≤ 10^4) representing the number of test cases, and a list of strings s_list where each string s in s_list has a length n (1 ≤ n ≤ 10^6) consisting of lowercase Latin letters. The sum of n over all test cases does not exceed 10^6.
def func():
    for _ in range(int(input())):
        a = int(input())
        
        s = input()
        
        x = s.count('map')
        
        y = s.count('pie')
        
        print(x + y)
        
    #State: The loop will execute t times, and for each test case, it will read an integer a (which is not used in the loop body), a string s, count the occurrences of the substrings 'map' and 'pie' in s, and print the sum of these counts. After all iterations, the initial variables t and s_list will remain unchanged, and the loop will have printed the sum of counts for each test case.
#Overall this is what the function does:The function `func` reads an integer `t` from the input, representing the number of test cases. For each test case, it reads an integer `a` (which is not used), and a string `s`. It counts the occurrences of the substrings 'map' and 'pie' in `s` and prints the sum of these counts. The function does not return any value. After all test cases are processed, the initial variables `t` and `s_list` (if they exist) remain unchanged, and the function will have printed the sum of counts for each test case.

