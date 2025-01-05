#State of the program right berfore the function call: n is a positive integer such that 1 ≤ n ≤ 100000, and the following line contains n space-separated integers where each integer is in the range from 1 to 10^9, inclusive.
def func():
    n = int(input())
    vs = map(int, raw_input().split())
    minO = -1
    res = 0
    for e in vs:
        res += e
        
        if minO == -1 or minO > e:
            minO = e
        
    #State of the program after the  for loop has been executed: `res` is the sum of all integers in `vs`, `minO` is the minimum integer in `vs`, `n` is a positive integer such that 1 ≤ `n` ≤ 100000, and `vs` is a map object containing `n` integers.
    if (res % 2 == 1) :
        res -= minO
    #State of the program after the if block has been executed: *`res` is the sum of all integers in `vs`, `minO` is the minimum integer in `vs`, `n` is a positive integer such that 1 ≤ `n` ≤ 100000, and `vs` is a map object containing `n` integers. If `res` is an odd integer, then `res` is the sum of all integers in `vs` minus `minO`.
    print(res)
#Overall this is what the function does:The function accepts a positive integer `n` (1 ≤ n ≤ 100000) and reads `n` space-separated integers (each between 1 and 10^9). It calculates the sum of these integers and identifies the minimum integer among them. If the sum is odd, it subtracts the minimum integer from the sum before printing the result. If the sum is even, it prints the sum as is. The function does not return a value, but instead prints the final result.

