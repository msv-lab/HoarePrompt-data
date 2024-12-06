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
                #State of the program after the if-else block has been executed: *`n` is an integer between 1 and 10^9, `m` is an integer between 1 and 10^9, `k` is an integer between 2 and 10^9, `area` is equal to `n * m / k`, `area` remains an integer, `area` is not equal to 0, and `2 * area` is greater than `n`. If `2 * area` is less than or equal to `m`, then `2 * area` is less than or equal to `m`. Otherwise, `2 * area` is greater than `m` and the printed output is `0 {m // 2}`.
            #State of the program after the if-else block has been executed: *`n`, `m`, and `k` are integers within their specified ranges. If `2 * area` is less than or equal to `n`, the printed output is '0 1'. Otherwise, if `2 * area` is greater than `n`, and if `2 * area` is less than or equal to `m`, then `2 * area` is less than or equal to `m`. If `2 * area` is greater than `m`, the printed output is `0 {m // 2}`.
        #State of the program after the if-else block has been executed: *`n`, `m`, and `k` are integers between their specified limits. If `area` equals 0, then `n`, `m`, and `k` remain unchanged. If `2 * area` is less than or equal to `n`, the output is '0 1'. If `2 * area` is greater than `n` but less than or equal to `m`, then `2 * area` is within bounds for `m`. If `2 * area` is greater than `m`, the output is `0 {m // 2}`.
    #State of the program after the if-else block has been executed: *`n`, `m`, and `k` are integers within their specified limits. If `area` is not an integer, 'NO' is printed. If `area` equals 0, then `n`, `m`, and `k` remain unchanged. If `2 * area` is less than or equal to `n`, the output is '0 1'. If `2 * area` is greater than `n` but less than or equal to `m`, then `2 * area` is within bounds for `m`. If `2 * area` is greater than `m`, the output is `0 {m // 2}`.
#Overall this is what the function does:The function accepts three integers `n`, `m`, and `k` through user input, calculates the area as `(n * m) / k`, and checks if this area is a positive integer. If the area is not an integer or is zero, it prints 'NO'. If the area is a positive integer, it prints 'YES' and provides coordinates based on the value of `2 * area`: if `2 * area` is less than or equal to `n`, it prints coordinates `(2 * area, 1)` and `(0, 1)`; if `2 * area` is less than or equal to `m`, it prints `(1, 2 * area)` and `(1, 0)`; otherwise, it prints `(n, m // 2)` and `(0, m // 2)`.

