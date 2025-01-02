#State of the program right berfore the function call: t is a positive integer (1 ≤ t ≤ 100), and for each of the t test cases, a, b, and c are strings of lowercase English letters of the same length (1 ≤ length ≤ 100).
def func():
    num = int(raw_input())
    for i in range(num):
        a = raw_input()
        
        b = raw_input()
        
        c = raw_input()
        
        f = 0
        
        for j in range(len(a)):
            if b[j] != c[j] and a[j] != c[j]:
                f = 1
                break
        
        if f == 0:
            print('YES')
        else:
            print('NO')
        
    #State of the program after the  for loop has been executed: `t` is a positive integer (1 ≤ t ≤ 100), `a`, `b`, and `c` are the last input strings of lowercase English letters of the same length (1 ≤ length ≤ 100), `num` is the input integer, `i` is `num - 1` (indicating the loop has completed `num` iterations), `j` is the last index of `a` if the inner loop completes without breaking or the index where `b[j] != c[j] and a[j] != c[j]` was met if the inner loop breaks. For each iteration of the outer loop, if `f` is 0, it indicates that there does not exist an index `j` such that `b[j] != c[j] and a[j] != c[j]`, and 'YES' is printed to the console. If `f` is 1, it indicates that there exists an index `j` such that `b[j] != c[j] and a[j] != c[j]`, and 'NO' is printed to the console.
#Overall this is what the function does:The function reads a positive integer `t` (1 ≤ t ≤ 100) indicating the number of test cases. For each test case, it reads three strings `a`, `b`, and `c` of lowercase English letters, all of the same length (1 ≤ length ≤ 100). The function then checks for each test case if there exists an index `j` such that both `b[j]` and `a[j]` are different from `c[j]`. If no such index exists, it prints 'YES'; otherwise, it prints 'NO'. After processing all `t` test cases, the function terminates. The final state of the program includes `t` being a positive integer, `a`, `b`, and `c` being the last input strings for the final test case, and the variable `num` holding the value of `t`. The variables `i` and `j` are also present, with `i` being `num - 1` and `j` being the last index checked or the index where the condition failed, depending on the test case.

