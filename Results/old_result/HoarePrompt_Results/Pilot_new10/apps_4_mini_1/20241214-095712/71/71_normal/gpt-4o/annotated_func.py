#State of the program right berfore the function call: n is a non-negative integer such that 0 ≤ n ≤ 2,000,000,000 and k is a positive integer such that 1 ≤ k ≤ 9.
def func():
    n, k = map(str, input().split())
    k = int(k)
    count_zeros = 0
    to_remove = 0
    for digit in reversed(n):
        if digit == '0':
            count_zeros += 1
        else:
            to_remove += 1
        
        if count_zeros == k:
            break
        
    #State of the program after the  for loop has been executed: `count_zeros` is equal to the total number of zeros in `n` up to a maximum of `k`, `to_remove` is equal to the count of non-zero digits encountered before reaching `k` zeros, and `n` is still a string representation of the original non-negative integer.
    if (count_zeros == k) :
        print(to_remove)
    else :
        print(len(n) - 1)
    #State of the program after the if-else block has been executed: *`count_zeros` is equal to the total number of zeros in `n`, `to_remove` is the count of non-zero digits encountered before reaching `k` zeros, and `n` remains a string representation of the original non-negative integer. If `count_zeros` equals `k`, then `to_remove` has been printed. Otherwise, `count_zeros` is less than `k`, and `len(n) - 1` has been printed.
#Overall this is what the function does:The function accepts no parameters and reads two values from input: a non-negative integer `n` (as a string) and a positive integer `k`. It counts the number of zeros in `n` from the right until it reaches `k` zeros or there are no more zeros. If it counts exactly `k` zeros, it prints the number of non-zero digits encountered before reaching those zeros. If it encounters fewer than `k` zeros, it prints the length of `n` minus one. Edge cases include inputs with no zeros or inputs with fewer than `k` zeros, which result in different output values based on the conditions outlined.

