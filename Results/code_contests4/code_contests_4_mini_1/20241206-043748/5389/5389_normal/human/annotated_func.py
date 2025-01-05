#State of the program right berfore the function call: c1, c2, c3, and c4 are integers in the range [1, 1000], n and m are integers in the range [1, 1000], ai is a list of n integers where each element is in the range [0, 1000], and bi is a list of m integers where each element is in the range [0, 1000].
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
        
    #State of the program after the  for loop has been executed: `bussum` is equal to the sum of the minimum of each element in `bus` multiplied by `c1` and `c2`, `bus` is a list of integers, `c1` and `c2` are the values assigned from input.
    for x in trol:
        trolsum += min(x * c1, c2)
        
    #State of the program after the  for loop has been executed: `bussum` is equal to the sum of the minimum of each element in `bus` multiplied by `c1` and `c2`; `trolsum` is equal to the sum of min(x * c1, c2) for each element `x` in `trol`.
    res = min(bussum, c3) + min(trolsum, c3)
    res = min(res, c4)
    print(res)
#Overall this is what the function does:The function reads input values for four integers (c1, c2, c3, c4), two integers (n, m), and two lists of integers (bus and trol). It calculates the total bus cost as the sum of the minimum of each bus value multiplied by c1 and c2, and similarly for the trol values. It then computes the result as the minimum of the bus cost, c3, and adds the minimum of the trol cost and c3, finally bounding the result by c4. The result is printed, representing the maximum possible cost constrained by the defined limits.

