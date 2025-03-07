#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 500, n is an integer such that 2 ≤ n ≤ 100, and a is a list of n integers where 1 ≤ a_i ≤ 10^9.
def func():
    for _ in range(int(input())):
        n = int(input())
        
        ar = map(str, sorted(list(map(int, input().split()))))
        
        print(' '.join(ar))
        
    #State: t is an integer such that 1 ≤ t ≤ 500, n is an integer such that 2 ≤ n ≤ 100, and a is a list of n integers where 1 ≤ a_i ≤ 10^9. The values of t, n, and a remain unchanged, but the loop has printed the sorted list of integers for each iteration.
#Overall this is what the function does:The function `func` does not accept any parameters and does not return any value. It reads an integer `t` from the input, indicating the number of test cases. For each test case, it reads an integer `n` and a list of `n` integers from the input, sorts the list, and prints the sorted list as a space-separated string. The values of `t`, `n`, and the list of integers are not retained after the function completes.

