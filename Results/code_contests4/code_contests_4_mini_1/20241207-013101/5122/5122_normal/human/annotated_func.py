#State of the program right berfore the function call: n is an integer such that 1 ≤ n ≤ 100,000, and the next line contains n space-separated integers, each in the range from 1 to 1,000,000,000, inclusive.
def func():
    n = int(input())
    vs = map(int, raw_input().split())
    minO = -1
    res = 0
    for e in vs:
        res += e
        
        if minO == -1 or minO > e:
            minO = e
        
    #State of the program after the  for loop has been executed: `n` is an integer such that 1 ≤ `n` ≤ 100,000; `minO` is the minimum value in `vs`; `res` is the sum of all integers in `vs`.
    if (res % 2 == 1) :
        res -= minO
    #State of the program after the if block has been executed: *`n` is an integer such that 1 ≤ `n` ≤ 100,000; `minO` is the minimum value in `vs`; `res` is the sum of all integers in `vs`. If `res` is odd, then `res` is the sum of all integers in `vs` after subtracting `minO`, and `res` may be either odd or even depending on the parity of `minO`.
    print(res)
#Overall this is what the function does:The function accepts an integer `n` (1 ≤ n ≤ 100,000) and a sequence of `n` space-separated integers (1 ≤ each integer ≤ 1,000,000,000). It calculates the sum of these integers and identifies the minimum value among them. If the total sum is odd, it subtracts the minimum value from the sum before printing the result. The function does not return a value but instead prints the final computed sum, which may be either odd or even based on the initial input.

