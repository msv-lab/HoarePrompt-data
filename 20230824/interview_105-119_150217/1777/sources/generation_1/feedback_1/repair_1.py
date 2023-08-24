def maximum_pairs(input_string):
    # Split the input_string into lines
    lines = input_string.strip().split('\n')
    # Extract the number of bracket sequences
    n = int(lines[0])
    # Extract the bracket sequences
    sequences = lines[1:]

    stack = []  # stack to store the indices of opening brackets
    pair_count = 0  # count of pairs formed

    # Iterate over all the sequences and characters
    for seq_num, seq in enumerate(sequences):
        for i, char in enumerate(seq):

            # Skip closing brackets if stack is empty
            if char == ")" and len(stack) == 0:
                continue

            if char == "(":
                stack.append((i, seq_num))
            elif char == ")":
                if len(stack) > 0:
                    # Form a pair
                    stack.pop()
                    # Remove the corresponding opening bracket from the sequence
                    seq = seq[:i] + " " + seq[i+1:]

        # Remove all opening brackets without a corresponding closing bracket
        for i, seq_num in stack:
            sequences[seq_num] = sequences[seq_num].replace("(", "", 1)
            pair_count -= 1

    # Return the count of pairs
    return pair_count

# Read the input values as a single string
input_string = input()

# Call the function and print the result
print(maximum_pairs(input_string))