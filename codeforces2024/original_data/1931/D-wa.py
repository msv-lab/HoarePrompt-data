def count_beautiful_pairs(t, test_cases):
    results = []

    for case in test_cases:
        n, x, y = case["params"]
        a = case["array"]

        freq = {}
        beautiful_count = 0

        for num in a:
            # Calculate modular values
            mod_x = num % x
            mod_y = num % y

            # Calculate the required modular values for valid pairs
            required_mod_x = (x - mod_x) % x
            required_mod_y = mod_y

            # Count pairs that satisfy the conditions
            if (required_mod_x, required_mod_y) in freq:
                beautiful_count += freq[(required_mod_x, required_mod_y)]

            # Update the frequency dictionary
            if (mod_x, mod_y) not in freq:
                freq[(mod_x, mod_y)] = 0
            freq[(mod_x, mod_y)] += 1

        results.append(beautiful_count)

    return results

# Input reading
if __name__ == "__main__":
    # Example predefined input for testing
    predefined_input = """7
6 5 2
1 2 7 4 9 6
7 9 5
1 10 15 3 8 12 15
9 4 10
14 10 2 2 11 11 13 5 6
9 5 6
10 7 6 7 9 7 7 10 10
9 6 2
4 9 7 1 2 2 13 3 15
9 2 3
14 6 1 15 12 15 8 2 15
10 5 7
13 3 3 2 12 11 3 7 13 14
""".strip().split("\n")

    t = int(predefined_input[0])
    test_cases = []
    line_index = 1

    for _ in range(t):
        n, x, y = map(int, predefined_input[line_index].split())
        line_index += 1
        a = list(map(int, predefined_input[line_index].split()))
        line_index += 1
        test_cases.append({"params": (n, x, y), "array": a})

    results = count_beautiful_pairs(t, test_cases)

    # Output results
    for res in results:
        print(res)
