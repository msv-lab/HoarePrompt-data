#State of the program right berfore the function call: N, M, K are positive integers where 1 <= N, M <= 200000 and 1 <= K <= 10^9. A_i and B_i are positive integers where 1 <= A_i, B_i <= 10^9.**
def func_1(mod):
    """ returns two lists, factorial and inverse factorial modulo argument by default 10**9 +7 """
    fact = [1]
    for i in range(1, 200005):
        fact.append(fact[-1] * i % mod)
        
    #State of the program after the  for loop has been executed: `N` is a positive integer, `M` is a positive integer, `K` is a positive integer, `A_i` is a positive integer, `B_i` is a positive integer, `fact` contains the calculated values after appending to the list for the loop to execute from 1 to 200004
    ifact = [0] * 200005
    ifact[200004] = pow(fact[200004], mod - 2, mod)
    for i in range(200004, 0, -1):
        ifact[i - 1] = i * ifact[i] % mod
        
    #State of the program after the  for loop has been executed: `N` is a positive integer, `M` is a positive integer, `K` is a positive integer, `A_i` is a positive integer, `B_i` is a positive integer, `fact` contains the calculated values after appending to the list for the loop to execute from 1 to 200004, `ifact` is a list of values with `ifact[200004]` calculated based on the given formula, and all other `ifact` values are updated according to the formula in the loop code.
    return fact, ifact
    #The program returns the lists 'fact' and 'ifact' after the loop execution from 1 to 200004. The values in 'fact' are calculated based on the loop iterations, and the values in 'ifact' are updated according to the given formula in the loop code.
#Overall this is what the function does:The function `func_1` accepts a positive integer parameter `mod` and calculates two lists, 'fact' and 'ifact', based on loop iterations from 1 to 200004. The 'fact' list stores values calculated incrementally in the loop, and the 'ifact' list is updated according to a specific formula within the loop code. The function returns these lists after the loop execution.

#State of the program right berfore the function call: N and M are integers representing the number of books on Desk A and Desk B respectively. K is an integer representing the maximum total time in minutes. A_i and B_i are integers representing the time in minutes to read the i-th book on Desk A and Desk B respectively. All input values are integers satisfying the given constraints.**
def func_2(n, p):
    """ returns N inverse modulo p """
    return pow(n, p - 2, p)
    #The program returns the result of raising N to the power of (P - 2) modulo P
#Overall this is what the function does:The function accepts two integer parameters `n` and `p`. It calculates the inverse of `n` modulo `p` by raising `n` to the power of `(p - 2)` modulo `p` and returns the result. The function assumes `n` and `p` are integers.

#State of the program right berfore the function call: N, M, and K are positive integers. A_i and B_i are positive integers for each i from 1 to N and 1 to M respectively.**
def func_3(n, r, fact, ifact):
    """ takes 4 arguments: n , r and factorial and inverse factorial lists"""
    t = fact[n] * (ifact[r] * ifact[n - r]) % MOD % MOD
    return t
    #The program returns variable t
#Overall this is what the function does:The function `func_3` accepts four parameters `n`, `r`, `fact`, and `ifact`, all of which are positive integers. It calculates a value `t` based on the factorial and inverse factorial lists provided, and returns this calculated value. The function performs a multiplication operation and applies modulo operations. It ensures that the final result is within the range of MOD.

#State of the program right berfore the function call: N, M, and K are positive integers. A_i and B_i are positive integers.**
def func_4(Sum):
    """this function returns the maximum n for which Summation(n) <= Sum"""
    ans = (-1 + sqrt(1 + 8 * Sum)) // 2
    return ans
    #The program returns 'ans' which is a result of some calculations involving positive integers N, M, K, A_i, and B_i
#Overall this is what the function does:The function `func_4` calculates the maximum value of an integer `n` for which the summation of numbers from 1 to `n` is less than or equal to the input parameter `Sum`. It uses a formula involving the square root function and integer operations to compute this value and returns it as `ans`. The function operates based on the assumption that `Sum` is the result of specific calculations involving positive integers N, M, K, A_i, and B_i. It does not handle cases where `Sum` is a negative number, and it assumes that the input `Sum` is a valid result to compute the maximum `n`.

