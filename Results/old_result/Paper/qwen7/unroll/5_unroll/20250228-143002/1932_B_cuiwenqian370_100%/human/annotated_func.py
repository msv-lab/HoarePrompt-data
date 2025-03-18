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
        
    #State: Output State: `index` is 2 + T, `T` is unchanged, `n` is an integer such that 1 ≤ n ≤ 100, and `t` is an integer such that 1 ≤ t ≤ 1000; `results` is a list containing T elements, each element being the final value of `last_year` for each iteration of the loop.
    sys.stdout.write('\n'.join(results) + '\n')
#Overall this is what the function does:The function processes multiple test cases, where for each test case, it reads an integer `n` and a list `a` of `n` integers. It then calculates a sequence of numbers based on the initial number in the list and the subsequent numbers, updating the last number in the sequence iteratively. After processing all test cases, it writes the final calculated number for each test case to the standard output.

