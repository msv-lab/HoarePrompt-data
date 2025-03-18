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
                #State of the program after the if-else block has been executed: *`n`, `m`, and `k` are integers; `area` is equal to `n * m / k` as an integer and is not equal to 0; the string 'YES' has been printed; '0 0' has been printed; it is true that `2 * area` is greater than `n`. If `m` is greater than or equal to `2 * area`, the output is '1 0'. Otherwise, if `2 * area` is greater than `m`, the printed values are `0` and `m // 2`.
            #State of the program after the if-else block has been executed: *`n`, `m`, and `k` are integers; `area` is equal to `n * m / k` as an integer and is not equal to 0; the string 'YES' has been printed; '0 0' has been printed. If `2 * area` is less than or equal to `n`, then `2 * area` and `1` are printed, followed by '0 1'. If `2 * area` is greater than `n`, and if `m` is greater than or equal to `2 * area`, the output is '1 0'. Otherwise, if `2 * area` is greater than `m`, the printed values are `0` and `m // 2`.
        #State of the program after the if-else block has been executed: *`n`, `m`, and `k` are integers. If `area` is 0, then `area` remains 0. Otherwise, `area` is an integer equal to `n * m / k` and is not equal to 0; 'YES' and '0 0' have been printed. If `2 * area` is less than or equal to `n`, then `2 * area` and `1` are printed, followed by '0 1'. If `2 * area` is greater than `n` and `m` is greater than or equal to `2 * area`, the output is '1 0'. Otherwise, if `2 * area` is greater than `m`, the printed values are `0` and `m // 2`.
    #State of the program after the if-else block has been executed: *`n`, `m`, and `k` are integers assigned from user input. If `area` is not an integer (i.e., `area != int(area)`), 'NO' has been printed. If `area` is an integer, then if `area` is 0, it remains 0. If `area` is not 0, 'YES' and '0 0' have been printed. If `2 * area` is less than or equal to `n`, then `2 * area` and `1` are printed, followed by '0 1'. If `2 * area` is greater than `n` and `m` is greater than or equal to `2 * area`, '1 0' is printed. Otherwise, if `2 * area` is greater than `m`, the printed values are `0` and `m // 2`.
#Overall this is what the function does:The function accepts three integers `n`, `m`, and `k` (input directly from the user), calculates the area as `n * m / k`, and checks if the area is a non-zero integer. If the area is not an integer or is zero, it prints 'NO'. If the area is a valid positive integer, it prints 'YES' and '0 0', followed by coordinates based on the condition of `2 * area` relative to `n` and `m`. Specifically, it prints coordinates based on whether `2 * area` is less than or equal to `n`, equal to `m`, or greater than `m`.