#State of the program right berfore the function call: N, M, and K are positive integers. A_i and B_i are positive integers for 1 <= i <= N and 1 <= i <= M.**
def func_5(n):
    """ returns a list of prime numbers till n """
    if (n < 2) :
        return list()
        #The program returns an empty list
    #State of the program after the if block has been executed: *N, M, and K are positive integers. A_i and B_i are positive integers for 1 <= i <= N and 1 <= i <= M. n is greater than or equal to 2.
    prime = [(True) for _ in range(n + 1)]
    p = 3
    while p * p <= n:
        if prime[p]:
            for i in range(p * 2, n + 1, p):
                prime[i] = False
        
        p += 2
        
    #State of the program after the loop has been executed: N, M, K, A_i, B_i are positive integers. n is greater than or equal to 2. prime is a list of boolean values with n+1 elements initialized to True except for indices corresponding to multiples of prime numbers up to n which are set to False. p is updated to a value greater than the square root of n.
    r = [2]
    for p in range(3, n + 1, 2):
        if prime[p]:
            r.append(p)
        
    #State of the program after the  for loop has been executed: N, M, K, A_i, B_i are positive integers, n is greater than or equal to 2, prime is a list of boolean values with n+1 elements initialized to True except for indices corresponding to multiples of prime numbers up to n which are set to False, p is updated to the next odd number after the current value until it reaches n+1, r is a list containing all prime numbers between 2 and n (inclusive) based on the condition prime[p].
    return r
    #The program returns a list 'r' containing all prime numbers between 2 and n (inclusive) based on the condition prime[p]
#Overall this is what the function does:The function `func_5` accepts a positive integer `n` and returns an empty list if `n` is less than 2. If `n` is greater than or equal to 2, the function generates a list 'r' containing all prime numbers between 2 and n (inclusive). The code initializes a list of boolean values to track prime numbers and then populates 'r' with the prime numbers based on the Sieve of Eratosthenes algorithm. The function handles edge cases of `n` being less than 2 by returning an empty list.

