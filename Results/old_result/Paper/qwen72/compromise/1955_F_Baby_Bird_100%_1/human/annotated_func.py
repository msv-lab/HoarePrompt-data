#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4, and each of the four integers p_i in the test cases is an integer such that 0 <= p_i <= 200.
def func():
    print('\n'.join([str(sum(3 * (x // 2) + x % 2 * (i < 3) for i, x in
    enumerate(map(int, input().split()))) // 3) for _ in range(int(input()))]))
    #This is printed: 22
    #12
#Overall this is what the function does:The function `func` processes a series of test cases. Each test case consists of four integers `p_i` (0 <= p_i <= 200). The function reads the number of test cases `t` (1 <= t <= 10,000) from user input and then, for each test case, reads four integers from user input. It computes a value based on these integers and prints the result for each test case. The final state of the program after the function concludes is that `t` test cases have been processed, and the computed results have been printed to the console.

