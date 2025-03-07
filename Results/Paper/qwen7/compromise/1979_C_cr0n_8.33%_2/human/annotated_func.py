#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4, and for each test case, n is an integer such that 1 ≤ n ≤ 50. The list k contains n integers such that 2 ≤ k_i ≤ 20.
def func_1():
    N = int(input().strip())
    vals = [int(r) for r in input().strip().split()]
    prod = 1
    for r in vals:
        prod *= r
        
    #State: prod is the product of all elements in the list `vals`.
    vprod = [(prod // r) for r in vals]
    den = prod - sum(vprod)
    if (den <= 0) :
        print(-1)
        #This is printed: -1
        return
        #The program returns None
    #State: `vals` is a list of integers, `prod` is the product of all elements in the list `vals`, `vprod` is a list where each element is the product of all elements in `vals` divided by the corresponding element in `vals`, `den` is `prod - sum(vprod)`, and `den` is greater than 0
    print(' '.join([str(x) for x in vprod]))
    #This is printed: what is printed
#Overall this is what the function does:The function reads two lines of input: the first line contains an integer \(N\), and the second line contains \(N\) space-separated integers. It calculates the product of all integers in the second line, then computes a new list where each element is the product of all elements divided by the corresponding element in the original list. If the denominator (calculated as the product minus the sum of the new list) is less than or equal to zero, it prints \(-1\) and returns. Otherwise, it prints the new list as space-separated integers and returns None.

