#State of the program right berfore the function call: n is a positive integer. The list of n integers contains elements in the range from 1 to 10^9, inclusive.
def func():
    n = int(input())
    vs = map(int, raw_input().split())
    minO = -1
    res = 0
    for e in vs:
        res += e
        
        if minO == -1 or minO > e:
            minO = e
        
    #State of the program after the  for loop has been executed: `n` is a positive integer, `vs` is a map object with at least one element, `minO` is the minimum value in `vs`, `res` is the sum of all elements in `vs`.
    if (res % 2 == 1) :
        res -= minO
    #State of the program after the if block has been executed: *`n` is a positive integer, `vs` is a map object with at least one element, `minO` is the minimum value in `vs`, `res` is the sum of all elements in `vs`. If `res` is an odd number after subtracting `minO`, then the overall state of the program is maintained.
    print(res)
#Overall this is what the function does:The function `func` reads a positive integer `n` from input, followed by a list of `n` integers. It calculates the sum of the integers in the list and finds the minimum value. If the sum of the integers is odd, it subtracts the minimum value from the sum and prints the result. The function does not accept any parameters. However, the current implementation does not handle cases where the input list is empty or where the sum is even, which could lead to unexpected behavior.

