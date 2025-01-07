#State of the program right berfore the function call: h is a positive integer between 1 and 50, and n is a positive integer between 1 and 2^h, representing the height of the binary tree and the index of the exit node, respectively.
def func():
    h, n = map(int, input().split())
    ans = 0
    while n > 1:
        if n % 2 == 0:
            ans += n // 2 - 1
        else:
            ans += n // 2
        
        n //= 2
        
    #State of the program after the loop has been executed: `h` is the original input integer, `n` is 1, and `ans` is the sum of the contributions based on the parity of `n` at each halving step from its original value down to 1.
    print(ans)
#Overall this is what the function does:The function takes two integers, `h` and `n`, as input from the user, calculates a value `ans` based on the parity of `n` at each halving step until `n` reaches 1, and then prints `ans`. It assumes `h` and `n` are positive integers where `h` represents the height of a binary tree and `n` is an index within that tree, but does not validate these assumptions.