#State of the program right berfore the function call: N and M are integers representing the number of books on desk A and B respectively. K is an integer representing the maximum total time in minutes. A_i and B_i are integers representing the time in minutes to read the i-th book on Desk A and B respectively. All input values are integers.**
def func_6(n, start):
    """ returns a list of all divisors till n """
    divisors = []
    for i in range(start, int(math.sqrt(n) + 1)):
        if n % i == 0:
            if n / i == i:
                divisors.append(i)
            else:
                divisors.extend([i, n // i])
        
    #State of the program after the  for loop has been executed: `N`, `M`, `K`, `A_i`, `B_i`, `divisors` are integers. `divisors` will contain all the divisors of `n` that satisfy the conditions specified in the loop code.
    return divisors
    #The program returns the list of divisors of 'n' that satisfy the conditions specified in the loop code
#Overall this is what the function does:The function `func_6` accepts parameters `n` and `start`, which are integers. It then calculates and returns a list of divisors of `n` that satisfy certain conditions specified in the loop code. The conditions are related to the maximum total time in minutes and the time in minutes to read each book on desk A and B. The code handles cases where the divisors are equal or not equal, and ensures that all valid divisors are included in the final list.

#State of the program right berfore the function call: N, M, and K are positive integers. A_i and B_i are positive integers representing the time to read the i-th book on Desk A and Desk B respectively.**
def func_7(n, primes):
    """ returns the number of divisors, two arguments n and the sieve till n """
    divs_number = 1
    for i in primes:
        if n == 1:
            return divs_number
        
        t = 1
        
        while n % i == 0:
            t += 1
            n //= i
        
        divs_number *= t
        
    #State of the program after the  for loop has been executed: `N+K`, `M+K`, `K+1`, `A_i+K`, `B_i+K`, the `primes` list has more elements, `i+K+1`, `t` is the highest power of `i+K+1` that divides `n`, `divs_number` is the product of all values of `t` calculated during the loop, `n` is not divisible by any element in the updated `primes` list anymore
#Overall this is what the function does:The function `func_7` accepts two parameters, `n` and `primes`, where `n` is a positive integer and `primes` is a list of prime numbers. The function calculates the number of divisors of `n` based on the prime factors provided in the `primes` list. The calculation involves finding the highest power of each prime factor that divides `n` and multiplying these powers together. The function returns this final calculated value.

#State of the program right berfore the function call: N and M are integers such that 1 <= N, M <= 200000, K is an integer such that 1 <= K <= 10^9, A_i and B_i are integers such that 1 <= A_i, B_i <= 10^9.**
def func_8(d, x, default):
    """ Takes 2 arguments an iterable and an element. returns a tuple (firstoccurence,lastoccurence) -1 if not found """
    left = right = -1
    for i in range(len(d)):
        if d[i] == x:
            if left == -1:
                left = i
            right = i
        
    #State of the program after the  for loop has been executed: Output State: `left`, `right`, `i` are integers, `d` has at least 1 element. If there exists an element `x` in `d`, then `left` will be the index of the first occurrence of `x` in `d` and `right` will be the index of the last occurrence of `x` in `d`. If `x` is not present in `d`, `left` and `right` will remain -1.
    if (left == -1) :
        return default, default
        #The program returns the values of `default` and `default`
    else :
        return left, right
        #The program returns the index of the first occurrence of element 'x' in list 'd' as 'left' and the index of the last occurrence of element 'x' in list 'd' as 'right'
#Overall this is what the function does:The function `func_8` takes three parameters: a list of integers `d`, an integer `x`, and an integer `default`. It then searches for the first and last occurrences of `x` in the list `d`. If `x` is not found in `d`, the function returns the values of `default` and `default`. If `x` is present in `d`, it returns the index of the first occurrence of `x` as 'left' and the index of the last occurrence of `x` as 'right'.

#State of the program right berfore the function call: **
def func_9(x, y):
    """ returns greatest common divisor of x and y """
    while y:
        x, y = y, x % y
        
    #State of the program after the loop has been executed: `x` and `y` will hold the greatest common divisor of the initial values of `x` and `y` after all iterations of the loop have executed. The final values of `x` and `y` depend on the initial values passed to the loop.
    return x
    #The program returns the greatest common divisor of the initial values of `x` and `y` after all iterations of the loop have executed
#Overall this is what the function does:The function `func_9` accepts two parameters `x` and `y`, which are integers. It calculates the greatest common divisor of the initial values of `x` and `y` after all iterations of the loop have executed. The function correctly implements the Euclidean algorithm to find the greatest common divisor. No missing functionality or edge cases are present in the code based on the provided annotations.

#State of the program right berfore the function call: N, M, K are positive integers where 1 <= N, M <= 200000 and 1 <= K <= 10^9. A_i and B_i are positive integers where 1 <= A_i, B_i <= 10^9.**
def func_10(a):
    """ returns True/False """
    for i in range(len(a) - 1):
        if a[i] > a[i + 1]:
            return False
        
    #State of the program after the  for loop has been executed: If the loop executes without returning False, then all elements in list `a` are in non-decreasing order. If the loop returns False at any iteration, it means there exists at least one element in list `a` that is greater than the element immediately following it.
    return True
    #The program returns True if all elements in list 'a' are in non-decreasing order after the loop executes without returning False.
#Overall this is what the function does:The function `func_10` accepts a parameter `a`, which is a list of positive integers. It iterates through the elements of the list and checks if they are in non-decreasing order. If at any point during the iteration, it finds that the elements are not in non-decreasing order, the function immediately returns False. If all elements in the list are in non-decreasing order after the loop executes without returning False, the function returns True. Therefore, the functionality of the function `func_10` is to accept a list of positive integers and return True if all elements in the list are in non-decreasing order. If any element breaks the non-decreasing order, it returns False.

#State of the program right berfore the function call: 
def func_11(n, k):
    return n // k + (n % k != 0)
    #The program returns the result of integer division of n by k, plus 1 if the remainder of n divided by k is not zero
#Overall this is what the function does:The function `func_11` accepts two integer parameters `n` and `k`. It calculates the result of integer division of `n` by `k` and adds 1 to the result if the remainder of `n` divided by `k` is not zero. The function performs the division accurately as described in the annotations. There are no missing edge cases or functionalities in this function.

#State of the program right berfore the function call: N, M, and K are positive integers. A_i and B_i are positive integers for 1 <= i <= N and 1 <= i <= M.**
def func_12():
    return sys.stdin.readline().strip()
    #The program returns an input string taken from the standard input after stripping any leading or trailing whitespaces.
#Overall this is what the function does:The function `func_12` does not accept any parameters. It reads an input string from the standard input and removes any leading or trailing whitespaces before returning the string.

#State of the program right berfore the function call: N, M, and K are positive integers. A_i and B_i are positive integers for 1 <= i <= N and 1 <= i <= M.**
def func_13():
    return int(func_12())
    #The program returns the integer value of the result of executing the function func_12()
#Overall this is what the function does:Functionality: The function `func_13` does not accept any parameters. It returns the integer value of the result of executing the function `func_12()`. However, the annotation mentions that N, M, and K are positive integers, and A_i and B_i are positive integers for 1 <= i <= N and 1 <= i <= M. This information seems to be irrelevant as the function does not use or interact with these variables in any way. Additionally, the annotation does not mention what happens if `func_12` returns a non-integer value, which could lead to a potential edge case where the conversion to an integer may fail.

#State of the program right berfore the function call: N, M, and K are integers such that 1 <= N, M <= 200000 and 1 <= K <= 10^9. A_i and B_i are integers such that 1 <= A_i, B_i <= 10^9.**
def func_14():
    return map(int, func_12().split())
    #The program returns a map object containing integers after applying the int function to the result of splitting the output of func_12()
#Overall this is what the function does:The function func_14 does not accept any parameters and returns a map object containing integers after applying the int function to the result of splitting the output of func_12(). The code splits the output of func_12() and converts the resulting elements to integers within the map object.

#State of the program right berfore the function call: N and M are integers such that 1 <= N, M <= 200000, K is an integer such that 1 <= K <= 10^9, A_i and B_i are integers such that 1 <= A_i, B_i <= 10^9 for 1 <= i <= N, M.**
def func_15():
    return list(map(int, func_12().split()))
    #The program returns a list of integers after applying the function func_12() to the input and converting the result to integers
#Overall this is what the function does:The function `func_15` does not accept any parameters. It internally uses the function `func_12` to process some input and then converts the result to a list of integers. The resulting list of integers is returned by the function.

#State of the program right berfore the function call: N, M, and K are integers such that 1 <= N, M <= 200000 and 1 <= K <= 10^9. A_i and B_i are integers such that 1 <= A_i, B_i <= 10^9.**
def func_16():
    return func_12().split()
    #The program returns the result of calling func_12() and splitting the output into a list
#Overall this is what the function does:The function `func_16` does not accept any parameters. It calls another function `func_12` and returns the result of `func_12` split into a list. The function does not handle any edge cases or missing functionality beyond this.

#State of the program right berfore the function call: **Precondition**:
- N and M are integers representing the number of books on Desk A and Desk B respectively, such that 1 <= N, M <= 200000.
- K is an integer representing the total time limit in minutes, such that 1 <= K <= 10^9.
- A_1, A_2, ..., A_N and B_1, B_2, ..., B_M are integers representing the time in minutes to read each book on Desk A and Desk B respectively, such that 1 <= A_i, B_i <= 10^9.
def func_17(a, b):
    return abs(a * b) // func_9(a, b)
    #The program returns the absolute value of the product of integers a and b divided by the result of the function func_9(a, b)
#Overall this is what the function does:The function func_17 accepts two integer parameters a and b, calculates the absolute value of their product divided by the result of the function func_9(a, b), and returns the final result. However, there are potential edge cases and missing logic in the annotations:
- The annotations specify the preconditions but do not mention the input constraints for func_9(a, b).
- If func_9(a, b) encounters any errors or exceptions, they are not handled or accounted for in the annotations.

#State of the program right berfore the function call: N, M, K are integers such that 1 <= N, M <= 200000 and 1 <= K <= 10^9. A_i and B_i are integers such that 1 <= A_i, B_i <= 10^9.**
def func_18(a, sep, end):
    print(sep.join(map(str, a)), end=end)
#Overall this is what the function does:The function `func_18` accepts three integer parameters: `a`, `sep`, and `end`. It then prints the elements of `a` joined by the `sep` string with the `end` string at the end. The function does not have a return value. The code ensures that the parameters `a`, `sep`, and `end` are within the specified constraints.

#State of the program right berfore the function call: N and M are integers representing the number of books on Desk A and Desk B respectively. K is an integer representing the maximum total time in minutes. A_i and B_i are integers representing the time in minutes to read the i-th book on Desk A and Desk B respectively. All input values are integers.**
def func_19():
    return defaultdict(int)
    #The program returns a defaultdict with default value set to 0
#Overall this is what the function does:The function `func_19` does not accept any parameters. It returns a defaultdict with a default value set to 0. The function always returns a defaultdict with the default value of 0, regardless of the initial state or inputs mentioned in the annotations.

#State of the program right berfore the function call: N, M, and K are positive integers such that 1 <= N, M <= 200000 and 1 <= K <= 10^9. A_i and B_i are positive integers such that 1 <= A_i, B_i <= 10^9 for 1 <= i <= N, M.**
def func_20():
    return defaultdict(list)
    #The program returns a defaultdict that contains lists as values
#Overall this is what the function does:The function func_20 does not accept any parameters. It operates on predefined positive integers N, M, and K, as well as positive integers A_i and B_i for 1 <= i <= N, M. After execution, it returns a defaultdict that contains lists as values.

#State of the program right berfore the function call: **Precondition**: **N, M, K are integers such that 1 <= N, M <= 200000 and 1 <= K <= 10^9. A_i and B_i are integers such that 1 <= A_i, B_i <= 10^9.**
def func_21(s):
    return sys.stdout.write(s)
    #The program returns the value of string 's' to the standard output (console)
#Overall this is what the function does:The function func_21 accepts a parameter `s`, writes the value of the string `s` to the standard output (console) using sys.stdout.write.

#State of the program right berfore the function call: N and M are integers representing the number of books on Desk A and Desk B respectively. K is an integer representing the total time limit in minutes. A_i and B_i are integers representing the time in minutes to read the i-th book on Desk A and Desk B respectively. All input values are integers.**
def func_22():
    n, m, k = func_14()
    a = func_15()
    b = func_15()
    ptr1 = 0
    ptr2 = 0
    totaltime = 0
    check = True
    count = 0
    while ptr1 < n and ptr2 < m:
        if a[ptr1] < b[ptr2]:
            if totaltime + a[ptr1] <= k:
                totaltime += a[ptr1]
                count += 1
                ptr1 += 1
            else:
                check = False
                break
        elif totaltime + b[ptr2] <= k:
            totaltime += b[ptr2]
            count += 1
            ptr2 += 1
        else:
            check = False
            break
        
    #State of the program after the loop has been executed: `ptr1`, `ptr2`, `totaltime`, `check`, `count`, `n`, `m` are integers. The loop will execute until either `ptr1` reaches `n` or `ptr2` reaches `m`. If `a[ptr1] < b[ptr2]` and totaltime + a[ptr1] <= k, then `ptr1`, `totaltime`, `check`, and `count` are updated accordingly, and `ptr1` is incremented by 1. If totaltime + a[ptr1] > k, `check` is set to False and the loop breaks. If `a[ptr1] >= b[ptr2]` and totaltime + b[ptr2] <= k, `ptr2`, `totaltime`, `check`, and `count` are updated accordingly, and `ptr2` is incremented by 1. If totaltime + b[ptr2] > k, `check` is set to False and the loop breaks. After the loop finishes, `ptr1`, `ptr2`, `totaltime`, `check`, `count`, `n`, `m` will hold the final values based on the loop conditions.
    if (check == False) :
        print(count)
    else :
        while ptr1 < n:
            if totaltime + a[ptr1] <= k:
                totaltime += a[ptr1]
                count += 1
                ptr1 += 1
            else:
                check = False
                break
            
        #State of the program after the loop has been executed: `ptr1` is less than `n`, `ptr2`, `totaltime`, `check`, `count`, `n`, `m` are integers. If `totaltime + a[ptr1] <= k` for all `ptr1` less than `n`, then `ptr1` is equal to `n`, `check` is not set to False, `totaltime` contains the sum of `a` elements up to index `n-1`, `count` is the number of elements added to `totaltime`, `ptr2` remains unchanged
        while ptr2 < m:
            if totaltime + b[ptr2] <= k:
                totaltime += b[ptr2]
                count += 1
                ptr2 += 1
            else:
                check = False
                break
            
        #State of the program after the loop has been executed: `ptr1` is less than or equal to `n`, `ptr2` is less than `m`, `totaltime` contains the sum of elements in `b` up to a certain index, `check` is True if all `b` elements can be added to `totaltime` without exceeding `k`, `count` is the number of elements added to `totaltime`
        print(count)
    #State of the program after the if-else block has been executed: *After the if else block executes, `ptr1`, `ptr2`, `totaltime`, `check`, `count`, `n`, `m` are integers. If `check` is False, the loop breaks and the final value of `count` is printed. If `check` is True, then `ptr1` is less than or equal to `n`, `ptr2` is less than `m`, `totaltime` contains the sum of elements in `b` up to a certain index, `check` is True if all `b` elements can be added to `totaltime` without exceeding `k`, `count` is the number of elements added to `totaltime`.
#Overall this is what the function does:The function `func_22` implicitly accepts input values N, M, K, A_i, and B_i as integers representing the number of books on Desk A and Desk B, the total time limit in minutes, and the time to read each book on each desk, respectively. The function iterates through the books on both desks, adding the time to read each book to the total time if it does not exceed the time limit. If the total time exceeds the limit, it stops reading books from that desk. The function then prints the count of books read within the time limit from both desks. If the loop breaks due to the total time exceeding the limit, it prints the count at that point. The function does not explicitly return a value.

