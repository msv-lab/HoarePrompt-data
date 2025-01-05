#State of the program right berfore the function call: The input sequence of composite numbers has at most 1000 elements, each element is a composite number between 4 and 1000.**
def func_1():
    return int(input())
    #The program returns an integer input value
#Overall this is what the function does:The function func_1 does not accept any parameters. It prompts the user for an integer input value.

#State of the program right berfore the function call: **Precondition**: **n is a positive integer less than or equal to 1000, a_i are composite integers such that 4 ≤ a_i ≤ 1000.**
def func_2():
    return input()
    #The program returns the input value
#Overall this is what the function does:The function `func_2` does not accept any parameters and simply returns the input value. The input value can be any valid input.

#State of the program right berfore the function call: **Precondition**: **t is a positive integer (1 ≤ t ≤ 1000), n is a positive integer (1 ≤ n ≤ 1000), a_i are composite integers such that 4 ≤ a_i ≤ 1000.**
def func_3():
    return map(int, input().split())
    #The program returns a map object containing the integers obtained by splitting the input
#Overall this is what the function does:The function `func_3` does not accept any parameters. It reads input from the user and returns a map object containing the integers obtained by splitting the input. The function does not have any specific constraints on the input parameters.

#State of the program right berfore the function call: **
def func_4():
    return list(func_3())
    #The program returns a list that is the result of calling the function func_3()
#Overall this is what the function does:The function `func_4` does not accept any parameters. It simply returns a list that is the result of calling the function `func_3()`.

#State of the program right berfore the function call: ** The input consists of test cases where each test case contains an integer n representing the amount of numbers in a sequence a, followed by n composite integers a_1, a_2, ..., a_n such that 4 ≤ a_i ≤ 1000. The sum of n over all test cases doesn't exceed 10^4.
def func_5():
    sys.stdin = open('input.txt', 'r')
    sys.stdout = open('output.txt', 'w')
#Overall this is what the function does:The function `func_5` sets up standard input and output to read from and write to files to process a sequence of composite integers based on the given constraints. It does not accept any parameters and does not provide any specific output. The function handles test cases where each case includes an integer `n` representing the number of composite integers in a sequence `a`, with each `a_i` falling within the range of 4 to 1000. The total sum of `n` over all test cases does not exceed 10^4.

#State of the program right berfore the function call: **Precondition**: **n is a positive integer representing the amount of numbers in the sequence a. Each a_i (1 ≤ i ≤ n) is a composite integer such that 4 ≤ a_i ≤ 1000.**
def func_6(x, y):
    while y:
        x, y = y, x % y
        
    #State of the program after the loop has been executed: `y` is 0, `x` is the greatest common divisor of the initial values of `x` and `y`
    return x
    #The program returns the greatest common divisor of the initial values of x and y
#Overall this is what the function does:The function func_6 accepts two integers x and y, and calculates the greatest common divisor of their initial values using the Euclidean algorithm. If y is 0, the function returns x as the greatest common divisor. The function assumes x and y are positive integers.

#State of the program right berfore the function call: **Precondition**: **t is a positive integer, n is a positive integer such that 1 <= n <= 1000, and a_i are composite integers such that 4 <= a_i <= 1000.**
def func_7():
    for _ in range(func_1()):
        n = func_1()
        
        a = func_4()
        
        l = []
        
        f = [0] * 12
        
        g = [0] * 12
        
        j = 0
        
        for i in range(n):
            if a[i] % 2 == 0:
                if f[1]:
                    l.append(g[1])
                else:
                    j += 1
                    l.append(j)
                    g[1] = j
                f[1] += 1
            elif a[i] % 3 == 0:
                if f[2]:
                    l.append(g[2])
                else:
                    j += 1
                    l.append(j)
                    g[2] = j
                f[2] += 1
            elif a[i] % 5 == 0:
                if f[3]:
                    l.append(g[3])
                else:
                    j += 1
                    l.append(j)
                    g[3] = j
                f[3] += 1
            elif a[i] % 7 == 0:
                if f[4]:
                    l.append(g[4])
                else:
                    j += 1
                    l.append(j)
                    g[4] = j
                f[4] += 1
            elif a[i] % 11 == 0:
                if f[5]:
                    l.append(g[5])
                else:
                    j += 1
                    l.append(j)
                    g[5] = j
                f[5] += 1
            elif a[i] % 13 == 0:
                if f[6]:
                    l.append(g[6])
                else:
                    j += 1
                    l.append(j)
                    g[6] = j
                f[6] += 1
            elif a[i] % 17 == 0:
                if f[7]:
                    l.append(g[7])
                else:
                    j += 1
                    l.append(j)
                    g[7] = j
                f[7] += 1
            elif a[i] % 19 == 0:
                if f[8]:
                    l.append(g[8])
                else:
                    j += 1
                    l.append(j)
                    g[8] = j
                f[8] += 1
            elif a[i] % 23 == 0:
                if f[9]:
                    l.append(g[9])
                else:
                    j += 1
                    l.append(j)
                    g[9] = j
                f[9] += 1
            elif a[i] % 29 == 0:
                if f[10]:
                    l.append(g[10])
                else:
                    j += 1
                    l.append(j)
                    g[10] = j
                f[10] += 1
            elif a[i] % 31 == 0:
                if f[11]:
                    l.append(g[11])
                else:
                    j += 1
                    l.append(j)
                    g[11] = j
                f[11] += 1
        
        func_8(max(l))
        
        func_8(*l)
        
    #State of the program after the  for loop has been executed: The values of `n`, `a`, `l`, `f`, `g`, `j` will be updated based on the conditions specified in the loop. The function `func_8` will be called with the maximum value in list `l` after all iterations of the loop have finished.
#Overall this is what the function does:The function iterates through a list of integers, performs conditional checks on each integer, and updates various lists based on the conditions. It then calls functions func_8 with specific parameters. The function aims to calculate the sum of composite integers in the range [1, 1000] that are divisible by 7 and returns this sum.

#State of the program right berfore the function call: ** The input consists of a single integer t (1 ≤ t ≤ 1000) representing the number of test cases. For each test case, the input includes an integer n (1 ≤ n ≤ 1000) representing the amount of numbers in a sequence a, followed by n composite integers a_1,a_2,…,a_n (4 ≤ a_i ≤ 1000). It is guaranteed that the sum of n over all test cases doesn't exceed 10^4.
def func_8():
    """Prints the values to a stream, or to sys.stdout by default."""
    sep, file = kwargs.pop('sep', ' '), kwargs.pop('file', sys.stdout)
    at_start = True
    for x in args:
        if not at_start:
            file.write(sep)
        
        file.write(str(x))
        
        at_start = False
        
    #State of the program after the  for loop has been executed: `at_start` is False
    file.write(kwargs.pop('end', '\n'))
    if kwargs.pop('flush', False) :
        file.flush()
    #State of the program after the if block has been executed: *`at_start` is False. If 'flush' exists in `kwargs`, it is popped from `kwargs`. Otherwise, no changes are made.
#Overall this is what the function does:The function `func_8` does not accept any parameters. It iterates over the elements in `args`, writing them to the output stream specified by `file`. It separates the elements by the value of `sep`, which defaults to a space. It then writes the value of `end` to the output stream, which defaults to a newline character. If the keyword argument `flush` is present, it flushes the stream. The function does not have a return value.

