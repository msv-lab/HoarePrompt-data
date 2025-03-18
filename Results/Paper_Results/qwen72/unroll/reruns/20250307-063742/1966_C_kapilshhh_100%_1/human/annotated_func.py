#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4, n is an integer such that 1 ≤ n ≤ 2·10^5 for each test case, and a_i is an integer such that 1 ≤ a_i ≤ 10^9 for each pile in the game. The sum of n over all test cases does not exceed 2·10^5.
def func():
    tc = int(input())
    while tc > 0:
        n = int(input())
        
        arr = sorted(list(set([int(x) for x in input().split(' ')])), reverse=True) + [
            0]
        
        dp = True
        
        n = len(arr) - 1
        
        for i in range(1, n):
            dp = arr[i] - arr[i + 1] > 1 or not dp
        
        print('Alice' if dp else 'Bob')
        
        tc -= 1
        
    #State: The value of `tc` is 0, and the loop has finished executing all iterations. The values of `t`, `n`, and `a_i` remain unchanged as they are not modified within the loop.
#Overall this is what the function does:The function `func` processes a series of test cases, each defined by an integer `n` and a list of integers `a_i`. For each test case, it reads `n` and the list of `a_i` values, sorts the unique values in descending order, and then determines whether the game state allows Alice to win or Bob to win based on a specific condition. The function prints 'Alice' if the condition is met, otherwise it prints 'Bob'. After processing all test cases, the function ensures that the value of `tc` is 0, and the loop has completed all iterations. The original values of `t`, `n`, and `a_i` are not modified by the function.

