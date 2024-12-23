#State of the program right berfore the function call: n, m, and k are integers such that 1 ≤ n, m ≤ 10^9 and 2 ≤ k ≤ 10^9.
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
                #State of the program after the if-else block has been executed: *`n` is `n_input`, `m` is `m_input`, `k` is `k_input`, and the area is \((n_input * m_input) / k_input\). If \(2 * area \leq m_input\), the output is `1 0`. Otherwise, the output is `0` followed by `m // 2`.
            #State of the program after the if-else block has been executed: *`n` is `n_input`, `m` is `m_input`, `k` is `k_input`, and the area is \((n_input * m_input) / k_input\). If \(2 * area \leq n_input\), the output is "0 1". Otherwise, if \(2 * area \leq m_input\), the output is "1 0". Otherwise, the output is "0" followed by `m // 2`.
        #State of the program after the if-else block has been executed: *`n` is `n_input`, `m` is `m_input`, `k` is `k_input`, and `area` is \((n_input * m_input) / k_input\). If `area` is 0, the print statement outputs 'NO'. Otherwise, if \(2 * area \leq n_input\), the output is "0 1". If \(2 * area \leq m_input\) and the previous condition is not met, the output is "1 0". If neither of the above conditions is met, the output is "0" followed by `m // 2`.
    #State of the program after the if-else block has been executed: *`n` is `n_input`, `m` is `m_input`, `k` is `k_input`. If `area` (which is `(n_input * m_input) / k_input`) is not an integer, the print statement 'NO' is executed. If `area` is 0, the print statement outputs 'NO'. Otherwise, if \(2 * area \leq n_input\), the output is "0 1". If \(2 * area \leq m_input\) and the previous condition is not met, the output is "1 0". If neither of the above conditions is met, the output is "0" followed by `m // 2`.
#Overall this is what the function does:The function reads three integers \(n\), \(m\), and \(k\) from input, where \(1 \leq n, m \leq 10^9\) and \(2 \leq k \leq 10^9\). It calculates the area as \(\frac{n \times m}{k}\) and checks if this area is an integer. If the area is not an integer, it prints 'NO'. If the area is zero, it also prints 'NO'. Otherwise, it prints 'YES' and then proceeds to print coordinates based on certain conditions:

1. If \(2 \times \text{area} \leq n\), it prints "0 1".
2. If \(2 \times \text{area} > n\) but \(2 \times \text{area} \leq m\), it prints "1 0".
3. If neither of the above conditions is met, it prints "0" followed by \(m // 2\).

After these operations, the function does not return anything explicitly; however, it prints the necessary information to the console based on the given conditions.

