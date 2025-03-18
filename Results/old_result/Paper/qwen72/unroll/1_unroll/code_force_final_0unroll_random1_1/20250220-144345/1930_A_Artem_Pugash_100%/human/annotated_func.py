#State of the program right berfore the function call: t is an integer such that 1 <= t <= 5000, n is an integer such that 1 <= n <= 50, and a is a list of 2n integers where each integer a_i satisfies 1 <= a_i <= 10^7.
def func():
    for _ in range(int(input())):
        n = int(input())
        
        l = sorted(list(map(int, input().split())))
        
        score = 0
        
        for i in range(0, 2 * n, 2):
            score += l[i]
        
        print(score)
        
    #State: t is an integer such that 1 <= t <= 5000, n is an integer such that 1 <= n <= 50, and a is a list of 2n integers where each integer a_i satisfies 1 <= a_i <= 10^7. The variable `score` is the sum of the smallest n integers from the list `a` for each iteration of the outer loop, and this value is printed for each iteration.
#Overall this is what the function does:The function `func` reads an integer `t` from the input, indicating the number of test cases. For each test case, it reads an integer `n` and a list of 2n integers from the input. It then calculates the sum of the smallest n integers from the list and prints this sum. The function does not return any value; it only prints the calculated sum for each test case. After the function concludes, the input variables `t`, `n`, and the list `a` are no longer relevant, and the program state is unchanged except for the printed output.

