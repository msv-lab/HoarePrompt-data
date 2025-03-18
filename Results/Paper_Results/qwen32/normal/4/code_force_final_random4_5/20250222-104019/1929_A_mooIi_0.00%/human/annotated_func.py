#State of the program right berfore the function call: t is an integer such that 1 <= t <= 500. For each test case, n is an integer such that 2 <= n <= 100, and a is a list of n integers where each integer a_i satisfies 1 <= a_i <= 10^9.
def func():
    for _ in range(int(input())):
        n = int(input())
        
        ar = map(str, sorted(list(map(int, input().split()))))
        
        print(' '.join(ar))
        
    #State: `t` is an integer such that 1 <= t <= 500; the loop has executed `t` times, with each iteration involving a new input integer `n` and a list `a` of `n` integers. For each iteration, `ar` is a map object containing sorted string integers from the input list `a`.
#Overall this is what the function does:The function processes multiple test cases, where each test case consists of an integer `n` and a list of `n` integers. For each test case, it sorts the list of integers and prints them in ascending order as a space-separated string.

