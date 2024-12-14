#State of the program right berfore the function call: n, m, and k are integers such that 1 <= n, m <= 10^9 and 2 <= k <= 10^9.
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
                #State of the program after the if-else block has been executed: *`n` is an integer (1 <= `n` <= 10^9), `m` is an integer (1 <= `m` <= 10^9), `k` is an integer (2 <= `k` <= 10^9), and `area` is calculated as `n * m / k` which is greater than 0. If `2 * area` is less than or equal to `m`, the printed output is '1 0'. Otherwise, the printed output is `0 m // 2`.
            #State of the program after the if-else block has been executed: *`n`, `m`, and `k` are integers with the specified ranges. If `2 * area` is less than or equal to `n`, the output is '0 1'. Otherwise, if `2 * area` is less than or equal to `m`, the output is '1 0'. If `2 * area` is greater than both `n` and `m`, the output is '0 m // 2'.
        #State of the program after the if-else block has been executed: *`n`, `m`, `k` are integers within specified ranges. If `area` equals 0, "NO" is printed. Otherwise, if `2 * area` is less than or equal to `n`, the output is '0 1'. If `2 * area` is less than or equal to `m`, the output is '1 0'. If `2 * area` is greater than both `n` and `m`, the output is '0 m // 2'.
    #State of the program after the if-else block has been executed: *`n`, `m`, `k` are integers within specified ranges. If `area` is not an integer, indicating a fractional component, 'NO' is printed. If `area` is equal to 0, 'NO' is printed. Otherwise, if `2 * area` is less than or equal to `n`, the output is '0 1'. If `2 * area` is less than or equal to `m`, the output is '1 0'. If `2 * area` is greater than both `n` and `m`, the output is '0 m // 2'.
#Overall this is what the function does:The function accepts three integers `n`, `m`, and `k` provided through input. It computes the area based on the formula `area = n * m / k`. If the area is not an integer or if it is zero, the function prints 'NO'. If the area is a positive integer, it prints 'YES' and two coordinates based on the value of `2 * area`: if `2 * area` is less than or equal to `n`, it outputs '0 1'; if it's less than or equal to `m`, it outputs '1 0'; otherwise, it outputs '0 m // 2' along with the maximum values of `n` and `m` that fit the criteria.

