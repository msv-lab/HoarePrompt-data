#State of the program right berfore the function call: m is an integer such that 1 ≤ m ≤ 100000.
def func():
    m = int(input())
    count = 0
    n = 1
    while True:
        if n // 5 ** count >= m:
            break
        
        count += 1
        
    #State of the program after the loop has been executed: If m is 1, `count` is 0; if m is greater than 1, `count` is 1, `n` remains 1.
    n = 1
    ans = []
    while True:
        if n // 5 ** count < m:
            break
        
        ans.append(n)
        
        n += 1
        
    #State of the program after the loop has been executed: `n` is 5 if `m` is 1, `ans` contains [1, 2, 3, 4]; if `m` is greater than 1, `n` will be the first integer for which `n // 5 >= m` is false, and `ans` will contain all integers from 1 up to `n-1`.
    print(len(ans))
    print(' '.join(map(str, ans)))
#Overall this is what the function does:The function accepts no parameters and reads an integer `m` (where 1 ≤ m ≤ 100000) from input. It determines how many integers from 1 up to the largest integer `n` such that `n // 5^count < m` (where `count` is the smallest integer such that `n // 5^count >= m`) can be accommodated. It prints the count of these integers and the integers themselves. Specifically, it prints the count of integers from 1 to `n-1`, where `n` is the first integer for which `n // 5^count` is no longer greater than or equal to `m`. If `m` is 1, it will print 4 integers: 1, 2, 3, and 4. If `m` is greater than 1, it will dynamically determine the appropriate range based on the value of `m`.

