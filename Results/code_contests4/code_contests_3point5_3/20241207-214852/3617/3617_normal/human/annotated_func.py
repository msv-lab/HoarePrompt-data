#State of the program right berfore the function call: **
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
        
    #State of the program after the loop has been executed: The loop will continue to execute until the input from the standard input is empty, at which point the loop will terminate. For each iteration, the loop reads an integer `N` from the input and creates a list `A` containing `N` integers. It then calculates the differences between each element of `A` and its index position, sorts these differences, and calculates the sum of absolute differences to the left and right of each element. These sums are stored in list `m`. The minimum value from `m` is printed in each iteration. After the loop finishes, `line` will contain the last input from the standard input.
#Overall this is what the function does:The function `func_1` reads input from the standard input until empty, where each input contains an integer `N` followed by `N` integers. It calculates the sum of absolute differences to the left and right of each element in the list based on the differences between the elements and their index positions. The minimum sum for each element is printed. The function does not specify a return value.

