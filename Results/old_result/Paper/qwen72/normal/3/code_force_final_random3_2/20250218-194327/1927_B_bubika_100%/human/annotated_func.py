#State of the program right berfore the function call: The function should accept two parameters: an integer t (1 \le t \le 10^4) representing the number of test cases, and a list of lists, where each inner list contains the integer n (1 \le n \le 2 \cdot 10^5) and a list of n integers a_1, a_2, \dots, a_n (0 \le a_i < n) representing the trace of the string. The sum of n over all test cases does not exceed 2 \cdot 10^5, and it is guaranteed that for each given trace, there exists a suitable string s.
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
        
    #State: The loop will have completed all `t` iterations, and for each test case, `r` will be a string containing characters from `a` at the indices specified by the integers in `s`, repeated according to the number of times each integer appears in `s`. The list `b` will be a list of 26 integers where each index `j` in `b` represents the number of times the integer `j` appeared in `s` for the last test case. The variables `t`, `n`, and `s` will have been reset and re-assigned for each test case, and `i` and `x` will be the last integer in `s` and its corresponding index in `b` for the last test case, respectively.
#Overall this is what the function does:The function `func` reads an integer `t` from input, representing the number of test cases. For each test case, it reads an integer `n` and a list of `n` integers from input. It constructs a string `r` by mapping each integer in the list to a corresponding character in the alphabet and appending it to `r`. The constructed string `r` is printed for each test case. After all test cases are processed, the function does not return any value, but the output consists of `t` strings, each corresponding to a test case. The state of the program after the function concludes includes the completion of all test case iterations, with the final string `r` printed for each test case.

