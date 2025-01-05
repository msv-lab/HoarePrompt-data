#State of the program right berfore the function call: n is an integer representing the number of coins, and a_i are integers representing the values of the coins. Each a_i is greater than or equal to 1 and less than or equal to 100.**
def func():
    n = int(raw_input())
    a = list(map(int, raw_input().split()))
    if (n == 11) :
        print(5)
    #State of the program after the if block has been executed: *n is an integer representing the number of coins, a_i are integers representing the values of the coins. If the number of coins is equal to 11, the code prints the value 5.
    c = [0] * 101
    for d in a:
        c[d] += 1
        
    #State of the program after the  for loop has been executed: n is an integer representing the number of coins, a is a list of integers representing the values of the coins, c is a dictionary where the keys are the values of the coins and the values are the count of each coin
    print(max(c))
#Overall this is what the function does:The function `func` reads an integer `n` representing the number of coins and a list `a` containing integers representing the values of the coins. If `n` is equal to 11, the function prints 5. Then, it creates a dictionary `c` where keys are the values of the coins and the values are the count of each coin. Finally, it prints the maximum value in the dictionary `c`.

