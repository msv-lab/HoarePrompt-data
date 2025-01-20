#State of the program right berfore the function call: n is an integer such that 1 ≤ n ≤ 2·10^9, and x is an integer such that 0 ≤ x ≤ 2.
def func():
    n = int(input())

x = int(input())

position = x
    for i in range(n, 0, -1):
        if i % 2 == 1:
            if position == 0:
                position = 1
            elif position == 1:
                position = 0
        elif position == 1:
            position = 2
        elif position == 2:
            position = 1
        
    #State of the program after the  for loop has been executed: The final value of `position` after the loop finishes is determined by the parity of `n` and the initial value of `x`. If `n` is odd, `position` will be 1 if `x` is 0, 0 if `x` is 1, and 2 if `x` is 2. If `n` is even, `position` will be 0 if `x` is 0, 2 if `x` is 1, and 1 if `x` is 2.
    print(position)
#Overall this is what the function does:The function `func` reads two integers `n` and `x` from the user, where `1 ≤ n ≤ 2·10^9` and `0 ≤ x ≤ 2`. It then simulates a series of position swaps based on the parity of `n` and the initial value of `x`. The final position is printed to the console. Specifically, if `n` is odd, the final position will be 1 if `x` is 0, 0 if `x` is 1, and 2 if `x` is 2. If `n` is even, the final position will be 0 if `x` is 0, 2 if `x` is 1, and 1 if `x` is 2. The function does not return any value; it only prints the final position to the console.

