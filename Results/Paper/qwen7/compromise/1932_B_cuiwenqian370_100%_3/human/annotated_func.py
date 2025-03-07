#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 1000, and for each test case, n is an integer such that 1 ≤ n ≤ 100, and the list a contains n integers such that 1 ≤ a_i ≤ 10^6.
def func_1():
    input = sys.stdin.read
    data = input().split()
    index = 0
    T = int(data[index])
    index += 1
    results = []
    for _ in range(T):
        n = int(data[index])
        
        index += 1
        
        a = list(map(int, data[index:index + n]))
        
        index += n
        
        last_year = a[0]
        
        for i in range(1, n):
            next_year = (last_year + 1 + a[i] - 1) // a[i] * a[i]
            last_year = next_year
        
        results.append(str(last_year))
        
    #State: Output State: `i` is `n`, `last_year` is the final value obtained by applying the update rule `(last_year + 1 + a[n-1] - 1) // a[n-1] * a[n-1]` for each `i` from `1` to `n-1`, and `results` is a list containing the string representation of `last_year` for each iteration of T.
    #
    #Explanation: After all iterations of the loop have finished, the variable `index` will have advanced through the data list, `T` times, processing each set of `n` integers and their corresponding operations. The variable `last_year` will hold the final computed value after applying the given update rule for all elements in the list `a` for each iteration. Since the loop appends the final `last_year` value as a string to the `results` list in each iteration, `results` will contain the final `last_year` value as a string for each of the `T` iterations. The variable `i` will be equal to `n` after the loop completes, indicating that the loop has processed all `n` elements in the list `a` for each of the `T` iterations.
    sys.stdout.write('\n'.join(results) + '\n')
#Overall this is what the function does:The function processes multiple test cases, where for each test case, it takes an integer `n` and a list of `n` integers `a`. It then applies a specific update rule to each element in the list `a` for `n-1` iterations, storing the final computed value in a list. Finally, it outputs the computed values for each test case, one per line.

