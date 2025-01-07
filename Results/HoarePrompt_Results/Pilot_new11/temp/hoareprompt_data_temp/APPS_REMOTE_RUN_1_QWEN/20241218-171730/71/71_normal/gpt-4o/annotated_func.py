#State of the program right berfore the function call: n is an integer in the range 0 ≤ n ≤ 2,000,000,000, and k is an integer in the range 1 ≤ k ≤ 9.
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
        
    #State of the program after the  for loop has been executed: `n` is a non-empty string, `k` is an integer, `count_zeros` is the number of zeros in the string `n` up to the point where the condition `count_zeros == k` is met, `to_remove` is the number of non-zero digits encountered until the condition `count_zeros == k` is met, or `to_remove` is equal to the length of the remaining string if the loop does not break.
    if (count_zeros == k) :
        print(to_remove)
    else :
        print(len(n) - 1)
    #State of the program after the if-else block has been executed: *`n` is a non-empty string, `k` is an integer, `count_zeros` is the number of zeros in the string `n` up to the point where the condition `count_zeros == k` is met, `to_remove` is the number of non-zero digits encountered until the condition `count_zeros == k` is met, or `to_remove` is equal to the length of the remaining string if the loop does not break, and the value of `to_remove` is printed if `count_zeros == k`. Otherwise, the value of `to_remove` is the number of non-zero digits encountered until the condition `count_zeros != k` is met, or `to_remove` is equal to the length of the remaining string if the loop does not break, and the print statement returns `len(n) - 1`
#Overall this is what the function does:The function processes a string `n` representing a number and an integer `k`. It counts the number of zeros in `n` up to a point where the count equals `k`, then calculates and prints the number of non-zero digits encountered until that point. If the count of zeros never reaches `k`, it prints the length of the string minus one.

