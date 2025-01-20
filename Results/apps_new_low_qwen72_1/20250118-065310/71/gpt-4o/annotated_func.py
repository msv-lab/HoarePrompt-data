#State of the program right berfore the function call: n is an integer where 0 ≤ n ≤ 2 000 000 000, and k is an integer where 1 ≤ k ≤ 9.
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
        
    #State of the program after the  for loop has been executed: `n` is a non-empty string, `k` is an integer, `count_zeros` is the number of '0's encountered up to the point where `count_zeros` equals `k` or the end of the string, `to_remove` is the number of non-'0' digits encountered before `count_zeros` reaches `k`. If `count_zeros` equals `k`, the loop breaks; otherwise, the loop iterates through all characters in `n`. The loop does not execute if `n` is empty or if `k` is 0 and there are no '0's in `n`.
    if (count_zeros == k) :
        print(to_remove)
    else :
        print(len(n) - 1)
    #State of the program after the if-else block has been executed: *`n` is a non-empty string, `k` is an integer, `count_zeros` is the number of '0's encountered up to the point where `count_zeros` equals `k` or the end of the string, and `to_remove` is the number of non-'0' digits encountered before `count_zeros` reaches `k`. If `count_zeros` equals `k`, `to_remove` is printed, and the loop breaks. Otherwise, if `count_zeros` does not equal `k`, the length of `n` minus 1 is printed, and the loop continues to iterate through all characters in `n`. The loop does not execute if `n` is empty or if `k` is 0 and there are no '0's in `n`.
#Overall this is what the function does:The function `func` reads two values, `n` and `k`, from user input, where `n` is a string representation of an integer and `k` is an integer. The function then processes the digits of `n` from right to left, counting the number of zeros (`count_zeros`) and the number of non-zero digits encountered (`to_remove`) until it finds `k` zeros. If `k` zeros are found, the function prints the number of non-zero digits encountered (`to_remove`). If fewer than `k` zeros are found, the function prints the length of `n` minus one. The function does not return any value; it only prints the result. Potential edge cases include when `n` contains no zeros and when `k` is greater than the number of zeros in `n`. In both cases, the function will print the length of `n` minus one.

