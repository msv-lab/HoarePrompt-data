#State of the program right berfore the function call: **
def func_1(a, b):
    c = a + b
    if (c >= mod) :
        c -= mod
    #State of the program after the if block has been executed: *`c` is the sum of `a` and `b`. If `c` is greater than or equal to `mod`, the program executes as follows: if `c` is equal to `mod`, `c` is updated to `mod`. If `c` is greater than `mod`, `c` remains unchanged.
    return c
    #The program returns the updated value of 'c' after the conditions are applied
#Overall this is what the function does:The function `func_1` accepts two parameters `a` and `b`, calculates the sum of `a` and `b`, and then updates the value of `c` based on the condition that if `c` is greater than or equal to `mod`, it is adjusted accordingly. The function returns the final value of `c` after applying the conditions. If `c` equals `mod`, it is set to `mod`, and if `c` exceeds `mod`, it remains unchanged.

#State of the program right berfore the function call: **
def func_2(a, b):
    return a * b % mod
    #The program returns the result of the multiplication of 'a' and 'b' modulo 'mod'
#Overall this is what the function does:The function `func_2` accepts two integer parameters `a` and `b`, and returns the result of their multiplication modulo `mod`.

#State of the program right berfore the function call: **
def func_3(a, b):
    if (b == 0) :
        return 1
        #The program returns the integer 1
    else :
        if (b % 2 == 1) :
            return func_2(a, func_3(a, b - 1))
            #The program returns the result of calling func_2 with parameters a and the result of calling func_3 with parameters a and b-1.
        else :
            temp = func_3(a, b / 2)
            return func_2(temp, temp)
            #The program returns the result of calling func_2 with the input parameters 'temp' and 'temp'
#Overall this is what the function does:The function `func_3` accepts two parameters, `a` and `b`, and returns different values based on the following cases:
Case 1: If `b` is equal to 0, the function returns the integer 1.
Case 2: If `b` is odd, the function calls `func_2` with parameters `a` and the result of calling `func_3` with parameters `a` and `b-1`.
Case 3: If `b` is even, the function calculates `temp` by calling `func_3` with parameters `a` and `b / 2`, then returns the result of calling `func_2` with `temp` as both parameters.
Therefore, the functionality of the function `func_3` involves recursion and condition checking based on the value of `b`.

#State of the program right berfore the function call: **
def func_4(a):
    return func_3(a, mod - 2)
    #The program returns the result of calling function 'func_3' with arguments 'a' and 'mod - 2'
#Overall this is what the function does:The function func_4 accepts a parameter `a` and returns the result of calling function 'func_3' with arguments 'a' and 'mod - 2'.

#State of the program right berfore the function call: a is a list of N positive integers and m is a positive integer such that 1 <= N <= 10^4 and 1 <= m <= 10^6.
def func_5(a, m):
    m0 = m
    y = 0
    x = 1
    if (m == 1) :
        return 0
        #The program returns 0
    #State of the program after the if block has been executed: *`a` is a list of N positive integers, `m`, `m0` are positive integers such that 1 <= N <= 10^4 and 1 <= m <= 10^6, `m0` is the same as `m`, `y` is 0, `x` is 1, m is not equal to 1
    while a > 1:
        q = a // m
        
        t = m
        
        m = a % m
        
        a = t
        
        t = y
        
        y = x - q * y
        
        x = t
        
    #State of the program after the loop has been executed: `a` is 1, `m` is 0, `m0` and `t` are positive integers, `y` is the result of the final `x - q * y`, `x` is the result of the final `y`
    if (x < 0) :
        x = x + m0
    #State of the program after the if block has been executed: *`a` is 1, `m` is 0, `m0` and `t` are positive integers, `y` is the result of the final `x - q * y`, `x` is the result of the final `y`. If `x` is less than 0, then `x` is increased by `m0`.
    return x
    #The program returns the final value of variable `x` after the calculations described above
#Overall this is what the function does:The function `func_5` accepts a list `a` of N positive integers and a positive integer `m`, where 1 <= N <= 10^4 and 1 <= m <= 10^6. The function performs calculations on `a` and `m` to determine the final value of variable `x` following a series of operations involving `m`, `a`, `x`, and `y`. If the execution reaches a specific condition where `m` is equal to 1, the function returns 0. Otherwise, it calculates the final value of `x` based on the given conditions and returns it. In the process, if `x` becomes negative, it is adjusted by adding `m0`.

#State of the program right berfore the function call: **
def func_6():
    n = int(raw_input())
    arr = [int(x) for x in raw_input().split()]
    answer = {}
    for i in range(n):
        cnt = {}
        
        x = arr[i]
        
        i = 2
        
        while i * i <= x:
            while x % i == 0:
                x /= i
                cnt[i] = cnt.get(i, 0) + 1
            i += 1
        
        if x != 1:
            cnt[x] = cnt.get(x, 0) + 1
        
        for key in cnt:
            answer[key] = max(answer.get(key, 0), cnt[key])
        
    #State of the program after the  for loop has been executed: `n` is greater than or equal to 0, `arr` is a list containing integers, `answer` is a dictionary where each key corresponds to a prime factor of the integers in `arr` and the value is the maximum power of that prime factor that divides the integer at its index in `arr`
    lcm = 1
    for prime in answer:
        for _ in range(answer[prime]):
            lcm = func_2(lcm, prime)
        
    #State of the program after the  for loop has been executed: `n` is greater than or equal to 0, `arr` is a list containing integers, `answer` is a dictionary with keys corresponding to prime factors of integers in `arr` and the maximum powers that divide each integer, `lcm` is updated by calling `func_2` with arguments `lcm` and each prime factor in the `answer` dictionary
    ans = 0
    for x in arr:
        ans = func_1(ans, func_2(lcm, func_4(x)))
        
    #State of the program after the  for loop has been executed: `n` is greater than or equal to 0, `arr` is a list containing integers, `answer` is a dictionary with keys corresponding to prime factors of integers in `arr` and the maximum powers that divide each integer, `lcm` is updated, `ans` is the result of multiple calls to `func_1` with arguments `ans`, the result of calling `func_2` with arguments `lcm` and the result of calling `func_4` with each element in `arr`
    ans = int(ans)
    print(ans)
#Overall this is what the function does:The function `func_6` reads an integer `n` and a list of integers. It then calculates the prime factors of each integer in the list and stores the maximum power of each prime factor in a dictionary `answer`. After that, it computes the least common multiple (lcm) of these prime factors. Next, it iterates through the list of integers, calculates the product of the lcm with the result of two different functions, and updates the answer. Finally, it converts the final answer to an integer and prints it. The function does not accept any parameters and solely operates based on the input read during execution.

