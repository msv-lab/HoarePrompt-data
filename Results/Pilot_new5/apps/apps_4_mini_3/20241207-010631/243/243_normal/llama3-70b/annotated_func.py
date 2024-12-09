#State of the program right berfore the function call: m is an integer such that 1 <= m <= 100000.
def func():
    m = int(input())
    count = 0
    n = 1
    while True:
        if n // 5 ** count >= m:
            break
        
        count += 1
        
    #State of the program after the loop has been executed: `count` is the smallest integer such that `n // 5
    n = 1
    ans = []
    while True:
        if n // 5 ** count < m:
            break
        
        ans.append(n)
        
        n += 1
        
    #State of the program after the loop has been executed: `count` is 0, `n` is 5, `ans` is a list containing the numbers [1, 2, 3, 4].
    print(len(ans))
    print(' '.join(map(str, ans)))
#Overall this is what the function does:The function prompts the user for an integer input `m` (where 1 <= m <= 100000), then calculates the smallest integer `count` such that `1 // 5

