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
                #State of the program after the if-else block has been executed: *`n`, `m`, `k` are integers within specified ranges. If `2 * area` is less than or equal to `m`, then `'1 0'` is printed. Otherwise, since it is greater than both `n` and `m`, the output is `'0 {m // 2}'`, indicating that `2 * area` is greater than `m`.
            #State of the program after the if-else block has been executed: *`n`, `m`, `k` are integers. If `2 * area` is less than or equal to `n`, then the output `0 1` is printed. If `2 * area` is less than or equal to `m`, then `'1 0'` is printed. Otherwise, since `2 * area` is greater than both `n` and `m`, the output is `'0 {m // 2}'`, indicating that `2 * area` is greater than `m`.
        #State of the program after the if-else block has been executed: *`n`, `m`, `k` are integers. If `area` is equal to 0, 'NO' has been printed. Otherwise, if `2 * area` is less than or equal to `n`, the output `0 1` is printed. If `2 * area` is less than or equal to `m`, then the output `1 0` is printed. If `2 * area` is greater than both `n` and `m`, the output is `0 {m // 2}`, indicating that `2 * area` is greater than `m`.
    #State of the program after the if-else block has been executed: *`n`, `m`, `k` are integers between 1 and 10^9 and 2 and 10^9 respectively. If `area` is not an integer, then 'NO' has been printed. If `area` is equal to 0, 'NO' has been printed. Otherwise, if `2 * area` is less than or equal to `n`, the output `0 1` is printed. If `2 * area` is less than or equal to `m`, then the output `1 0` is printed. If `2 * area` is greater than both `n` and `m`, the output is `0 {m // 2}`, indicating that `2 * area` is greater than `m`.
#Overall this is what the function does:The function reads three integers `n`, `m`, and `k` from input, calculates the value of `area` as `(n * m) / k`, and checks specific conditions to determine the output. If `area` is not an integer or if it is zero, the function prints 'NO'. Otherwise, it prints 'YES' followed by two pairs of integers that represent coordinates, which depend on the value of `2 * area` relative to `n` and `m`. The potential outputs are coordinates that signify different positions based on these conditions. This function does not return any values; it solely prints the results based on the calculations and checks performed.

