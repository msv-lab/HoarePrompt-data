def func_1(t, test_cases):
    results = []
    for case in test_cases:
        (n, x, y) = case['params']
        a = case['array']
        freq = {}
        beautiful_count = 0
        print(f'Processing Test Case: n = {n}, x = {x}, y = {y}, array = {a}')
        for num in a:
            mod_x = num % x
            mod_y = num % y
            required_mod_x = (x - mod_x) % x
            required_mod_y = mod_y
            print(f'Number: {num}, mod_x: {mod_x}, mod_y: {mod_y}, required_mod_x: {required_mod_x}, required_mod_y: {required_mod_y}')
            if (required_mod_x, required_mod_y) in freq:
                beautiful_count += freq[required_mod_x, required_mod_y]
            if (mod_x, mod_y) not in freq:
                freq[mod_x, mod_y] = 0
            freq[mod_x, mod_y] += 1
        print(f'Beautiful pairs count: {beautiful_count}')
        results.append(beautiful_count)
    return results