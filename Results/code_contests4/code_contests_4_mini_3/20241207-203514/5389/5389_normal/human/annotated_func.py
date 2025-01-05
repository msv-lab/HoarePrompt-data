#State of the program right berfore the function call: c1, c2, c3, and c4 are integers between 1 and 1000, n and m are integers between 1 and 1000, ai is a list of n integers where each integer is between 0 and 1000, and bi is a list of m integers where each integer is between 0 and 1000.
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
        
    #State of the program after the  for loop has been executed: `c1`, `c2`, `c3`, `c4` are assigned new integer values from input; `n` and `m` are assigned new integer values from input; `ai` and `bi` remain unchanged; `bus` is a list of integers; `trol` is a list of integers from `raw_input()`; `busc1` is an empty list; `bussum` is the sum of `min(x * c1, c2)` for each element `x` in `bus`; `trolsum` is 0.
    for x in trol:
        trolsum += min(x * c1, c2)
        
    #State of the program after the  for loop has been executed: `c1`, `c2`, `c3`, `c4` are assigned new integer values from input; `n` and `m` are assigned new integer values from input; `ai` and `bi` remain unchanged; `bus` is a list of integers; `trol` is a list of integers; `busc1` is an empty list; `bussum` is the sum of `min(x * c1, c2)` for each element `x` in `bus`; `trolsum` is the sum of `min(x * c1, c2)` for each element `x` in `trol`.
    res = min(bussum, c3) + min(trolsum, c3)
    res = min(res, c4)
    print(res)
#Overall this is what the function does:The function accepts several integer inputs (c1, c2, c3, c4, n, m) and two lists of integers (bus and trol), calculates the total cost based on certain constraints, and prints the result. Specifically, it computes the sum of minimum values for each element in the bus and trol lists multiplied by c1, limited by c2, then further limits the total by c3 and finally by c4 before printing the result. The function does not return a value; it only outputs the computed result directly.

