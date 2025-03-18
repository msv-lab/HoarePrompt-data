#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 100, and for each test case, x and y are integers such that 0 ≤ x, y ≤ 9.
def func():
    x = int(input())
    for i in range(x):
        x, y = list(map(int, input().split()))
        
        if x < y:
            print(x, y)
        else:
            print(y, x)
        
    #State: Output State: The output state will consist of pairs of integers printed based on the comparison of the two numbers provided in each iteration of the loop. Specifically, for each line of input containing two integers \(x\) and \(y\), if \(x < y\), then \(x\) and \(y\) are printed in the order \(x, y\); otherwise, they are printed in the order \(y, x\). The total number of such pairs will be equal to the value of `x`, which is the number of iterations the loop will run.
#Overall this is what the function does:The function reads multiple pairs of integers \(x\) and \(y\) from the user, compares them, and prints the pair in ascending order. Specifically, for each pair, if \(x < y\), it prints \(x, y\); otherwise, it prints \(y, x\). The function does not return any value; its purpose is to process and output the sorted pairs based on the given conditions.

