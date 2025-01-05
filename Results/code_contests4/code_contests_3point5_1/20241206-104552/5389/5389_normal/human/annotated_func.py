#State of the program right berfore the function call: **
def func():
    c1, c2, c3, c4 = [int(x) for x in raw_input().split()]
    n, m = [int(x) for x in raw_input().split()]
    bus = [int(x) for x in raw_input().split()]
    trol = [int(x) for x in raw_input().split()]
    busc1 = []
    bussum = 0
    trolsum = 0
    for x in bus:
        bussum += min(x * c1, c2)
        
    #State of the program after the  for loop has been executed: `c1`, `c2`, `c3`, `c4` are assigned integer values, `n` and `m` are assigned integer values, `busc1` is an empty list, `bussum` is the sum of the minimum values between each element of `bus` multiplied by `c1` and `c2`, `trolsum` is 0
    for x in trol:
        trolsum += min(x * c1, c2)
        
    #State of the program after the  for loop has been executed: `c1`, `c2`, `c3`, `c4` are assigned integer values, `n` and `m` are assigned integer values, `busc1` is an empty list, `bussum` is the sum of the minimum values between each element of `bus` multiplied by `c1` and `c2`, `trolsum` is updated based on the minimum value between `x * c1` and `c2` for all elements in `trol`
    res = min(bussum, c3) + min(trolsum, c3)
    res = min(res, c4)
    print(res)
#Overall this is what the function does:The function `func` reads input values from the user, calculates the sum of minimum values between elements of arrays `bus` and `trol` multiplied by `c1` and `c2`, then computes the result based on conditions involving `c3` and `c4`. The final result is printed as output. The function does not accept any parameters and does not have a specific return value.

