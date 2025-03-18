#State of the program right berfore the function call: m is a positive integer such that 1 ≤ m ≤ 100,000.
def func():
    m = int(input())
    count = 0
    n = 1
    while True:
        if n // 5 ** count >= m:
            break
        
        count += 1
        
    #State of the program after the loop has been executed: if m is greater than 1, `count` is the maximum such that `1 // 5
    n = 1
    ans = []
    while True:
        if n // 5 ** count < m:
            break
        
        ans.append(n)
        
        n += 1
        
    #State of the program after the loop has been executed: `n` is `n_final`, `ans` is the list of integers starting from 1 to `n_final - 1`, and `count` is the maximum such that `1 // 5`.
    print(len(ans))
    print(' '.join(map(str, ans)))
#Overall this is what the function does:The function accepts a positive integer `m` from user input within the range of 1 to 100,000. It calculates the maximum integer `count` such that `n // 5

