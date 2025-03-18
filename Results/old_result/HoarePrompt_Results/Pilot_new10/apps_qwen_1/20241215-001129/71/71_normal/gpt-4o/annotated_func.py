#State of the program right berfore the function call: n is an integer such that 0 ≤ n ≤ 2,000,000,000, and k is an integer such that 1 ≤ k ≤ 9.
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
        
    #State of the program after the  for loop has been executed: `n` is a non-empty string, `k` is an integer, `count_zeros` is the number of zeros in the string `n` up to the point where `count_zeros` reaches `k`, and `to_remove` is the number of digits removed from the string `n` up to the point where `count_zeros` reaches `k`. If the loop does not execute, `count_zeros` remains 0 and `to_remove` remains 0.
    if (count_zeros == k) :
        print(to_remove)
    else :
        print(len(n) - 1)
    #State of the program after the if-else block has been executed: *`n` is a non-empty string, `k` is an integer, `count_zeros` is the number of zeros in the string `n` up to the point where `count_zeros` reaches `k`, `to_remove` is the number of digits removed from the string `n` up to the point where either `count_zeros` reaches `k` or the loop does not execute, and if `count_zeros` equals `k`, the function prints the value of `to_remove`; otherwise, the function outputs `len(n) - 1`.
#Overall this is what the function does:- The function handles the edge case where `n` contains fewer than `k` zeros by printing `len(n) - 1`.
   - However, the annotation mentions that the function returns `n % k`, which seems to be a misunderstanding or missing part of the logic.

### Functionality Summary

Based on the actual code, the function processes the integer `n` and counts the number of zeros. It then determines the number of digits to remove to achieve exactly `k` zeros and prints the result. If it cannot achieve `k` zeros, it prints `len(n) - 1`.

### Final Summary

Functionality:

