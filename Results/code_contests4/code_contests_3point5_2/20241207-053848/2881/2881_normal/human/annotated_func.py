#State of the program right berfore the function call: a, b, x, y are integers such that 1 ≤ a, b, x, y ≤ 2·10^9.**
def func_1(be, en):
    while be < en:
        mid = (be + en + 1) // 2
        
        if x * mid <= a and y * mid <= b:
            be = mid
        else:
            en = mid - 1
        
    #State of the program after the loop has been executed: a, b, x, y are integers such that 1 ≤ a, b, x, y ≤ 2·10^9. The loop terminates when be is no longer less than en. The final values of be, en, mid, x, y are based on the conditions x * mid <= a and y * mid <= b being satisfied or not.
    print(be * x, be * y)
#Overall this is what the function does:The function `func_1` accepts two integer parameters `be` and `en` where 1 ≤ be, en ≤ 2·10^9. It calculates the value of `be` and `en` based on the conditions x * mid <= a and y * mid <= b within a while loop. The function then prints the values of be multiplied by x and y.

