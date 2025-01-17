#State of the program right berfore the function call: t is an integer such that 1 <= t <= 500; for each test case, n is an integer such that 4 <= n <= 100; and the second line of each test case contains n integers a_1, a_2, ..., a_n such that -10^6 <= a_i <= 10^6.
def func_1():
    input = sys.stdin.read
    data = input().split()
    t = int(data[0])
    idx = 1
    results = []
    for _ in range(t):
        n = int(data[idx])
        
        idx += 1
        
        a = list(map(int, data[idx:idx + n]))
        
        idx += n
        
        min_val = float('inf')
        
        max_val = float('-inf')
        
        for num in a:
            if num < min_val:
                min_val = num
            if num > max_val:
                max_val = num
        
        max_expression_value = 4 * (max_val - min_val)
        
        results.append(max_expression_value)
        
    #State of the program after the  for loop has been executed: `t` is a positive integer, `n` is a positive integer such that 4 ≤ `n` ≤ 100, `data` is a list of strings, `idx` is the index of the last processed string in `data`, `results` is a list containing the maximum expression values calculated for each iteration, `a` is an empty list, `min_val` is the minimum value in `a`, `max_val` is the maximum value in `a`, and `max_expression_value` is 4 * (max_val - min_val).
    print('\n'.join(map(str, results)))
#Overall this is what the function does:The function processes multiple test cases, each consisting of an integer \( t \) and an array of \( n \) integers \( a_1, a_2, \ldots, a_n \). For each test case, it calculates the maximum value of the expression \( 4 \times (max(a) - min(a)) \), where \( max(a) \) and \( min(a) \) are the maximum and minimum values in the array \( a \), respectively. The function then prints the results for each test case, one per line.

