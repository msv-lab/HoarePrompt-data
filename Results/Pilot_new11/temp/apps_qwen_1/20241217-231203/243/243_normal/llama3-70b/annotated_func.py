#State of the program right berfore the function call: m is an integer such that 1 ≤ m ≤ 100 000.
def func():
    m = int(input())
    count = 0
    n = 1
    while True:
        if n // 5 ** count >= m:
            break
        
        count += 1
        
    #State of the program after the loop has been executed: `m` is an integer value between 1 and 100,000, `count` is the largest integer such that 5^count is less than or equal to `m`, and `n` is 1
    n = 1
    ans = []
    while True:
        if n // 5 ** count < m:
            break
        
        ans.append(n)
        
        n += 1
        
    #State of the program after the loop has been executed: `m` is an integer value between 1 and 100,000; `count` is the largest integer such that \(5^{\text{count}} \leq m\); `n` is `n + k`, where `k` is the number of times the loop executed; `ans` is a list containing `[1, 2, ..., n]` if the final value of `n` is less than 5, otherwise `ans` is unchanged.
    print(len(ans))
    print(' '.join(map(str, ans)))
#Overall this is what the function does:The function accepts no parameters and calculates a sequence of numbers from 1 up to the largest number less than or equal to `m` that is not divisible by 5. It then prints the length of this sequence followed by the sequence itself. If the final value of `n` is less than 5, the sequence includes all numbers from 1 to `n`; otherwise, the sequence remains unchanged. Potential edge cases include when `m` is less than 5, in which case the sequence will only contain 1, and when `m` is exactly 100,000, the function will still terminate correctly. However, the annotation stating that `n` is `n + k` where `k` is the number of times the loop executed is incorrect; instead, `n` increments by 1 in each iteration.

