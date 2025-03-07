#State of the program right berfore the function call: t is an integer such that 1 <= t <= 500, n is an integer such that 2 <= n <= 100, and a is a list of n integers where 1 <= a_i <= 10^9.
def func():
    for _ in range(int(input())):
        n = int(input())
        
        ar = map(str, sorted(list(map(int, input().split()))))
        
        print(' '.join(ar))
        
    #State: t is an integer such that 1 <= t <= 500, n is an integer such that 2 <= n <= 100, and a is a list of n integers where 1 <= a_i <= 10^9. The values of t, n, and a remain unchanged, but the loop has printed the sorted list of integers for each iteration of t.
#Overall this is what the function does:The function `func` does not accept any parameters. It reads an integer `t` from the input, which represents the number of test cases. For each test case, it reads an integer `n` and a list of `n` integers from the input, sorts the list in non-decreasing order, and prints the sorted list as a space-separated string. The function does not return any value. After the function concludes, the values of `t`, `n`, and the input lists remain unchanged, but the sorted lists have been printed for each test case.

