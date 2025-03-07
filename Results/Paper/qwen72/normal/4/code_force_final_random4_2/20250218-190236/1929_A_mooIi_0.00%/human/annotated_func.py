#State of the program right berfore the function call: t is an integer where 1 <= t <= 500, n is an integer where 2 <= n <= 100, and a is a list of n integers where 1 <= a_i <= 10^9 for each i from 1 to n.
def func():
    for _ in range(int(input())):
        n = int(input())
        
        ar = map(str, sorted(list(map(int, input().split()))))
        
        print(' '.join(ar))
        
    #State: `t` is an integer where 1 <= t <= 500, `n` is an input integer greater than 0, `a` is a list of n integers where 1 <= a_i <= 10^9 for each i from 1 to n, `_` is `t-1`, `ar` is a map object containing the string representations of the sorted integers from the input, `t` must be greater than or equal to the number of iterations completed.
#Overall this is what the function does:The function `func` reads an integer `t` from the input, where `1 <= t <= 500`, and then for each of the `t` test cases, it reads an integer `n` (where `2 <= n <= 100`) and a list of `n` integers. It sorts the list of integers, converts each integer to a string, and prints the sorted list as a space-separated string. The function does not return any value. After the function concludes, `t` test cases have been processed, and the final state of the program is that `t` is an integer where `1 <= t <= 500`, `n` is the last input integer greater than 0, and `ar` is a map object containing the string representations of the sorted integers from the last input list.

