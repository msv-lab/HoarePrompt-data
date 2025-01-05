#State of the program right berfore the function call: c1, c2, c3, c4 are integers within the range 1 to 1000, n and m are integers within the range 1 to 1000, ai is a list of integers where each element is within the range 0 to 1000 for i from 1 to n, and bi is a list of integers where each element is within the range 0 to 1000 for j from 1 to m.
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
        
    #State of the program after the  for loop has been executed: bussum is equal to the sum of min(x * c1, c2) for each x in bus; bus is a list of integers, c1 and c2 are integer values from input.
    for x in trol:
        trolsum += min(x * c1, c2)
        
    #State of the program after the  for loop has been executed: `bussum` remains equal to the sum of min(x * c1, c2) for each x in bus, `trolsum` is equal to the sum of min(x * c1, c2) for each x in trol, `trol` is a list of integers with at least as many elements as the number of iterations executed.
    res = min(bussum, c3) + min(trolsum, c3)
    res = min(res, c4)
    print(res)
#Overall this is what the function does:The function calculates the total cost of bus and trolley rides based on given constraints, where the cost for each ride is capped by a maximum value. It takes inputs for costs, limits, and the number of rides for buses and trolleys, computes the total costs for each, and prints the minimum of these totals, further constrained by additional limits. The function does not return a value but directly prints the result.

