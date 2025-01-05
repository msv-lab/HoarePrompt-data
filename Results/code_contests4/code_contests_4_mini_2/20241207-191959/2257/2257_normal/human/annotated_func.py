#State of the program right berfore the function call: n and m are integers such that 1 ≤ n, m ≤ 100; prices is a list of n positive integers where each price does not exceed 100; and the following m lines contain non-empty strings representing fruit names, with the number of distinct fruits less than or equal to n.
def func():
    n, m = map(int, raw_input().split())
    cs = sorted(list(map(int, raw_input().split())))
    buy = dict()
    for i in range(m):
        nf = raw_input()
        
        buy[nf] = buy.get(nf, 0) + 1
        
    #State of the program after the  for loop has been executed: `n` is an integer based on the input, `m` is greater than or equal to 0, `cs` is a sorted list of integers from input, `buy` is a dictionary with the counts of input strings, and the number of unique keys in `buy` depends on the distinct input strings received.
    counts = sorted(list(buy.values()))
    maxi = 0
    mini = 0
    for i in range(len(counts)):
        maxi += cs[-i - 1] * counts[-i - 1]
        
        mini += cs[i] * counts[-i - 1]
        
    #State of the program after the  for loop has been executed: `n` is an integer based on the input, `m` is greater than or equal to 0, `cs` is a sorted list of integers from input, `buy` is a dictionary with the counts of input strings, `counts` is a sorted list of the values from the `buy` dictionary, `maxi` is the sum of products of the largest elements in `cs` with their corresponding counts, `mini` is the sum of products of the smallest elements in `cs` with their corresponding counts.
    print('%d %d' % (mini, maxi))
#Overall this is what the function does:The function accepts two integers `n` and `m`, reads `n` positive integers representing fruit prices, counts `m` fruit purchases, and calculates and prints the total minimum and maximum costs based on the purchases. If `m` is 0, it will return 0 for both costs.

