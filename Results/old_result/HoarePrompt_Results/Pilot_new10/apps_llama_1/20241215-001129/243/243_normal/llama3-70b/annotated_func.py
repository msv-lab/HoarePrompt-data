#State of the program right berfore the function call: The input is a positive integer m, such that 1 <= m <= 100000, representing the required number of trailing zeroes in the factorial of a number.
def func():
    m = int(input())
    count = 0
    n = 1
    while True:
        if n // 5 ** count >= m:
            break
        
        count += 1
        
    #State of the program after the loop has been executed: `n` is 1, `count` is the smallest integer such that `5
    n = 1
    ans = []
    while True:
        if n // 5 ** count < m:
            break
        
        ans.append(n)
        
        n += 1
        
    #State of the program after the loop has been executed: `count` is 1, `n` is the first integer for which `n // 5 < m` is true, `ans` contains all integers from the original value of `n` (1) up to `n-1` at the point of termination.
    print(len(ans))
    print(' '.join(map(str, ans)))
#Overall this is what the function does:The function attempts to find and print numbers related to the input `m`, supposedly aiming to find the smallest number whose factorial has `m` trailing zeroes, but due to logical flaws and misinterpretation of the mathematical principles, it does not achieve this correctly and instead performs a series of operations that do not accurately reflect the intended goal, including flawed loops that do not correctly determine the relevant numbers or their counts.

