#State of the program right berfore the function call: N is a positive integer such that 1 <= N <= 200000, and A is a list of integers where each A[i] is in the range 1 <= A[i] <= 10^9.
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
        
    #State of the program after the loop has been executed: `line` is an empty string indicating no more input lines to read, `N` is the last positive integer read from input, `m` contains the sum of absolute differences calculated for each index from 0 to `N-1`, and the minimum value of `m` from the last iteration has been printed.
#Overall this is what the function does:The function accepts a positive integer N and a list of integers A of length N. It calculates the sum of absolute differences between the sorted values of A adjusted by their indices, for each index in A. It then prints the minimum of these sums for each line of input until no more lines are available. If multiple lines are provided, the function processes each line separately and computes the respective results.

