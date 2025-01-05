#State of the program right berfore the function call: N is a positive integer such that 1 <= N <= 200000, and A is a list of N integers where each A_i satisfies 1 <= A_i <= 10^9.
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
        
    #State of the program after the loop has been executed: `line` is an empty string, `N` is a positive integer such that 1 <= `N` <= 200000; `A` is a list of integers containing the values read during the loop iterations; `diff` is a sorted list of differences between elements in `A` and their indices plus one; `m` is a list of size `N` containing the sum of absolute differences for each index `i`; the minimum value of `m` has been printed.
#Overall this is what the function does:The function reads multiple lines of input where each line specifies a positive integer N followed by N integers. For each line, it calculates the minimum sum of absolute differences between the sorted differences of the integers and their respective indices plus one, and prints this minimum value. The function processes until there are no more lines of input. It does not return any value; instead, it prints the results directly.

