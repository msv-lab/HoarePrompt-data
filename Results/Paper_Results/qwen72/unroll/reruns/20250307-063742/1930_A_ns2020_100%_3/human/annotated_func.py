#State of the program right berfore the function call: t is an integer such that 1 <= t <= 5000, n is an integer such that 1 <= n <= 50, and a is a list of 2n integers where each integer a_i satisfies 1 <= a_i <= 10^7.
def func():
    t = int(input())
    while t:
        n = int(input())
        
        A = list(map(int, input().split()))
        
        A.sort()
        
        print(sum(A[::2]))
        
        t = t - 1
        
    #State: The loop has executed `t` times, and for each execution, the sum of the smaller elements in each pair of the sorted list `A` has been printed. The value of `t` is now 0, and the values of `n` and `A` are not defined in the final state because they are re-assigned in each iteration of the loop.
#Overall this is what the function does:The function `func` reads an integer `t` from the input, where `1 <= t <= 5000`. It then enters a loop that runs `t` times. In each iteration of the loop, it reads another integer `n` from the input, where `1 <= n <= 50`, and a list of `2n` integers `A` from the input, where each integer in `A` satisfies `1 <= a_i <= 10^7`. The function sorts the list `A` and prints the sum of the elements at even indices (i.e., the smaller elements in each pair of the sorted list). After `t` iterations, the function completes and the value of `t` is 0. The function does not return any value.

