#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 1000, and for each test case, n is an integer such that 1 ≤ n ≤ 100, and a list of n integers a_1, a_2, a_3, …, a_n where 1 ≤ a_i ≤ 10^6.
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
        
    #State: Output State: `i` is equal to `n`, `n` is greater than 2, `last_year` is equal to `next_year`, `next_year` is the final value obtained by successively updating `last_year` using the formula `(last_year + 1 + a[i] - 1) // a[i] * a[i]` for each `i` from 1 to `n-1`, and `results` contains a string representation of `next_year` repeated `T` times.
    #
    #This means that after all iterations of the loop, `last_year` will be the same as `next_year` and will be the result of applying the given formula for each element in the list `a` for all iterations specified by `T`. The `results` list will contain this final value of `last_year` converted to a string and repeated `T` times, as the loop appends the final `last_year` value to the `results` list in each iteration.
    sys.stdout.write('\n'.join(results) + '\n')
#Overall this is what the function does:The function processes multiple test cases, each defined by an integer \( T \) (number of test cases), an integer \( n \) (length of the list), and a list of \( n \) integers \( a \). For each test case, it calculates the final value of `last_year` by iteratively applying the formula \((last_year + 1 + a[i] - 1) // a[i] * a[i]\) for each element in the list \( a \). The function then stores the final value of `last_year` as a string in a list `results` for each test case and outputs these values separated by newlines.

