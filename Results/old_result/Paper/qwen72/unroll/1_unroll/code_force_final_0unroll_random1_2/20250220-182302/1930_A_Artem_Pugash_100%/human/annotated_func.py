#State of the program right berfore the function call: t is an integer where 1 <= t <= 5000, n is an integer where 1 <= n <= 50, and a is a list of 2n integers where 1 <= a_i <= 10^7.
def func():
    for _ in range(int(input())):
        n = int(input())
        
        l = sorted(list(map(int, input().split())))
        
        score = 0
        
        for i in range(0, 2 * n, 2):
            score += l[i]
        
        print(score)
        
    #State: t is an integer where 1 <= t <= 5000, n is an integer where 1 <= n <= 50, and a is a list of 2n integers where 1 <= a_i <= 10^7. The loop has printed the sum of the first, third, fifth, ..., (2n-1)th smallest elements of the list a for each iteration.
#Overall this is what the function does:The function `func` reads an integer `t` indicating the number of test cases. For each test case, it reads an integer `n` and a list of 2n integers. It then calculates the sum of the first, third, fifth, ..., (2n-1)th smallest elements of the list and prints this sum. The function does not return any value. After the function concludes, the input values `t`, `n`, and the list of integers have been consumed, and the specified sums have been printed for each test case.

