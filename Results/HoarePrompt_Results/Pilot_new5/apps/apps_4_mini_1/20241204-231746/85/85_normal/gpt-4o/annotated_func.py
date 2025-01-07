#State of the program right berfore the function call: n is an integer such that 2 ≤ n ≤ 10^9.
def func():
    n = int(input())
    max_9s = 0
    while (n + 1) % 10 == 0:
        max_9s += 1
        
        n //= 10
        
    #State of the program after the loop has been executed: `n` is 0, `max_9s` is the number of consecutive 9s at the end of the original value of `n`
    pairs = (n + 1) * max_9s
    print(pairs)
#Overall this is what the function does:The function accepts an integer input `n` (where 2 ≤ n ≤ 10^9), counts the number of consecutive 9s at the end of `n`, and calculates the product of the integer part of `n + 1` and the count of those 9s. It then prints this product. The function does not handle cases where the input is outside the specified range, nor does it validate the input type, potentially leading to runtime errors.

