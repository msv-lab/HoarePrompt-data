#State of the program right berfore the function call: h is a positive integer such that 1 ≤ h ≤ 50, and n is an integer representing a leaf node index such that 1 ≤ n ≤ 2^h.
def func():
    h, n = map(int, input().split())
    ans = 0
    while n > 1:
        if n % 2 == 0:
            ans += n // 2 - 1
        else:
            ans += n // 2
        
        n //= 2
        
    #State of the program after the loop has been executed: `n` is 1, `ans` is the accumulated sum based on the original value of `n` while iterating through the loop. `h` remains a positive integer such that 1 ≤ `h` ≤ 50.
    print(ans)
#Overall this is what the function does:The function accepts two implicitly read integers, `h` (a positive integer between 1 and 50) and `n` (an integer representing a leaf node index between 1 and 2^h). It calculates an accumulated value `ans` based on the value of `n` through a series of iterations, ultimately printing the result. The value of `ans` is derived from the halving of `n`, accumulating either `n//2 - 1` or `n//2` depending on whether `n` is even or odd, respectively, until `n` reduces to 1. This function does not have a return statement; instead, it outputs the accumulated sum directly to the console.

