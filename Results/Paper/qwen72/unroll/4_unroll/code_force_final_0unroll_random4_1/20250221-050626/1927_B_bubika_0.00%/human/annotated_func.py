#State of the program right berfore the function call: The function should take an integer t (1 \le t \le 10^4) representing the number of test cases, and for each test case, it should take an integer n (1 \le n \le 2 \cdot 10^5) representing the length of the lost string, and a list of n integers a_1, a_2, \dots, a_n (0 \le a_i < n) representing the trace of the string. The sum of n over all test cases does not exceed 2 \cdot 10^5, and it is guaranteed that for each given trace, there exists a suitable string s consisting of lowercase Latin letters a-z.
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
        
    #State: For each test case, the loop will output a string `r` of length `n` constructed from the trace `s` by mapping each integer in `s` to a corresponding character in the string `a`. The string `a` will remain unchanged as 'abcdefghijklmnopqrstuvwxyz'. The list `b` will be modified such that each element at index `x` will be incremented by the number of times the integer `x` appears in the trace `s` for the current test case. After all test cases are processed, the final state of `b` will depend on the cumulative frequency of each integer in all traces.
#Overall this is what the function does:The function `func` takes an integer `t` representing the number of test cases. For each test case, it takes an integer `n` and a list of `n` integers `s`. It constructs and prints a string `r` of length `n` by mapping each integer in `s` to a corresponding character in the string `a` ('abcdefghijklmnopqrstuvwxyz'). The string `a` remains unchanged, and the list `b` is modified to reflect the cumulative frequency of each integer in all traces across all test cases. The function does not return any value; it only prints the constructed strings for each test case.

