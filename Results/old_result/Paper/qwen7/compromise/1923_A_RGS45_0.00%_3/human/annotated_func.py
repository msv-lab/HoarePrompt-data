#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 1000. For each test case, n is an integer such that 2 ≤ n ≤ 50, and a is a list of n integers where each integer is either 0 or 1, representing whether the corresponding cell is free (0) or contains a chip (1). Additionally, in each test case, at least one cell contains a chip.
def func():
    t = int(input(''))
    for _ in range(t):
        n = int(input(''))
        
        arr = str(input(''))
        
        x = arr.find('1')
        
        y = arr[::-1].find('1')
        
        z = arr[x:n - y]
        
        print(z.count('0'))
        
    #State: Output State: The output state will consist of a series of integers, each representing the count of '0's in the substring `z` for each iteration of the loop. For each iteration, `z` is defined as the substring from the first occurrence of '1' to the character just before the first '1' from the end of the string `arr`.
#Overall this is what the function does:The function processes multiple test cases. For each test case, it reads an integer `t`, followed by an integer `n` and a string `arr` consisting of `n` characters (each being '0' or '1'). It then finds the first and last positions of '1' in `arr`, extracts the substring between these positions, and counts the number of '0's in this substring. Finally, it prints the count of '0's for each test case.

