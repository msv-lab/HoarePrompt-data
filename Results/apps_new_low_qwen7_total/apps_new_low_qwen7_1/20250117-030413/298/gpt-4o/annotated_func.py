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
                #State of the program after the if-else block has been executed: *`n`, `m`, and `k` are updated based on the input. `area` remains the same as before the execution of the code. If `2 * area <= m`, then two print statements execute with outputs '1 2*area' and '1 0'. Otherwise, no additional print statements are executed with different outputs.
            #State of the program after the if-else block has been executed: *`n`, `m`, and `k` are updated based on the input. `area` remains the same as before the execution of the code. If `2 * area <= n`, the print statements execute with outputs '1 2*area' and '1 0'. Otherwise, if `2 * area <= m`, then two print statements execute with outputs '1 2*area' and '1 0'. No other print statements are executed under any other conditions.
        #State of the program after the if-else block has been executed: *`n`, `m`, and `k` are updated based on the input. `area` remains the same as before the execution of the code. If `area == 0`, the console prints 'NO'. Otherwise, if `2 * area <= n`, the console prints '1 2*area' and '1 0'. If `2 * area <= m` and `2 * area > n`, the console prints '1 2*area' and '1 0'. No other print statements are executed under any other conditions.
    #State of the program after the if-else block has been executed: *`n`, `m`, and `k` are updated based on the input where `area = n * m / k`. If `area` is not an integer, the function prints 'NO'. Otherwise, if `area == 0`, the function prints 'NO'. If `2 * area <= n`, the function prints '1 2*area' and '1 0'. If `2 * area <= m` and `2 * area > n`, the function prints '1 2*area' and '1 0'. No other print statements are executed under any other conditions.
#Overall this is what the function does:The function reads three integers \( n \), \( m \), and \( k \) from standard input, where \( 1 \leq n, m \leq 10^9 \) and \( 2 \leq k \leq 10^9 \). It calculates the area as \( \frac{n \times m}{k} \). If the area is not an integer, it prints "NO". If the area is zero, it also prints "NO". If the area is an integer, it checks if \( 2 \times \text{area} \leq n \) or \( 2 \times \text{area} \leq m \). If either condition is true, it prints specific pairs of integers. If neither condition is true, it prints "1 0". The function does not return any value and only prints the results to standard output.

