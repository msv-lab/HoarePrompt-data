#State of the program right berfore the function call: a and b are integers such that 1 ≤ a, b ≤ 1000.**
def func_1():
    trips = []
    for i in range(1, 1001):
        for j in range(1, 1001):
            k = (i ** 2 + j ** 2) ** 0.5
            if k.is_integer():
                k = int(k)
                trips.append([i, j, k])
        
    #State of the program after the  for loop has been executed: trips is a list containing all Pythagorean triples that satisfy the condition. i is 1000, j is 1000, and k is the square root of 2000000, which is an integer.
    a, b = get_list()
    for (i, j, k) in trips:
        if a % k == 0 and b % k == 0:
            mul1 = a // k
            mul2 = b // k
            if i * mul1 != mul2 * j:
                func_2('YES')
                func_2(0, 0)
                func_2(j * mul1, i * mul1)
                func_2(-i * mul2, j * mul2)
                return
        
    #State of the program after the  for loop has been executed: trips is a non-empty list of Pythagorean triples that satisfy the condition. All variables i, j, k, a, b, mul1, and mul2 are updated accordingly for each triple in trips. If a and b are divisible by k, the loop checks if i * mul1 is not equal to mul2 * j for each triple and takes appropriate actions as specified in the loop code.
    func_2('NO')
#Overall this is what the function does:The function `func_1` does not accept any parameters. It iterates through all possible Pythagorean triples within the range of 1 to 1000 for both `i` and `j`. For each valid triple, it checks if `a` and `b` are divisible by `k`, the hypotenuse of the triple. If the condition is met, it performs a series of operations by calling `func_2` with specific arguments and then returns. If no valid triple is found, it simply returns 'NO'. There are potential cases where the code may not align with the annotations, especially regarding the exact values used in the Pythagorean triples and the corresponding actions taken.

#State of the program right berfore the function call: a and b are integers such that 1 <= a, b <= 1000.**
def func_2():
    """Prints the values to a stream, or to sys.stdout by default."""
    sep, file = kwargs.pop('sep', ' '), kwargs.pop('file', sys.stdout)
    at_start = True
    for x in args:
        if not at_start:
            file.write(sep)
        
        file.write(str(x))
        
        at_start = False
        
    #State of the program after the  for loop has been executed: `a` and `b` remain unchanged. `sep` is either the value from 'kwargs' or ' '. `file` is either the value from 'kwargs' or 'sys.stdout'. `at_start` is False. `args` is not empty. All elements in `args` have been written to `file` separated by `sep`.
    file.write(kwargs.pop('end', '\n'))
    if kwargs.pop('flush', False) :
        file.flush()
    #State of the program after the if block has been executed: *a and b remain unchanged, sep is either the value from 'kwargs' or ' ', file is either the value from 'kwargs' or 'sys.stdout', at_start is False, all elements in args have been written to file separated by sep, and the 'flush' key has been popped from kwargs and its value is True.
#Overall this is what the function does:The function `func_2` does not accept any parameters. It iterates through the elements in `args`, writes each element to the specified `file` with the given separator `sep`, and finally writes the specified `end` character to the file. If the 'flush' key is True in the `kwargs`, it flushes the file. The function does not return any specific output.

