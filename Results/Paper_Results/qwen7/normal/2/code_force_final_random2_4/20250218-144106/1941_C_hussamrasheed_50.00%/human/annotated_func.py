#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4. For each test case, n is a positive integer such that 1 ≤ n ≤ 10^6, and the string s consists of lowercase Latin letters with a total length sum not exceeding 10^6.
def func():
    t = int(input())
    for i in range(t):
        n = int(input())
        
        s = input()
        
        m = s.count('map')
        
        s = s.replace('map', '')
        
        p = s.count('pie')
        
        print(m + p)
        
    #State: After all iterations of the loop, `t` must be a positive integer, `i` will be equal to `t-1`, `n` will be an input integer for each iteration, `s` will be the string input by the user with all occurrences of 'map' removed for each iteration, `m` will be the number of occurrences of 'map' in the original `s` for each iteration, `p` will be the count of occurrences of 'pie' in the updated `s` for each iteration.
#Overall this is what the function does:The function processes a series of test cases, where for each test case, it reads a positive integer `n` and a string `s`. It then counts the occurrences of the substring 'map' in `s`, removes all instances of 'map' from `s`, counts the occurrences of 'pie' in the modified `s`, and prints the sum of these two counts. This process is repeated for `t` test cases, where `t` is also provided as input.

