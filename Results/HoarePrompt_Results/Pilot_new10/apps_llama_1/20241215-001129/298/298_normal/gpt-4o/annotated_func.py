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
                #State of the program after the if-else block has been executed: `n` is an input integer, `m` is an input integer, `k` is an input integer, `area` is an integer equal to `n * m / k`, `area` is not equal to 0, 'YES' has been printed, '0 0' has been printed, and 2 * `area` is larger than `n`. If 2 * `area` is less than or equal to `m`, then '1 ` followed by the value of `2 * area` has been printed and '1 0' has been printed. Otherwise, '0 0' has been printed twice, `f'{n} {m // 2}'` has been printed, and `f'0 {m // 2}'` has been printed twice.
            #State of the program after the if-else block has been executed: `n` is an input integer, `m` is an input integer, `k` is an input integer, `area` is an integer equal to `n * m / k`, `area` is not equal to `0`, 'YES' has been printed, '0 0' has been printed. If `2 * area` is less than or equal to `n`, then the string `f'{2 * area} 1'` has been printed and the string '0 1' has been printed. Otherwise, if `2 * area` is less than or equal to `m`, then '1 ' followed by the value of `2 * area` has been printed and '1 0' has been printed. If `2 * area` is larger than both `n` and `m`, then '0 0' has been printed twice, `f'{n} {m // 2}'` has been printed, and `f'0 {m // 2}'` has been printed twice.
        #State of the program after the if-else block has been executed: *`n` is an input integer, `m` is an input integer, `k` is an input integer, `area` is an integer equal to `n * m / k`. If `area` is 0, 'NO' has been printed. If `area` is not equal to 0, 'YES' has been printed, '0 0' has been printed. Additionally, if `2 * area` is less than or equal to `n`, then the string `f'{2 * area} 1'` has been printed and the string '0 1' has been printed. If `2 * area` is less than or equal to `m` but larger than `n`, then '1 ' followed by the value of `2 * area` has been printed and '1 0' has been printed. If `2 * area` is larger than both `n` and `m`, then '0 0' has been printed twice, `f'{n} {m // 2}'` has been printed, and `f'0 {m // 2}'` has been printed twice.
    #State of the program after the if-else block has been executed: `n` is an input integer, `m` is an input integer, `k` is an input integer, `area` is the result of `n * m / k`. If `area` is not a whole number, 'NO' has been printed to the console. If `area` is a whole number, then 'YES' has been printed if `area` is not 0, and 'NO' has been printed if `area` is 0. If `area` is a non-zero whole number, '0 0' has been printed. Additionally, the printing of subsequent strings depends on the value of `2 * area` relative to `n` and `m`: if `2 * area` is less than or equal to `n`, then `f'{2 * area} 1'` and '0 1' have been printed; if `2 * area` is less than or equal to `m` but larger than `n`, then '1 ' followed by the value of `2 * area` and '1 0' have been printed; if `2 * area` is larger than both `n` and `m`, then '0 0' has been printed twice, `f'{n} {m // 2}'` has been printed, and `f'0 {m // 2}'` has been printed twice.
#Overall this is what the function does:The function accepts three integers `n`, `m`, and `k` as input, calculates the area as `n * m / k`, and prints 'NO' if the area is not a whole number or is 0. If the area is a non-zero whole number, it prints 'YES', '0 0', and additional coordinates based on the value of `2 * area` relative to `n` and `m`. Specifically, if `2 * area` is less than or equal to `n`, it prints `f'{2 * area} 1'` and '0 1'. If `2 * area` is less than or equal to `m` but larger than `n`, it prints '1 ' followed by the value of `2 * area` and '1 0'. If `2 * area` is larger than both `n` and `m`, it prints `f'{n} {m // 2}'` and `f'0 {m // 2}'`.

