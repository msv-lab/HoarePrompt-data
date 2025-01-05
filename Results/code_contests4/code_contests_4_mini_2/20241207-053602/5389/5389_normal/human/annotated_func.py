#State of the program right berfore the function call: c1, c2, c3, c4 are integers in the range [1, 1000]; n and m are integers in the range [1, 1000]; ai is a list of integers with length n where each integer is in the range [0, 1000]; bi is a list of integers with length m where each integer is in the range [0, 1000].
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
        
    #State of the program after the  for loop has been executed: `bussum` is equal to the sum of min(x * c1, c2) for each integer x in the list `bus`; `c1`, `c2`, `c3`, `c4` are new integer values; `n` and `m` are new integer values; `bus` is a list of integers; `busc1` is an empty list; `trolsum` is 0.
    for x in trol:
        trolsum += min(x * c1, c2)
        
    #State of the program after the  for loop has been executed: `bussum` is equal to the sum of min(x * c1, c2) for each integer x in the list `bus`; `trolsum` is equal to the sum of min(x * c1, c2) for each integer x in the list `trol`.
    res = min(bussum, c3) + min(trolsum, c3)
    res = min(res, c4)
    print(res)
#Overall this is what the function does:The function reads two lists of integers representing bus and trolley capacities, calculates the total cost based on given constraints (applying limits from constants c1, c2, and c3), and prints out the minimum of the calculated totals and a maximum limit c4. The function does not return any value but prints the result instead.

