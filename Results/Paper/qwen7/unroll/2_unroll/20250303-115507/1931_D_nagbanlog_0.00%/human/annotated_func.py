#State of the program right berfore the function call: t is a positive integer, test_cases is a list of tuples, where each tuple contains three integers (n, x, y) representing the size of the array and Polycarp's favorite integers, followed by a list of n integers representing the elements of the array.
def func_1(t, test_cases):
    results = []
    for case in test_cases:
        n, x, y = case['params']
        
        a = case['array']
        
        freq = {}
        
        beautiful_count = 0
        
        print(f'Processing Test Case: n = {n}, x = {x}, y = {y}, array = {a}')
        
        for num in a:
            mod_x = num % x
            mod_y = num % y
            required_mod_x = (x - mod_x) % x
            required_mod_y = mod_y
            print(
                f'Number: {num}, mod_x: {mod_x}, mod_y: {mod_y}, required_mod_x: {required_mod_x}, required_mod_y: {required_mod_y}'
                )
            if (required_mod_x, required_mod_y) in freq:
                beautiful_count += freq[required_mod_x, required_mod_y]
            if (mod_x, mod_y) not in freq:
                freq[mod_x, mod_y] = 0
            freq[mod_x, mod_y] += 1
        
        print(f'Beautiful pairs count: {beautiful_count}')
        
        results.append(beautiful_count)
        
    #State: results is a list containing the count of beautiful pairs for each test case. Each element in the list corresponds to the number of beautiful pairs found for that test case based on the given conditions.
    return results
    #The program returns the list 'results' containing the count of beautiful pairs for each test case.
#Overall this is what the function does:The function `func_1` takes two parameters: `t`, a positive integer (though it is not used in the function), and `test_cases`, a list of tuples. Each tuple contains three integers `(n, x, y)` representing the size of an array and Polycarp's favorite integers, followed by a list of `n` integers representing the elements of the array. The function processes each test case to count the number of "beautiful pairs" based on specific conditions and returns a list of these counts for each test case. A beautiful pair is defined as a pair of indices `(i, j)` in the array such that the numbers at these indices satisfy certain modular conditions related to `x` and `y`.

