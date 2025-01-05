#State of the program right berfore the function call: n is an integer such that 1 ≤ n ≤ 100,000, and the next line contains n space-separated integers where each integer is in the range from 1 to 1,000,000,000 inclusive.
def func():
    n = int(input())
    vs = map(int, raw_input().split())
    minO = -1
    res = 0
    for e in vs:
        res += e
        
        if minO == -1 or minO > e:
            minO = e
        
    #State of the program after the  for loop has been executed: `res` is the sum of all integers in `vs`, `minO` is the minimum integer in `vs`, `n` is an integer such that 1 ≤ `n` ≤ 100,000, `vs` is a map object containing `n` integers.
    if (res % 2 == 1) :
        res -= minO
    #State of the program after the if block has been executed: *`res` is the sum of all integers in `vs`, `minO` is the minimum integer in `vs`, and `n` is an integer such that 1 ≤ `n` ≤ 100,000. If `res` is odd, `res` is adjusted by subtracting `minO`. If `res` is even, `res` remains the sum of all integers in `vs`.
    print(res)
#Overall this is what the function does:The function accepts an integer `n` (1 ≤ n ≤ 100,000) followed by `n` integers (each ranging from 1 to 1,000,000,000). It calculates the sum of these integers. If the sum is odd, it subtracts the minimum integer from this sum, and then it prints the final result. If the sum is even, it prints the sum as is. The function does not handle cases where the input format is incorrect or where the input values do not meet the specified constraints.

