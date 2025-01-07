#State of the program right berfore the function call: m is an integer such that 1 ≤ m ≤ 100 000.
def func():
    m = int(input())
    count = 0
    n = 1
    while True:
        if n // 5 ** count >= m:
            break
        
        count += 1
        
    #State of the program after the loop has been executed: `m` is an integer between 1 and 100,000 inclusive, `count` is the largest integer such that \(5^{\text{count}} \leq \frac{n}{m}\) and \(5^{\text{count}+1} > \frac{n}{m}\), and `n` is the result of the last division operation, i.e., `n // 5
    n = 1
    ans = []
    while True:
        if n // 5 ** count < m:
            break
        
        ans.append(n)
        
        n += 1
        
    #State of the program after the loop has been executed: `m` is an integer between 1 and 100,000 inclusive, `count` is the largest integer such that \(5^{\text{count}} \leq \frac{n}{m}\) and \(5^{\text{count}+1} > \frac{n}{m}\), `n` is the final value of `n` after all iterations of the loop, `ans` is a list containing all integers from 1 up to and including `n`.
    print(len(ans))
    print(' '.join(map(str, ans)))
#Overall this is what the function does:The function reads an integer `m` (where \(1 \leq m \leq 100,000\)) from input. It then calculates the largest integer `count` such that \(5^{\text{count}} \leq \frac{n}{m}\). Afterward, it generates a list `ans` containing all integers from 1 up to and including the last valid `n` where \(5^{\text{count}} > \frac{n}{m}\). Finally, it prints the length of `ans` followed by the elements of `ans` separated by spaces.

