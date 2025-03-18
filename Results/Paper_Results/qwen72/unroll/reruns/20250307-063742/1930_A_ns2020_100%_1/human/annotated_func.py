#State of the program right berfore the function call: t is an integer where 1 <= t <= 5000, n is an integer where 1 <= n <= 50, and a is a list of 2n integers where 1 <= a_i <= 10^7.
def func():
    t = int(input())
    while t:
        n = int(input())
        
        A = list(map(int, input().split()))
        
        A.sort()
        
        print(sum(A[::2]))
        
        t = t - 1
        
    #State: `t` is 0, `n` is the last input integer where 1 <= n <= 50, and `A` is the last sorted list of 2n integers where 1 <= a_i <= 10^7.
#Overall this is what the function does:The function `func` reads an integer `t` from the input, where `1 <= t <= 5000`. It then processes `t` test cases. For each test case, it reads an integer `n` (where `1 <= n <= 50`) and a list of `2n` integers (each between `1` and `10^7`). The function sorts the list and prints the sum of the elements at even indices. After processing all test cases, the function terminates with `t` being `0`, `n` being the last input integer, and `A` being the last sorted list of `2n` integers. The function does not return any value.

