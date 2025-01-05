#State of the program right berfore the function call: n is a positive integer, and the list of n integers contains values in the range from 1 to 10^9, inclusive.**
def func():
    n = int(input())
    vs = map(int, raw_input().split())
    minO = -1
    res = 0
    for e in vs:
        res += e
        
        if minO == -1 or minO > e:
            minO = e
        
    #State of the program after the  for loop has been executed: `n` is a positive integer, `vs` has been iterated over completely, `minO` is the minimum value in the list `vs`, `res` is the sum of all elements in `vs`.
    if (res % 2 == 1) :
        res -= minO
    #State of the program after the if block has been executed: *`n` is a positive integer, `vs` has been iterated over completely, `minO` is the minimum value in the list `vs`, `res` is the sum of all elements in `vs` minus the minimum value. If the sum of elements in `vs` is odd, then the function performs the if part operation.
    print(res)
#Overall this is what the function does:The function does not accept any parameters. It takes an integer n as input and generates a list of n integers. It then calculates the sum of all elements in the list and subtracts the minimum value from the sum if the sum is odd, finally printing the result.

