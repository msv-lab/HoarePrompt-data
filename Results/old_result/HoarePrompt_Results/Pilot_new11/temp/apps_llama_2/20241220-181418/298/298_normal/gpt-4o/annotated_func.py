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
                #State of the program after the if-else block has been executed: *`n` is an input integer, `m` is an input integer, `k` is an input integer, `area` is an integer equal to `n * m / k`, `area` is not equal to 0, 'YES' has been printed, '0 0' has been printed, and 2 * `area` is larger than `n`. If 2 * `area` is less than or equal to `m`, then '1 {2 * `area`}' has been printed and '1 0' has been printed. Otherwise, '0 ' and `m // 2` have been printed, and `n` and `m // 2` have been printed.
            #State of the program after the if-else block has been executed: `n` is an input integer, `m` is an input integer, `k` is an input integer, `area` is an integer equal to `n * m / k`, `area` is not equal to 0, 'YES' has been printed, '0 0' has been printed. If `2 * area` is less than or equal to `n`, then `2 * area` and `1` have been printed, and '0 1' has been printed. Otherwise, `2 * area` is larger than `n`. If `2 * area` is less than or equal to `m`, then '1 {2 * `area`}' has been printed and '1 0' has been printed. Otherwise, '0 ' and `m // 2` have been printed, and `n` and `m // 2` have been printed.
        #State of the program after the if-else block has been executed: `n` is an input integer, `m` is an input integer, `k` is an input integer, `area` is an integer equal to `n * m / k`. If `area` is 0, 'NO' has been printed. If `area` is not 0, 'YES' and '0 0' have been printed. Additionally, if `2 * area` is less than or equal to `n`, then `2 * area` and `1` have been printed, and '0 1' has been printed. If `2 * area` is larger than `n` but less than or equal to `m`, then '1 {2 * `area`}' has been printed and '1 0' has been printed. If `2 * area` is larger than both `n` and `m`, then '0 ' and `m // 2` have been printed, and `n` and `m // 2` have been printed.
    #State of the program after the if-else block has been executed: *`n` is an input integer, `m` is an input integer, `k` is an input integer, `area` is equal to `n * m / k`. If `area` is not an integer, 'NO' has been printed to the console. If `area` is an integer, then 'NO' has been printed if `area` is 0. If `area` is not 0, 'YES' and '0 0' have been printed. Additionally, if `2 * area` is less than or equal to `n`, then `2 * area` and `1` have been printed, and '0 1' has been printed. If `2 * area` is larger than `n` but less than or equal to `m`, then '1 {2 * `area`}' has been printed and '1 0' has been printed. If `2 * area` is larger than both `n` and `m`, then '0 ' and `m // 2` have been printed, and `n` and `m // 2` have been printed.
#Overall this is what the function does:The function takes three integer inputs (n, m, k) from the user, which are expected to be within specific ranges (1 <= n, m <= 10^9 and 2 <= k <= 10^9), and determines whether the area calculated as n * m / k is an integer and not equal to 0. If the area is not an integer or is 0, the function prints 'NO'. If the area is a non-zero integer, it prints 'YES' and '0 0', followed by additional coordinates based on the comparison of 2 * area with n and m. Specifically, it prints either '2 * area 1' and '0 1' if 2 * area is less than or equal to n, '1 2 * area' and '1 0' if 2 * area is larger than n but less than or equal to m, or 'n m // 2' and '0 m // 2' if 2 * area exceeds both n and m. The function's intended purpose seems to be related to geometric or spatial calculations, possibly involving rectangular areas divided into smaller sections, but its exact application or significance cannot be determined without further context.

