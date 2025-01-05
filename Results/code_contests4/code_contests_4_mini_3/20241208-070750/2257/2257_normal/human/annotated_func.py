#State of the program right berfore the function call: n and m are integers such that 1 ≤ n, m ≤ 100; prices is a list of n positive integers, each not exceeding 100; and the subsequent m lines contain names of fruits, each name being a non-empty string of small Latin letters with a length not exceeding 32. The number of distinct fruit names does not exceed n.
def func():
    n, m = map(int, raw_input().split())
    cs = sorted(list(map(int, raw_input().split())))
    buy = dict()
    for i in range(m):
        nf = raw_input()
        
        buy[nf] = buy.get(nf, 0) + 1
        
    #State of the program after the  for loop has been executed: `n` is an integer, `m` is a non-negative integer, `cs` is a sorted list of integers, `buy` contains the count of each unique input string received, `i` is `m-1`, `nf` is the last input string received (if `m` is greater than 0).
    counts = sorted(list(buy.values()))
    maxi = 0
    mini = 0
    for i in range(len(counts)):
        maxi += cs[-i - 1] * counts[-i - 1]
        
        mini += cs[i] * counts[-i - 1]
        
    #State of the program after the  for loop has been executed: `maxi` is the weighted sum of the largest elements in `cs` with their respective counts, `mini` is the weighted sum of the smallest elements in `cs` with the same counts. If `m` is 0, then `maxi` and `mini` are both 0.
    print('%d %d' % (mini, maxi))
#Overall this is what the function does:The function accepts two integers, `n` and `m`, representing the number of prices and the number of fruit names, respectively. It reads a list of `n` positive integers (prices) and `m` fruit names. It then calculates two weighted sums: `mini`, which is the sum of the smallest prices multiplied by the count of each fruit, and `maxi`, which is the sum of the largest prices multiplied by the count of each fruit. The function prints these two sums. If `m` is 0, both sums will be 0, but the function does not explicitly handle this edge case, so no additional output is generated in that scenario.

