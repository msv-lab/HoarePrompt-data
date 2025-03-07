#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 500, and for each test case, n is an integer such that 1 ≤ n ≤ 500. Additionally, the sum of n^2 over all test cases does not exceed 5 × 10^5.
def func():
    t = int(input())
    for _ in range(t):
        n = int(input())
        
        sum, r = 0, 0
        
        for i in range(1, n + 1):
            if n * (n + 1) // 2 > i * n:
                r = i
                sum += n * (n + 1) // 2
            else:
                sum += i * n
        
        print(sum, n + r)
        
        for j in range(1, n + r + 1):
            if j <= n:
                print(1, j, end=' ')
                print(*range(1, n + 1))
            else:
                print(2, j % n, end=' ')
                print(*range(1, n + 1))
        
    #State: Output State: The output will consist of `t` pairs of lines, each pair containing a sum and a number `n + r`. For each input `n`, it will also print a sequence of lines where the first line prints numbers from 1 to `n`, and subsequent lines alternate between printing numbers from 1 to `n` in order and repeating the first number based on the modulo operation with `n`.
    #
    #To break it down further:
    #- For each input `n`, the loop calculates a sum and a value `r`.
    #- It then prints the sum and `n + r`.
    #- Following this, it prints a sequence of lines where the first line contains numbers from 1 to `n`. Subsequent lines alternate between printing numbers from 1 to `n` and repeating the first number based on the modulo operation with `n`.
    #
    #This pattern will repeat `t` times based on the input integer `t`.
#Overall this is what the function does:The function processes multiple test cases, each consisting of an integer `t` (1 ≤ t ≤ 500) and an integer `n` (1 ≤ n ≤ 500), where the sum of `n^2` over all test cases does not exceed 5 × 10^5. For each test case, it calculates a sum and a value `r`, then prints the sum and `n + r`. It also prints a sequence of lines where the first line contains numbers from 1 to `n`, and subsequent lines alternate between printing numbers from 1 to `n` and repeating the first number based on the modulo operation with `n`. This process repeats `t` times.

