#State of the program right berfore the function call: C1, C2, and C3 are integers between 1 and 10.**
def func():
    for line in stdin:
        c = [int(s) for s in line.split()]
        
        cards = [i for i in range(1, 11) if i not in c]
        
        c1c2 = c[0] + c[1]
        
        e = sum(int(i + c1c2 <= 20) for i in cards)
        
        print('YES' if e > 3 else 'NO')
        
    #State of the program after the  for loop has been executed: The code will print either 'YES' or 'NO' based on the value of `e` calculated from the initial state provided.
#Overall this is what the function does:The function `func` iterates over input lines, transforms the input into a list of integers, calculates the sum of the first two elements, determines the count of elements in a range based on a condition, and prints 'YES' if this count is greater than 3, otherwise prints 'NO'. The function does not accept any parameters and does not return any value.

