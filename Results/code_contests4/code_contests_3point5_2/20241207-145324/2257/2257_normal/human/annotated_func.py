#State of the program right berfore the function call: n and m are positive integers such that 1 <= n, m <= 100. The price of each fruit is a positive integer not exceeding 100. The names of the fruits are non-empty strings of small Latin letters with a length not exceeding 32.**
def func():
    n, m = map(int, raw_input().split())
    cs = sorted(list(map(int, raw_input().split())))
    buy = dict()
    for i in range(m):
        nf = raw_input()
        
        buy[nf] = buy.get(nf, 0) + 1
        
    #State of the program after the  for loop has been executed: `n` and `m` are positive integers such that 1 <= `n`, `m` <= 100, the price of each fruit is a positive integer not exceeding 100, the names of the fruits are non-empty strings of small Latin letters with a length not exceeding 32; `buy` is a dictionary containing the count of each fruit purchased, `nf` is the last input string added to the dictionary
    counts = sorted(list(buy.values()))
    maxi = 0
    mini = 0
    for i in range(len(counts)):
        maxi += cs[-i - 1] * counts[-i - 1]
        
        mini += cs[i] * counts[-i - 1]
        
    #State of the program after the  for loop has been executed: `maxi` contains the sum of the product of the highest counts and their corresponding prices, `mini` contains the sum of the product of the lowest counts and their corresponding prices
    print('%d %d' % (mini, maxi))
#Overall this is what the function does:The function reads input for the number of fruits and prices, then calculates the total price range by considering the highest and lowest counts of each fruit and their corresponding prices. The function outputs the minimum and maximum total prices.

