#State of the program right berfore the function call: h is an integer such that 1 ≤ h ≤ 50, and n is an integer such that 1 ≤ n ≤ 2^{h}.
def func():
    h, n = map(int, input().split())
    ans = 0
    while n > 1:
        if n % 2 == 0:
            ans += n // 2 - 1
        else:
            ans += n // 2
        
        n //= 2
        
    #State of the program after the loop has been executed: `h` is an integer such that 1 ≤ h ≤ 50, `n` is 1, `ans` is the sum of the values added during each iteration based on the parity of `n`
    print(ans)
#Overall this is what the function does:The function `func()` accepts two parameters `h` and `n`, where `h` is an integer such that \(1 \leq h \leq 50\), and `n` is an integer such that \(1 \leq n \leq 2^h\). It processes `n` by repeatedly dividing it by 2 and adding either \(n//2 - 1\) or \(n//2\) to `ans` based on whether `n` is even or odd, respectively. After the loop, it prints the value of `ans`. The final state of the program is that `h` remains unchanged, `n` is reduced to 1, and `ans` contains the sum of the values added during each iteration based on the parity of `n`.

