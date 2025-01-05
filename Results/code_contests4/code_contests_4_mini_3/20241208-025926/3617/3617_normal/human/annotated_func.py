#State of the program right berfore the function call: N is a positive integer such that 1 <= N <= 200000, and A is a list of N integers where each integer A_i satisfies 1 <= A_i <= 10^9.
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
        
    #State of the program after the loop has been executed: `line` is an empty string, `N` is an integer representing the last input value, `A` is a list of integers corresponding to the last input, `diff` is a sorted list of differences based on the last input list `A`, `m` is a list containing the sum of absolute differences for each index from 0 to N-1 with respect to the sorted list `diff`, the minimum value of `m` is printed.
#Overall this is what the function does:The function accepts a positive integer N (1 <= N <= 200000) and a list A of N integers (1 <= A_i <= 10^9). It calculates the sorted differences between each element in A and its 1-based index, computes the sum of absolute differences for each index in the sorted differences list, and prints the minimum sum of these differences. The function continues processing until there are no more lines of input.

