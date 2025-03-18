#State of the program right berfore the function call: $n$ and $m$ are positive integers such that $1 \le n, m \le 10^9$, and $k$ is an integer such that $2 \le k \le 10^9$.
def func():
    n, m, k = map(int, input().split())
    area = n * m / k
    if (area != int(area)) :
        print('NO')
    else :
        area = int(area)
        if (area == 0) :
            print('NO')
        else :
            print('YES')
            print('0 0')
            if (2 * area <= n) :
                print(f'{2 * area} 1')
                print(f'0 1')
            else :
                if (2 * area <= m) :
                    print(f'1 {2 * area}')
                    print(f'1 0')
                else :
                    print(f'{n} {m // 2}')
                    print(f'0 {m // 2}')
                #State of the program after the if-else block has been executed: `n` is an input integer, `m` is an input integer, `k` is an input integer, and `area` is recalculated as follows: if `2 * area <= m`, then `area` remains `n * m / k` and the console prints '1 0'. Otherwise, `area` becomes `n * (m // 2) / k` and the console prints '0 {m // 2} YES'.
            #State of the program after the if-else block has been executed: *`n`, `m`, and `k` are input integers. `area` is initially calculated as `n * m / k`. If `2 * area <= n`, then `area` is updated to `n / 2` and the console prints '0 1'. Otherwise, `area` is recalculated as follows: if `2 * area <= m`, then `area` remains `n * m / k` and the console prints '1 0'. Otherwise, `area` becomes `n * (m // 2) / k` and the console prints '0 {m // 2} YES'.
        #State of the program after the if-else block has been executed: *`n`, `m`, and `k` are input integers. `area` is initially calculated as `n * m / k`. If `area == 0`, the string 'NO' is printed to the console. Otherwise, if `2 * area <= n`, then `area` is updated to `n / 2` and the console prints '0 1'. If `2 * area > n` and `2 * area <= m`, then `area` remains `n * m / k` and the console prints '1 0'. Otherwise, `area` becomes `n * (m // 2) / k` and the console prints '0 {m // 2} YES'.
    #State of the program after the if-else block has been executed: *`n`, `m`, and `k` are input integers. `area` is initially calculated as `n * m / k`. If `area` is not an integer, the output is 'NO'. If `area` is an integer:
    #- If `area == 0`, the string 'NO' is printed.
    #- If `2 * area <= n`, then `area` is updated to `n / 2` and the console prints '0 1'.
    #- If `2 * area > n` and `2 * area <= m`, then `area` remains `n * m / k` and the console prints '1 0'.
    #- Otherwise, `area` becomes `n * (m // 2) / k` and the console prints '0 {m // 2} YES'.
#Overall this is what the function does:The function accepts three parameters \( n \), \( m \), and \( k \), where \( n \) and \( m \) are positive integers within the range \( 1 \le n, m \le 10^9 \) and \( k \) is an integer within the range \( 2 \le k \le 10^9 \). It calculates the area as \( \text{area} = \frac{n \times m}{k} \). If \( \text{area} \) is not an integer, the function prints 'NO'. If \( \text{area} \) is an integer, it checks several conditions and prints specific outputs based on those conditions. The final state of the program includes the following:

- If \( \text{area} = 0 \), the function prints 'NO'.
- If \( 2 \times \text{area} \leq n \), the function prints '0 1' and '0 0', and exits.
- If \( 2 \times \text{area} > n \) and \( 2 \times \text{area} \leq m \), the function prints '1 0' and '1 0', and exits.
- Otherwise, the function prints '0 \(\frac{m}{2}\)' and '0 \(\frac{m}{2}\)', and exits.

The function does not return any value; instead, it only prints the necessary outputs to the console. Potential edge cases include when \( n \) or \( m \) is exactly \( 1 \) or \( k \) is at its maximum, which might affect the calculation of \( \text{area} \).

