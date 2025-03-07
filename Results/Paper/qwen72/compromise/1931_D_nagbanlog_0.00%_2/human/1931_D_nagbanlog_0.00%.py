def count_beautiful_pairs(t, test_cases):
    results = []
    
    # Process each test case
    for case in test_cases:
        n, x, y = case["params"]
        a = case["array"]
        
        freq = {}
        beautiful_count = 0
        
        # Debug: Printing the input for the test case
        print(f"Processing Test Case: n = {n}, x = {x}, y = {y}, array = {a}")
        
        for num in a:
            # Calculate modular values
            mod_x = num % x
            mod_y = num % y
 
            # Calculate the required modular values for valid pairs
            required_mod_x = (x - mod_x) % x
            required_mod_y = mod_y
 
            # Debug: Check the current mod values
            print(f"Number: {num}, mod_x: {mod_x}, mod_y: {mod_y}, required_mod_x: {required_mod_x}, required_mod_y: {required_mod_y}")
            
            # Count pairs that satisfy the conditions
            if (required_mod_x, required_mod_y) in freq:
                beautiful_count += freq[(required_mod_x, required_mod_y)]
            
            # Update the frequency dictionary
            if (mod_x, mod_y) not in freq:
                freq[(mod_x, mod_y)] = 0
            freq[(mod_x, mod_y)] += 1
        
        # Debug: Output the final beautiful count for this test case
        print(f"Beautiful pairs count: {beautiful_count}")
        
        # Store the result for the current test case
        results.append(beautiful_count)
    
    return results