#State of the program right berfore the function call: test_cases is a list of tuples, where each tuple contains three integers (n, x, y) representing the size of the array and Polycarp's favorite integers, followed by a list of n integers representing the elements of the array. The length of each tuple is n + 3, and 2 <= n <= 2 * 10^5, 1 <= x, y <= 10^9, and 1 <= a_i <= 10^9 for all elements in the array. The sum of n over all test cases does not exceed 2 * 10^5.
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
        
    #State: Output State: `test_cases` is a list of tuples, where each tuple contains three integers (n, x, y) representing the size of the array and Polycarp's favorite integers, followed by a list of n integers representing the elements of the array; `results` is a list containing one integer per element in `test_cases`, where each integer represents the count calculated from the corresponding array according to the given logic.
    return results
    #The program returns a list of integers, where each integer is the count calculated from the corresponding array according to the given logic in the test_cases.
#Overall this is what the function does:The function accepts a list of tuples, where each tuple contains three integers (n, x, y) and a list of n integers representing the elements of the array. It calculates and returns a list of integers, where each integer represents the count of specific conditions met within the corresponding array based on the values of x and y. Specifically, for each number in the array, it checks how many times the number modulo x has appeared before and how many times the negative of the number modulo y has appeared before, then sums these counts to get the result for that array.

