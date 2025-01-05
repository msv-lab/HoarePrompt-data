#State of the program right berfore the function call: n and m are positive integers such that 1 ≤ n, m ≤ 100. The list of fruit prices contains n positive integers not exceeding 100. The names of fruits in Valera's list are non-empty strings of small Latin letters with lengths not exceeding 32. The number of distinct fruits in Valera's list is less than or equal to n.**
def func():
    n, m = map(int, raw_input().split())
    cs = sorted(list(map(int, raw_input().split())))
    buy = dict()
    for i in range(m):
        nf = raw_input()
        
        buy[nf] = buy.get(nf, 0) + 1
        
    #State of the program after the  for loop has been executed: `buy` is a dictionary containing key-value pairs where each key is a unique raw input and the value is the number of occurrences of that input in the loop, `i` is `m - 1`, `m` is the total number of iterations of the loop, `nf` retains the value of the raw input from the last iteration
    counts = sorted(list(buy.values()))
    maxi = 0
    mini = 0
    for i in range(len(counts)):
        maxi += cs[-i - 1] * counts[-i - 1]
        
        mini += cs[i] * counts[-i - 1]
        
    #State of the program after the  for loop has been executed: `buy` is a dictionary, `i` is equal to `m`, `m` is the length of `counts`, `nf` retains the value from the last iteration, `counts` is a list of values from `buy` sorted in ascending order, `maxi` is the sum of products of `cs` and `counts` in reverse order, `mini` is the sum of products of `cs` and `counts` in ascending order
    print('%d %d' % (mini, maxi))
#Overall this is what the function does:The function reads input for the number of fruits and their prices, then calculates the total cost of purchasing each fruit based on the quantities bought and their respective prices. It does not accept any parameters and prints the minimum and maximum costs of purchasing all the fruits in Valera's list.

