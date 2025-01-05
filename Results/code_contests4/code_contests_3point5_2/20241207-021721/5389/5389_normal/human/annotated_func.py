#State of the program right berfore the function call: 
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
        
    #State of the program after the  for loop has been executed: `c1`, `c2`, `c3`, and `c4` have integer values based on user input, `n` and `m` are assigned new integer values, `bus` is a list containing integers parsed from user input using `raw_input().split()`, `trol` is a list of integers created from `bus`, `busc1` is an empty list, `bussum` contains the sum of all elements in `bus` after applying the min function to each element, `trolsum` is 0
    for x in trol:
        trolsum += min(x * c1, c2)
        
    #State of the program after the  for loop has been executed: `c1`, `c2`, `c3`, and `c4` have integer values based on user input, `n` and `m` are assigned new integer values, `bus` is a list containing integers parsed from user input using `raw_input().split()`, `trol` is a list of integers created from `bus`, `busc1` is an empty list, `bussum` contains the sum of all elements in `bus` after applying the min function to each element, `trolsum` is the sum of the minimum values between `x * c1` and `c2` for all elements in `trol`
    res = min(bussum, c3) + min(trolsum, c3)
    res = min(res, c4)
    print(res)
#Overall this is what the function does:The function reads user input for integers and lists, calculates the sum of elements in two lists by applying a min function, then determines the minimum of the sums and prints the result. It does not accept any parameters and outputs a specific value.

