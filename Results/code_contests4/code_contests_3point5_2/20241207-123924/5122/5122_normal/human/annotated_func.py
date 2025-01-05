#State of the program right berfore the function call: n is a positive integer and the list of n integers contains values between 1 and 10^9 (inclusive).**
def func():
    n = int(input())
    vs = map(int, raw_input().split())
    minO = -1
    res = 0
    for e in vs:
        res += e
        
        if minO == -1 or minO > e:
            minO = e
        
    #State of the program after the  for loop has been executed: n is a positive integer, vs contains n elements, minO is the minimum value in vs, res is the sum of all elements in vs
    if (res % 2 == 1) :
        res -= minO
    #State of the program after the if block has been executed: *n is a positive integer, vs contains n elements, minO is the minimum value in vs, res is the sum of all elements in vs. If the sum of all elements in vs is still an odd number after subtracting minO, then the program will execute the if block. Otherwise, the program will not enter the if block.
    print(res)
#Overall this is what the function does:The function takes an input n and a list of n integers. It calculates the sum of all integers in the list and finds the minimum value in the list. If the sum of all integers is odd, it subtracts the minimum value from the sum and prints the result. The function does not return any value.

