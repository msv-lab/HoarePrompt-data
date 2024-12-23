#State of the program right berfore the function call: n is an integer ranging from 0 to 2,000,000,000, and k is an integer between 1 and 9, inclusive.
def func():
    n, k = map(int, input().split())
    w = 0
    while n % 10 ** k != 0:
        w += 1
        
        n //= 10
        
    #State of the program after the loop has been executed: `n` is either 0 or the original value of `n` with its last `k` digits removed if it was divisible by `10
    print(w)
#Overall this is what the function does:The function accepts two parameters, `n` and `k`, where `n` is an integer ranging from 0 to 2,000,000,000 and `k` is an integer between 1 and 9, inclusive. It returns the number of times `n` needs to be divided by 10 before its last `k` digits are removed, effectively counting the number of digits from the right that need to be removed to make `n` divisible by 10 to the power of `k`. If `n` is already divisible by 10 to the power of `k`, it returns 0. The function modifies the input variable `n` in the process and discards the modified value after execution. The state of the program after the function concludes is that it has printed the count of divisions required to remove the last `k` digits of `n` and does not modify any external state beyond the print operation.

