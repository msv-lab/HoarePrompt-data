#State of the program right berfore the function call: t is an integer such that 1 <= t <= 500. For each test case, n is an integer such that 2 <= n <= 100, and the array a contains n integers where each integer a_i satisfies 1 <= a_i <= 10^9.
def func():
    for _ in range(int(input())):
        n = int(input())
        
        ar = map(str, sorted(list(map(int, input().split()))))
        
        print(' '.join(ar))
        
    #State: `t` is an integer such that 1 <= t <= 500, and the loop has executed `t` times. For each of the `t` executions, `n` is an integer such that 2 <= n <= 100, and `ar` is a map object containing the sorted string representations of `n` integers provided in the input. The final output consists of `t` lines, each line being the space-separated sorted string representations of the integers from the corresponding input.
#Overall this is what the function does:The function processes `t` test cases, where each test case consists of an integer `n` and a list of `n` integers. For each test case, it sorts the list of integers in ascending order and prints them as space-separated strings.

