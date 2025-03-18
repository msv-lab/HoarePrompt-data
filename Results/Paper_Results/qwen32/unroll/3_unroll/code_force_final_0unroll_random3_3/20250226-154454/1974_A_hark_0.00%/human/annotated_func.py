#State of the program right berfore the function call: a and b are integers.
def func_1(a, b):
    return a if a < b else b
    #The program returns the smaller of the two integers, a or b.
#Overall this is what the function does:The function accepts two integer parameters and returns the smaller of the two integers.

#State of the program right berfore the function call: x and y are non-negative integers such that 0 <= x <= 99 and 0 <= y <= 99.
def func_2():
    x, y = map(int, input().split())
    if (x > 0 and y > 0) :
        bxsfory = math.ceil(y / 2)
        x = x - bxsfory * 15 + y * 4
        bxsfory1 = 0 if x <= 0 else math.ceil(x / 15) + 1
        print(bxsfory1 + bxsfory)
        #This is printed: bxsfory1 + bxsfory (where bxsfory is the ceiling of y / 2, and bxsfory1 is 0 if x - bxsfory * 15 + y * 4 is less than or equal to 0, otherwise math.ceil((x - bxsfory * 15 + y * 4) / 15) + 1)
    else :
        if (x == 0 and y > 0) :
            print(math.ceil(y / 2))
            #This is printed: math.ceil(y / 2) (where y is an integer greater than 0 and less than or equal to 99)
        else :
            if (x > 0 and y == 0) :
                print(math.ceil(x / 15))
                #This is printed: math.ceil(x / 15) (where x is an integer greater than 0)
            else :
                print(0)
                #This is printed: 0
            #State: `x` and `y` are integers where 0 <= `x` <= 99 and 0 <= `y` <= 99. At least one of `x` or `y` is 0, and it is not the case that `x` is 0 and `y` is greater than 0. If `x` is greater than 0 and `y` is 0, the conditions remain the same. Otherwise, it is not the case that both `x` and `y` are greater than 0.
        #State: `x` and `y` are integers where 0 <= `x` <= 99 and 0 <= `y` <= 99. At least one of `x` or `y` is 0. If `x` is 0 and `y` is greater than 0, the conditions remain the same. If `x` is greater than 0 and `y` is 0, the conditions remain the same. Otherwise, it is not the case that both `x` and `y` are greater than 0.
    #State: `x` and `y` are integers where 0 <= `x` <= 99 and 0 <= `y` <= 99. If both `x` and `y` are greater than 0, then `x` is updated to `x - bxsfory * 15 + y * 4`, where `bxsfory` is the ceiling of `y / 2`. Additionally, `bxsfory1` is `0` if the updated `x` is less than or equal to `0`, otherwise `math.ceil((x - bxsfory * 15 + y * 4) / 15) + 1`. If at least one of `x` or `y` is 0, the values of `x` and `y` remain unchanged.
#Overall this is what the function does:The function reads two non-negative integers `x` and `y` (where 0 <= x <= 99 and 0 <= y <= 99) from the input, performs calculations based on the values of `x` and `y`, and prints an integer result. The result is the sum of two calculated values: the ceiling of `y / 2` and the ceiling of `(x - (math.ceil(y / 2) * 15) + (y * 4)) / 15` if `x` and `y` are both greater than 0. If only `y` is greater than 0, it prints the ceiling of `y / 2`. If only `x` is greater than 0, it prints the ceiling of `x / 15`. If both `x` and `y` are 0, it prints 0.

#State of the program right berfore the function call: t is a positive integer such that 1 <= t <= 10^4, representing the number of test cases.
def func_3():
    t = int(input())
    for _ in range(t):
        func_2()
        
    #State: `t` is the input integer such that \(1 \leq t \leq 10^4\)
#Overall this is what the function does:The function `func_3` processes a number of test cases specified by the user input `t` (where `1 <= t <= 10^4`). For each test case, it calls `func_2` to perform some unspecified processing. The function does not accept any parameters and does not return a value; instead, it outputs results based on the processing of each test case.

