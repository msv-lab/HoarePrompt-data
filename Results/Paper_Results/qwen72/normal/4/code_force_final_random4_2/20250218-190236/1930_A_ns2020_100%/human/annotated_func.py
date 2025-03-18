#State of the program right berfore the function call: t is an integer such that 1 <= t <= 5000, n is an integer such that 1 <= n <= 50, and a is a list of 2n integers where each integer a_i satisfies 1 <= a_i <= 10^7.
def func():
    t = int(input())
    while t:
        n = int(input())
        
        A = list(map(int, input().split()))
        
        A.sort()
        
        print(sum(A[::2]))
        
        t = t - 1
        
    #State: `t` is 0, 1 <= `n` <= 50, `a` is a list of 2n integers where each integer `a_i` satisfies 1 <= `a_i` <= 10^7.
#Overall this is what the function does:The function `func` reads an integer `t` from the input, where `1 <= t <= 5000`. It then processes `t` test cases. For each test case, it reads an integer `n` (where `1 <= n <= 50`) and a list `A` of `2n` integers (each integer in the list satisfies `1 <= a_i <= 10^7`). The function sorts the list `A` and prints the sum of the elements at even indices. After processing all `t` test cases, the function concludes with `t` being 0. The function does not return any value.

