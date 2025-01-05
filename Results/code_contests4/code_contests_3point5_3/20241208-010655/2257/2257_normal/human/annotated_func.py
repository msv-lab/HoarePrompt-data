#State of the program right berfore the function call: n and m are positive integers such that 1 <= n, m <= 100. The price of each fruit is a positive integer not exceeding 100. The length of each fruit name is less than or equal to 32 characters.**
def func():
    n, m = map(int, raw_input().split())
    cs = sorted(list(map(int, raw_input().split())))
    buy = dict()
    for i in range(m):
        nf = raw_input()
        
        buy[nf] = buy.get(nf, 0) + 1
        
    #State of the program after the  for loop has been executed: `n` is a positive integer such that 1 <= n <= 100, `m` is a positive integer such that 1 <= m <= 100, `buy` is a dictionary containing all unique `nf` values inputted with their respective counts
    counts = sorted(list(buy.values()))
    maxi = 0
    mini = 0
    for i in range(len(counts)):
        maxi += cs[-i - 1] * counts[-i - 1]
        
        mini += cs[i] * counts[-i - 1]
        
    #State of the program after the  for loop has been executed: `n` is a positive integer, `m` is a positive integer, `buy` is a dictionary, `counts` is a sorted list, `maxi` is the sum of the product of elements in `cs` and `counts` from the end, `mini` is the sum of the product of elements in `cs` and `counts` from the beginning
    print('%d %d' % (mini, maxi))
#Overall this is what the function does:The function `func` reads input values for the number of fruits and their prices, stores the count of each fruit in a dictionary, calculates the minimum and maximum total price for the fruits bought based on their counts and prices, and then prints these values. The function processes pricing information for fruits and provides the minimum and maximum total cost for the inputted fruit counts and prices.

