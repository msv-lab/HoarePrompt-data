#State of the program right berfore the function call: The function should accept two parameters: an integer t (1 ≤ t ≤ 10^4) representing the number of test cases, and a list of lists, where each inner list contains the trace of a string (the first element of each inner list is an integer n (1 ≤ n ≤ 2·10^5) representing the length of the string, followed by n integers a_1, a_2, ..., a_n (0 ≤ a_i < n) representing the trace). The sum of n over all test cases does not exceed 2·10^5, and it is guaranteed that for each trace, there exists a suitable string s consisting of lowercase Latin letters a-z.
def func():
    a = 'abcdefghijklmnopqrstuvwxyz'
    for t in range(int(input())):
        b = [0] * 26
        
        n = int(input())
        
        s = list(map(int, input().split()))
        
        r = ''
        
        for i in s:
            x = b.index(i)
            r += a[x]
            b[x] += 1
        
        print(r)
        
    #State: The function will print a string `r` for each test case, where `r` is constructed by mapping the trace values in `s` to the corresponding characters in the string `a` (which contains all lowercase Latin letters from 'a' to 'z'). After each test case, the string `r` will be reset to an empty string, and the list `b` will be reset to a list of 26 zeros. The variable `a` remains unchanged as it contains all lowercase Latin letters from 'a' to 'z'.
#Overall this is what the function does:The function accepts an integer `t` representing the number of test cases and, for each test case, reads an integer `n` and a list of integers `s` from standard input. It constructs a string `r` by mapping each integer in `s` to a corresponding character in the alphabet (from 'a' to 'z'), and prints this string to standard output. After processing each test case, the function resets the string `r` and the list `b` (used for mapping) to their initial states. The function does not return any value.

