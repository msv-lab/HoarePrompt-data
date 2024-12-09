#State of the program right berfore the function call: m is an integer such that 1 ≤ m ≤ 100000.
def func():
    m = int(input())
    count = 0
    n = 1
    while True:
        if n // 5 ** count >= m:
            break
        
        count += 1
        
    #State of the program after the loop has been executed: `count` is 1, `n` is 1, `m` is an input integer such that 1 ≤ `m` ≤ 100000. The loop executes while `n // 5
    n = 1
    ans = []
    while True:
        if n // 5 ** count < m:
            break
        
        ans.append(n)
        
        n += 1
        
    #State of the program after the loop has been executed: `count` is 1, `n` is the first integer for which `n // 5 < m`, `m` is an input integer such that 1 ≤ `m` ≤ 100000, and `ans` contains each integer from 1 to the final value of `n - 1`.
    print(len(ans))
    print(' '.join(map(str, ans)))
#Overall this is what the function does:The function accepts no parameters, prompts the user for an integer `m`, computes the number of integers from 1 to just below the first integer where \( n // 5^{\text{count}} < m \), and returns the count of these integers along with the integers themselves as a space-separated string. It may not handle edge cases where `m` is very small or large properly, potentially leading to an empty output.

