#State of the program right berfore the function call: c1, c2, c3, c4 are integers representing the costs of different ticket types (1 ≤ c1, c2, c3, c4 ≤ 1000); n and m are integers representing the number of buses and trolleys (1 ≤ n, m ≤ 1000); ai is a list of integers representing the number of rides for each bus (0 ≤ ai ≤ 1000); bi is a list of integers representing the number of rides for each trolley (0 ≤ bi ≤ 1000).
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
        
    #State of the program after the  for loop has been executed: `bussum` is equal to the sum of min(x * c1, c2) for all elements x in `bus`, `bus` is a list of integers, `c1`, `c2`, `c3`, `c4`, `n`, and `m` are integers, `trol` is a list of integers, `busc1` is an empty list, `trolsum` is 0.
    for x in trol:
        trolsum += min(x * c1, c2)
        
    #State of the program after the  for loop has been executed: `bussum` is equal to the sum of min(x * c1, c2) for all elements x in `bus`; `trolsum` is equal to the sum of min(x * c1, c2) for all elements x in `trol`.
    res = min(bussum, c3) + min(trolsum, c3)
    res = min(res, c4)
    print(res)
#Overall this is what the function does:The function accepts ticket costs for different types of rides, the number of buses and trolleys, and the number of rides for each bus and trolley, then calculates the minimum total cost for rides taken on buses and trolleys based on the predefined ticket costs, ensuring that the cost is capped at specified limits for both bus and trolley rides, and overall. It returns the minimum total cost considering these constraints.

