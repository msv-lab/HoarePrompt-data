#State of the program right berfore the function call: n is an integer such that 1 ≤ n ≤ 10^9.
def func():
    n = int(input())
    for a in range(n // 1234567 + 1):
        for b in range((n - a * 1234567) // 123456 + 1):
            c = (n - a * 1234567 - b * 123456) // 1234
            if a * 1234567 + b * 123456 + c * 1234 == n:
                print('YES')
                exit()
        
    #State of the program after the  for loop has been executed: `n` is an integer within the range 1 to \(10^9\), `a` is the largest integer such that \(a \times 1234567 \leq n\), `b` is the largest integer such that \(b \times 123456 \leq n - a \times 1234567\), `c` is the unique integer such that \(c \times 1234 = n - a \times 1234567 - b \times 123456\), and the loop either prints 'YES' and exits or prints 'NO' if no such integers `a`, `b`, and `c` exist.
    print('NO')
#Overall this is what the function does:The function accepts no parameters and determines whether an integer `n` (where \(1 \leq n \leq 10^9\)) can be expressed as a sum of multiples of 1234567, 123456, and 1234. If such a combination exists, it prints 'YES' and exits. If no such combination exists, it prints 'NO'.

