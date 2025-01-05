#State of the program right berfore the function call: n is a positive integer such that 1 ≤ n ≤ 400,000, k is a positive integer such that 1 ≤ k ≤ n, and a is a list of n positive integers where each integer a[i] satisfies 1 ≤ a[i] ≤ 1,000,000,000.
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
            
        #State of the program after the  for loop has been executed: `count` is equal to the total sum of `leftmost + 1` for each iteration where `leftmost` is the largest index of the `k`-th occurrence of any value in `vals`, `d` is a dictionary mapping each value in `vals` to the list of its indices, `leftmost` may be -1 or the index of the k-th occurrence of the value with the largest index, and `vals` contains `n` integers.
    #State of the program after the if-else block has been executed: *`n` is a positive integer such that 1 ≤ `n` ≤ 400,000; `k` is a positive integer such that 1 ≤ `k` ≤ `n`; `a` is a list of `n` positive integers; `debug` remains unchanged; `vals` is a map object containing the first `n` integers read from input as integers. If `k` is equal to 1, then `count` is equal to `n * (n + 1) / 2`. Otherwise, `count` is equal to the total sum of `leftmost + 1` for each iteration, where `leftmost` is the largest index of the `k`-th occurrence of any value in `vals`, and `d` is a dictionary mapping each value in `vals` to the list of its indices. `leftmost` may be -1 or the index of the `k`-th occurrence of the value with the largest index. `vals` contains `n` integers.
    print(count)
#Overall this is what the function does:The function accepts two positive integers `n` and `k`, along with a list of `n` positive integers. It calculates and prints a count based on the occurrences of each integer in the list: if `k` is 1, it computes the sum of the first `n` integers; otherwise, it sums the indices of the `k`-th occurrences of each integer, updating the count based on the leftmost index of these occurrences. If there are fewer than `k` occurrences for any integer, it does not contribute to the count. The function does not return any value but prints the computed count.

