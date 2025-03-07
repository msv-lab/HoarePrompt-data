#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4, and for each test case, n is a positive integer such that 1 ≤ n ≤ 50. The list k contains n positive integers such that 2 ≤ k_i ≤ 20.
def func_1():
    N = int(input().strip())
    vals = [int(r) for r in input().strip().split()]
    prod = 1
    for r in vals:
        prod *= r
        
    #State: `prod` is the product of all elements in the list `vals`, `t` is a positive integer such that \(1 \leq t \leq 10^4\), `N` is an input integer where \(1 \leq N \leq 50\), and `vals` is an empty list.
    vprod = [(prod // r) for r in vals]
    den = prod - sum(vprod)
    if (den <= 0) :
        print(-1)
        #This is printed: -1
        return
        #The program returns None
    #State: `vals` is an empty list, `vprod` is an empty list, `t` is a positive integer such that \(1 \leq t \leq 10^4\), `N` is an input integer where \(1 \leq N \leq 50\), `prod` is the product of all elements in the list `vals`, `den` is `prod - sum(vprod)`, and `den` is greater than 0
    print(' '.join([str(x) for x in vprod]))
    #This is printed: ''
#Overall this is what the function does:The function reads two lines of input. The first line contains an integer \(N\), and the second line contains \(N\) space-separated integers stored in a list `vals`. It then calculates the product of all elements in `vals` and stores it in `prod`. Next, it computes a new list `vprod` where each element is `prod` divided by the corresponding element in `vals`. After that, it calculates `den` as `prod` minus the sum of all elements in `vprod`. If `den` is less than or equal to 0, it prints `-1` and returns. Otherwise, it prints the elements of `vprod` as a space-separated string. The function ultimately returns `None`.

