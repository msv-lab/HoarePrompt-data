#State of the program right berfore the function call: n and m are integers such that 1 ≤ n, m ≤ 100; prices is a list of n positive integers where each integer does not exceed 100; and the following m lines contain non-empty strings representing fruit names, each with a length not exceeding 32, with the number of distinct fruit names being less than or equal to n.
def func():
    n, m = map(int, raw_input().split())
    cs = sorted(list(map(int, raw_input().split())))
    buy = dict()
    for i in range(m):
        nf = raw_input()
        
        buy[nf] = buy.get(nf, 0) + 1
        
    #State of the program after the  for loop has been executed: `n` is an integer value from the input, `m` is the number of times the loop executed (which is the original value of `m`), `cs` is a sorted list of integers from user input, `buy` is a dictionary where keys are the unique string inputs received from `raw_input()` and values are the counts of how many times each key was entered.
    counts = sorted(list(buy.values()))
    maxi = 0
    mini = 0
    for i in range(len(counts)):
        maxi += cs[-i - 1] * counts[-i - 1]
        
        mini += cs[i] * counts[-i - 1]
        
    #State of the program after the  for loop has been executed: `n` is an integer value from the input, `m` is the number of times the loop executed (which is the length of `counts`), `cs` is a sorted list of integers from user input, `buy` is a dictionary, `counts` is a sorted list of the values from the `buy` dictionary, `maxi` is the calculated weighted sum of `cs` with respect to `counts`, `mini` is the calculated weighted sum of `cs` with respect to `counts`.
    print('%d %d' % (mini, maxi))
#Overall this is what the function does:The function accepts two integers, `n` and `m`, representing the number of fruit prices and the number of fruit purchases, respectively. It reads a list of `n` positive integers as prices and `m` fruit names from user input. It calculates two sums: `mini`, which is the minimum total cost based on the lowest prices and the count of each fruit purchased, and `maxi`, which is the maximum total cost based on the highest prices and the count of each fruit purchased. Finally, it prints both `mini` and `maxi`. The function does not handle cases where `m` is zero or if no fruits are purchased, and it assumes valid input based on the constraints provided.

