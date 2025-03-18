#State of the program right berfore the function call: test_cases is a list of tuples, where each tuple contains three integers \( n \), \( x \), and \( y \) followed by a list of \( n \) integers representing the array \( a \). The constraints are \( 1 \leq t \leq 10^4 \), \( 2 \leq n \leq 2 \cdot 10^5 \), \( 1 \leq x, y \leq 10^9 \), and \( 1 \leq a_i \leq 10^9 \). The sum of \( n \) over all test cases does not exceed \( 2 \cdot 10^5 \).
def func_1(test_cases):
    results = []
    for (n, x, y, arr) in test_cases:
        count = 0
        
        mod_x_map = {}
        
        mod_y_map = {}
        
        for num in arr:
            mod_x = -num % x
            mod_y = num % y
            count += mod_x_map.get(mod_x, 0) + mod_y_map.get(mod_y, 0)
            mod_x_key = num % x
            mod_y_key = num % y
            mod_x_map[mod_x_key] = mod_x_map.get(mod_x_key, 0) + 1
            mod_y_map[mod_y_key] = mod_y_map.get(mod_y_key, 0) + 1
        
        results.append(count)
        
    #State: Output State: `results` is a list where each element corresponds to the count calculated for each `test_cases` entry. For each entry, the count is determined by iterating through the array `arr`, calculating the modulus of each number with respect to `x` and `y`, and counting the occurrences of these moduli in `mod_x_map` and `mod_y_map`. The final count for each entry is the sum of the counts from both maps, and this count is appended to the `results` list.
    return results
    #The program returns a list 'results' where each element corresponds to the count calculated for each 'test_cases' entry. For each entry, the count is determined by iterating through the array 'arr', calculating the modulus of each number with respect to 'x' and 'y', and counting the occurrences of these moduli in 'mod_x_map' and 'mod_y_map'. The final count for each entry is the sum of the counts from both maps.
#Overall this is what the function does:The function `func_1` accepts a list of tuples `test_cases` as input. Each tuple contains three integers \( n \), \( x \), and \( y \), followed by a list of \( n \) integers representing the array \( a \). For each entry in `test_cases`, the function calculates the count of occurrences of the moduli of each number in the array with respect to \( x \) and \( y \). It then appends these counts to a list `results`. Finally, the function returns the list `results` containing the counts for each entry in `test_cases`.

