#State of the program right berfore the function call: The function should accept two parameters: an integer t (1 \le t \le 10^4) representing the number of test cases, and a list of lists a, where each inner list contains n integers (0 \le a_i < n) representing the trace of a string. Each inner list a corresponds to a test case, and the length n of each trace satisfies (1 \le n \le 2 \cdot 10^5). The sum of n over all test cases does not exceed 2 \cdot 10^5.
def func():
    a = 'abcdefghijklmnopqrstuvwxyz'
    b = [0] * 26
    for t in range(int(input())):
        n = int(input())
        
        s = list(map(int, input().split()))
        
        r = ''
        
        for i in s:
            x = b.index(i)
            r += a[x]
            b[x] += 1
        
        print(r)
        
    #State: The variable `b` will contain the counts of how many times each character in the string `a` was used to construct the output strings `r` for all test cases. The variable `a` remains unchanged as 'abcdefghijklmnopqrstuvwxyz'. The loop will print the constructed string `r` for each test case.
#Overall this is what the function does:The function `func` accepts no parameters and reads input from the standard input. It processes `t` test cases, where `t` is an integer provided by the user. For each test case, it reads an integer `n` and a list of integers `s`. The function constructs a string `r` by mapping each integer in `s` to a character in the alphabet (from 'a' to 'z') based on the current count of each character stored in the list `b`. The constructed string `r` is printed for each test case. After processing all test cases, the list `b` contains the counts of how many times each character in the alphabet was used to construct the output strings, and the string `a` remains unchanged as 'abcdefghijklmnopqrstuvwxyz'. The function does not return any value.

