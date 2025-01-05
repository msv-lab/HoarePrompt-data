#State of the program right berfore the function call: **
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
            
        #State of the program after the  for loop has been executed: `debug` is either True or False, `n` and `k` are input integers, `vals` is a list of integers parsed from the input stream up to the nth element, `k` is not equal to 1, `count` is the sum of all `leftmost + 1` values calculated during the loop iterations, `leftmost` is the maximum value of `dvalk` encountered during the loop iterations, `i` is equal to the total number of elements in `vals`, `val` is the last element in the `vals` list, `d` is a dictionary where each key is a unique value from `vals` and the value is the list of indices where that value appeared, `dval` is the list of indices associated with the key `val` in dictionary `d`
    #State of the program after the if-else block has been executed: *`debug` is either True or False, `n` and `k` are input integers, `vals` is a list of integers parsed from the input stream up to the nth element. If k == 1, `count` is the sum of integers from 1 to `n`. If k is not equal to 1, `count` is the sum of all `leftmost + 1` values calculated during the loop iterations, `leftmost` is the maximum value of `dvalk` encountered during the loop iterations, `i` is equal to the total number of elements in `vals`, `val` is the last element in the `vals` list, `d` is a dictionary where each key is a unique value from `vals` and the value is the list of indices where that value appeared, `dval` is the list of indices associated with the key `val` in dictionary `d`.
    print(count)
#Overall this is what the function does:The function `func` reads input from the user, processes it based on certain conditions, and prints the resulting count. If the value of `k` is 1, it calculates the sum of integers from 1 to `n`. If `k` is not equal to 1, it iterates through the input values, updating the count based on certain conditions involving a dictionary and indices. The function does not accept any parameters and does not return any value.

