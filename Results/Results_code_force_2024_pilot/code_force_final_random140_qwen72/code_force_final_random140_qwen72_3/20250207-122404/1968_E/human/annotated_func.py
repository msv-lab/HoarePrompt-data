#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 50, and for each of the t test cases, n is an integer such that 2 ≤ n ≤ 10^3.
def func():
    for i in range(0, int(input())):
        n = int(input())
        
        print(1, 1)
        
        print(1, 2)
        
        for i in range(3, n + 2):
            print(i, i)
        
    #State: After all iterations, `i` is equal to the total number of test cases `t` plus the last value of `n` for each test case, and `n` remains unchanged for each test case.
#Overall this is what the function does:The function `func` reads an integer `t` indicating the number of test cases, where 1 ≤ t ≤ 50. For each test case, it reads another integer `n`, where 2 ≤ n ≤ 10^3. It then prints a series of pairs of integers: (1, 1), (1, 2), followed by (i, i) for each `i` from 3 to `n + 1`. The function does not return any value; its primary purpose is to generate and print these pairs for each test case. After the function completes, the input values `t` and `n` for each test case remain unchanged, and the program state reflects the printed output.

