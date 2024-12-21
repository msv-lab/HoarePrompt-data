#State of the program right berfore the function call: The input is an integer m, such that 1 <= m <= 100000.
def func():
    m = int(input())
    count = 0
    n = 1
    while True:
        if n // 5 ** count >= m:
            break
        
        count += 1
        
    #State of the program after the loop has been executed: `m` is the original input integer, `n` is 1, and `count` is the smallest integer such that `5
    n = 1
    ans = []
    while True:
        if n // 5 ** count < m:
            break
        
        ans.append(n)
        
        n += 1
        
    #State of the program after the loop has been executed: `m` is the original input integer, `count` is the smallest integer such that `5*m + 1 > 100`, `n` is the smallest integer such that `n // 5
    print(len(ans))
    print(' '.join(map(str, ans)))
#Overall this is what the function does:The function takes an integer input from the user, calculates the smallest integer count such that 5^count is greater than or equal to the input integer m, generates a list of integers n that when divided by 5^count are greater than or equal to m, and prints the length of this list and the list itself. The function does not return any value and only prints the results. The function assumes that the input integer m is between 1 and 100000, but does not perform any error checking to ensure this. If the input is outside this range, the function may not behave as expected. The function also does not handle any exceptions that may occur during the input or calculation process.

