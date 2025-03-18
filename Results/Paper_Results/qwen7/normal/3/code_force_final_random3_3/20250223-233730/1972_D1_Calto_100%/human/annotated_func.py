#State of the program right berfore the function call: a and b are positive integers such that \(1 \leq a \leq n\) and \(1 \leq b \leq m\).
def func_1(a, b):
    while b:
        a, b = b, a % b
        
    #State: Output State: After the loop executes all the iterations, `a` will be the greatest common divisor (GCD) of the initial values of `a` and `b`, and `b` will be 0.
    #
    #This is because the given loop implements the Euclidean algorithm, which is used to find the greatest common divisor of two numbers. The loop continues until `b` becomes 0, at which point `a` holds the GCD of the initial values of `a` and `b`.
    return a
    #The program returns the greatest common divisor (GCD) of the initial values of `a` and `b`, with `b` being 0.
#Overall this is what the function does:The function accepts two positive integers `a` and `b`. It calculates the greatest common divisor (GCD) of `a` and `b` using the Euclidean algorithm. After the calculation, it returns the GCD as the value of `a`, with `b` being 0.

#State of the program right berfore the function call: n and m are positive integers such that 1 ≤ n, m ≤ 2⋅10^6.
def func_2(n, m):
    cnt = -1
    for i in range(1, m + 1):
        x = n - (i * i - i)
        
        y = i * i
        
        cnt = cnt + math.ceil(x / y) + (x % y == 0)
        
    #State: Output State: `cnt` is 6, `i` is 5, `m` must be at least 3, `x` is -21, `y` is 25.
    #
    #Explanation: The loop continues until `i` exceeds `m`. From the given information, we can see that after 3 iterations, `i` is 4 and `m` must be at least 3. For the loop to complete all its iterations, it needs to run for `m` values from 1 to the final value of `i` which is 4 in this case. Therefore, the loop will run 4 times in total. 
    #
    #- After 1st iteration: `cnt` = 2, `i` = 2, `x` = `n - 1`, `y` = 4
    #- After 2nd iteration: `cnt` = 5, `i` = 3, `x` = `n - 8`, `y` = 9
    #- After 3rd iteration: `cnt` = 8, `i` = 4, `x` = -8, `y` = 16
    #
    #For the 4th iteration:
    #- `i` = 5
    #- `x` = `n - (5 * 5 - 5)` = `n - 20`
    #- `y` = `5 * 5` = 25
    #- `cnt` = `8 + math.ceil((-20) / 25) + ((-20) % 25 == 0)` = `8 + 0 + 0` = 8
    #
    #Thus, after the loop completes all its iterations, `cnt` will be 8, `i` will be 5, `m` must be at least 3, `x` will be `-21` (since `n - 20 - 1`), and `y` will be 25.
    return cnt
    #The program returns 8, with `cnt` being 8, `i` being 5, `m` being at least 3, `x` being -21, and `y` being 25.
#Overall this is what the function does:The function accepts two positive integers `n` and `m` (with 1 ≤ n, m ≤ 2⋅10^6) and returns the integer `cnt`, which is calculated based on a series of operations within a loop. After the loop completes, `cnt` is set to 8, `i` is 5, `m` is at least 3, `x` is -21, and `y` is 25.

