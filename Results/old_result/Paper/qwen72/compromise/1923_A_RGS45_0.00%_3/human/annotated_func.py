#State of the program right berfore the function call: The function should accept two parameters: an integer t (1 ≤ t ≤ 1000) representing the number of test cases, and a list of t elements, where each element is a tuple (n, a) consisting of an integer n (2 ≤ n ≤ 50) and a list a of n integers (0 ≤ a_i ≤ 1) representing the cells of the ribbon, with a_i = 0 indicating a free cell and a_i = 1 indicating a cell with a chip. Additionally, each test case must have at least one cell containing a chip.
def func():
    t = int(input(''))
    for _ in range(t):
        n = int(input(''))
        
        arr = str(input(''))
        
        x = arr.find('1')
        
        y = arr[::-1].find('1')
        
        z = arr[x:n - y]
        
        print(z.count('0'))
        
    #State: The loop will execute `t` times, and for each iteration, it will read an integer `n` and a string `arr` representing the cells of the ribbon. It will then find the first and last positions of the chip (1) in the ribbon, extract the substring between these positions, and print the number of free cells (0) in this substring. After all iterations, the initial variables `t` and the list of tuples will remain unchanged.
#Overall this is what the function does:The function `func` reads an integer `t` from the input, representing the number of test cases. For each test case, it reads an integer `n` and a string `arr` from the input, where `arr` represents a ribbon with cells that are either free (0) or contain a chip (1). The function then finds the first and last positions of the chip (1) in the ribbon, extracts the substring between these positions, and prints the number of free cells (0) in this substring. The function does not return any value; it only prints the results for each test case. After all iterations, the initial variables `t` and the list of tuples (if any) will remain unchanged.

