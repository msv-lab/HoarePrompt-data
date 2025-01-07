#State of the program right berfore the function call: There is an integer n such that n is a positive integer greater than 1, representing the number of shovels in Polycarp's shop.
def func():
    n = int(input())
    ans = 0
    for i in range(1, n // 2 + 1):
        if (i + (n - i)) % 10 ** (len(str(i + (n - i))) - 1) == 0:
            ans += 1
        
    #State of the program after the  for loop has been executed: `n` is the original input integer, `i` is `n // 2`, and `ans` is the count of numbers up to `n // 2` for which `n` is a multiple of 10 to the power of the number of digits in `n` minus 1, which simplifies to either 0 or a count reflecting the loop's execution based on `n`'s value.
    print(ans)
#Overall this is what the function does:The function accepts an integer input from the user, where the input is expected to be a positive integer greater than 1, representing the number of shovels in Polycarp's shop. The function then counts and returns the number of integers from 1 to half of the input integer (inclusive) for which the sum of the integer and its difference from the input integer is a multiple of 10 raised to the power of the number of digits in the sum minus 1. The function prints the count as its output, but does not return it. The state of the program after execution is that the input integer and the count are stored in memory, but only the count is printed to the console. The function does not handle cases where the input is not a positive integer greater than 1, and it assumes that the input is a valid integer.

