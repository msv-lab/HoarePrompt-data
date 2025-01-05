#State of the program right berfore the function call: argv is a list of integers with length N where 1 <= N <= 2 * 10^5 and 1 <= argv[i] <= 10^9 for 1 <= i <= N.**
def func_1(argv):
    line = sys.stdin.readline().rstrip('\n')
    while line:
        N = int(line)
        
        A = [int(a) for a in raw_input().rstrip('\n').split(' ')]
        
        diff = sorted([(a - (i + 1)) for i, a in enumerate(A)])
        
        m = []
        
        for i in range(N):
            left = 0
            for j in range(0, i):
                left += abs(diff[j] - diff[i])
            right = 0
            for j in range(i + 1, N):
                right += abs(diff[j] - diff[i])
            m.append(left + right)
        
        print(min(m))
        
        line = sys.stdin.readline().rstrip('\n')
        
    #State of the program after the loop has been executed: The loop will continue to read input from stdin until there is no more input available. For each iteration, the code calculates the minimum value of `m` based on the given conditions and prints it. After all iterations have executed, the loop control variable `line` will be an empty string indicating there is no more input to read.
#Overall this is what the function does:The function `func_1` reads input from stdin until there is no more input available. For each input iteration, it calculates the minimum value of `m` based on the given conditions and prints it. The function accepts a parameter `argv`, which is a list of integers. The length of the list `argv` is between 1 and 2 * 10^5, and each element in the list is between 1 and 10^9. The function does not have any specific output specified.

