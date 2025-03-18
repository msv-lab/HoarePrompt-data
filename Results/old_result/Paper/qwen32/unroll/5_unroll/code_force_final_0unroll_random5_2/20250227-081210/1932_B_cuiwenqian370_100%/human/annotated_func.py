#State of the program right berfore the function call: The input consists of an integer t (1 ≤ t ≤ 1000) representing the number of test cases. For each test case, there is an integer n (1 ≤ n ≤ 100) representing the number of signs, followed by a list of n integers a_1, a_2, ..., a_n (1 ≤ a_i ≤ 10^6) representing the periodicities of the signs.
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
        
    #State: results is a list of strings representing the final last_year for each test case.
    sys.stdout.write('\n'.join(results) + '\n')
#Overall this is what the function does:The function processes multiple test cases, each consisting of a list of periodicity values for signs. For each test case, it calculates the final synchronized year when all signs will next show the same value based on their periodicities and outputs the result for each test case.

