#State of the program right berfore the function call: t is an integer where 1 <= t <= 500, n is an integer where 2 <= n <= 100, and a is a list of n integers where 1 <= a_i <= 10^9.
def func():
    for _ in range(int(input())):
        n = int(input())
        
        ar = map(str, sorted(list(map(int, input().split()))))
        
        print(' '.join(ar))
        
    #State: `_` is `t-1`, `n` is an input integer greater than or equal to 2, `ar` is a map object containing the sorted list of integers from the input, converted to strings.
#Overall this is what the function does:The function `func` reads an integer `t` from the input, where `1 <= t <= 500`, and then for each of the `t` test cases, it reads an integer `n` (where `2 <= n <= 100`) and a list of `n` integers. It sorts these integers in ascending order, converts them to strings, and prints them separated by spaces. The function does not return any value; it only performs the described input and output operations. After the function concludes, the program state is such that `t` test cases have been processed, and the sorted lists of integers for each test case have been printed.

