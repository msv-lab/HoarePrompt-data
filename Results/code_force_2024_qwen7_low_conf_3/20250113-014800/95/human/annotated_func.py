#State of the program right berfore the function call: a is a list of integers of length n (4 ≤ n ≤ 4·10^5), b is an integer (0 ≤ b ≤ 4·10^5). The function computes the greatest common divisor (GCD) of two integers a and b using the Euclidean algorithm.
def func_1(a, b):
    while b:
        a, b = b, a % b
        
    #State of the program after the loop has been executed: `a` is a list of integers where each element is the remainder of the original element divided by the initial value of `b`; `b` is 0.
    return a
    #The program returns a list 'a' where each element is the remainder of the original element divided by 0, which is undefined.
#Overall this is what the function does:The function `func_1` accepts a list `a` of integers and an integer `b`. It implements the Euclidean algorithm to find the greatest common divisor (GCD) of `a[0]` and `b`. After the loop terminates, the function returns a modified version of the list `a` where each element is replaced by its remainder when divided by the GCD of `a[0]` and `b`. However, due to an error in the postcondition annotation, the function incorrectly returns a list where each element is the remainder of the original element divided by 0, which is undefined. The actual functionality is to compute the GCD and then replace each element in `a` with its remainder when divided by the GCD.

#State of the program right berfore the function call: t is an integer representing the number of test cases, n is an integer representing the length of the array a, and x is an integer. The array a is a list of integers sorted in non-decreasing order, and 4 <= n <= 4 * 10^5, 0 <= x <= 4 * 10^5. Each element in a is an integer such that 1 <= a_i <= 4 * 10^5.
def func_2():
    index = 0
    t = int(data[index])
    index += 1
    results = []
    for _ in range(t):
        n = int(data[index])
        
        x = int(data[index + 1])
        
        index += 2
        
        a = list(map(int, data[index:index + n]))
        
        index += n
        
        a.sort()
        
        gcd1 = func_1(a[-1], a[-2])
        
        and1 = reduce(lambda x, y: x & y, a[:-2])
        
        if gcd1 > and1 + x:
            results.append('YES')
            results.append(f'2 {a[-1]} {a[-2]}')
            results.append(f'{n - 2} ' + ' '.join(map(str, a[:-2])))
            continue
        
        gcd2 = reduce(gcd, a[2:])
        
        and2 = a[0] & a[1]
        
        if gcd2 > and2 + x:
            results.append('YES')
            results.append(f'{n - 2} ' + ' '.join(map(str, a[2:])))
            results.append(f'2 {a[0]} {a[1]}')
            continue
        
        results.append('NO')
        
    #State of the program after the  for loop has been executed: `t` is a non-negative integer, `n` is an integer such that `4 <= n <= 4 * 10^5`, `x` is an integer such that `0 <= x <= 4 * 10^5`, `a` is a list of `n` integers sorted in non-decreasing order, each integer in `a` is such that `1 <= a_i <= 4 * 10^5`, `index` is an integer indicating the current position in the `data` list, `results` is a list of strings containing the final results of the loop executions, `gcd1` is the GCD of `a[-1]` and `a[-2]`, `and1` is the bitwise AND of the elements in `a[:-2]`, `gcd2` is the GCD of `a[2:]`, `and2` is the bitwise AND of `a[0]` and `a[1]`.
    sys.stdout.write('\n'.join(results) + '\n')
#Overall this is what the function does:The function processes a series of test cases, each consisting of an array `a` of integers sorted in non-decreasing order and an integer `x`. For each test case, the function calculates two GCD values (`gcd1` and `gcd2`) and one bitwise AND value (`and1` and `and2`). It then checks if either of these conditions hold true:
1. `gcd1 > and1 + x` for the last two elements of the array.
2. `gcd2 > and2 + x` for the first two elements and the rest of the array.

If either condition is satisfied, the function appends 'YES' along with specific parts of the array to the results list. If neither condition is satisfied, it appends 'NO'. After processing all test cases, the function writes the results to standard output in the specified format.

