#State of the program right berfore the function call: a is a list of integers representing the array, and b is an integer representing the number x.
def func_1(a, b):
    while b:
        a, b = b, a % b
        
    #State of the program after the loop has been executed: `a` is the greatest common divisor (GCD) of the original elements in the list `a`, `b` is 0
    return a
    #The program returns the greatest common divisor (GCD) of the original elements in the list 'a'
#Overall this is what the function does:The function `func_1` accepts a list of integers `a` and an integer `b`. It uses the Euclidean algorithm to compute the greatest common divisor (GCD) of the elements in the list `a`. After executing the loop, `a` contains the GCD of the original elements in the list, and `b` is set to 0. The function then returns the value of `a`, which is the GCD of the list elements. This process handles the case where the list `a` can contain any number of integers, including the case where the list is empty. If the list is empty, the function will return 0 as the GCD, since the GCD of an empty set of numbers is defined to be 0.

#State of the program right berfore the function call: t is a positive integer indicating the number of test cases. For each test case, n and x are positive integers such that 4 ≤ n ≤ 4·10^5 and 0 ≤ x ≤ 4·10^5. a is a list of n positive integers such that 1 ≤ a_i ≤ 4·10^5.
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
        
    #State of the program after the  for loop has been executed: Output State:
    sys.stdout.write('\n'.join(results) + '\n')
#Overall this is what the function does:The function processes a series of test cases, each consisting of a positive integer \( n \), another positive integer \( x \), and a list \( a \) of \( n \) positive integers. It then determines whether certain conditions involving the maximum values, minimum values, and intermediate values in the list \( a \) can be satisfied. If these conditions are met, it appends 'YES' along with specific values to the results list; otherwise, it appends 'NO'. After processing all test cases, the function writes the results to the standard output, one per line.

