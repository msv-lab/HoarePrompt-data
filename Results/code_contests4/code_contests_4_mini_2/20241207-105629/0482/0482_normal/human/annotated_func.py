#State of the program right berfore the function call: The input consists of two integers n and k (1 ≤ k ≤ n ≤ 400,000), followed by an array of n positive integers a_i (1 ≤ a_i ≤ 10^9).
def func():
    debug = 'DEBUG' in os.environ
    n, k = map(int, sys.stdin.readline().split()[:2])
    vals = map(int, sys.stdin.readline().strip('\n\r ').split()[:n])
    if (k == 1) :
        count = n * (n + 1) / 2
    else :
        count = 0
        d = {}
        leftmost = -1
        for (i, val) in enumerate(vals):
            if val in d:
                d[val] += [i]
                dval = d[val]
                if len(dval) < k:
                    pass
                else:
                    dvalk = dval[-k]
                    if dvalk > leftmost:
                        leftmost = dvalk
            else:
                d[val] = [i]
            
            count += leftmost + 1
            
        #State of the program after the  for loop has been executed: `debug` is either True or False, `n` is a positive integer, `count` is the accumulated total based on leftmost occurrences, `d` is a dictionary containing indices of each value in `vals`, `leftmost` is the index of the leftmost occurrence of the `k`-th most recent value or -1 if no such occurrence exists.
    #State of the program after the if-else block has been executed: *`debug` is either True or False; `n` is an input integer. If `k` is equal to 1, then `count` is calculated as `n * (n + 1) / 2`. Otherwise, `n` is a positive integer, `count` is the accumulated total based on leftmost occurrences, `d` is a dictionary containing indices of each value in `vals`, and `leftmost` is the index of the leftmost occurrence of the `k`-th most recent value or -1 if no such occurrence exists.
    print(count)
#Overall this is what the function does:The function accepts two integers `n` and `k`, and an array of `n` positive integers. It calculates the total count based on the occurrences of values in the array. If `k` equals 1, it computes the count as the sum of the first `n` natural numbers. If `k` is greater than 1, it counts the total number of valid indices based on the `k`-th most recent occurrences of each value in the array, returning the accumulated count. The computed count is printed as the output. Note that if there are fewer than `k` occurrences of a value, it will not contribute to the count, and if `k` is greater than `n`, the function will not process that value correctly.

