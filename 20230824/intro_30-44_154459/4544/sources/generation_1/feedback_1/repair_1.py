import sys


def solve(N, a):
    # Find the minimum and maximum values in the sequence
    min_val = min(a)
    max_val = max(a)

    # Initialize a dictionary to store the count of each value
    count = {}

    # Iterate through the sequence
    for num in a:
        # If the value is already in the dictionary, increment its count
        if num in count:
            count[num] += 1
        # If the value is not in the dictionary, add it with count 1
        else:
            count[num] = 1

    # Initialize the maximum count and the chosen value
    max_count = 0
    chosen_val = min_val

    # Iterate through the dictionary to find the maximum count and the chosen value
    for val, freq in count.items():
        # Update the maximum count and the chosen value if the current frequency is larger
        if freq > max_count:
            max_count = freq
            chosen_val = val
        # If the frequencies are the same, choose the smaller value
        elif freq == max_count and val < chosen_val:
            chosen_val = val

    # Count the number of i such that a_i = chosen_val
    res = sum(1 for num in a if num == chosen_val)

    return res


# Read the input from the standard input
def read_input():
    N = int(input())
    a = list(map(int, input().split()))
    return N, a


# Write the output to the standard output
def write_output(res):
    print(res)


# Main function
def main():
    # Read the input
    N, a = read_input()

    # Call the solve function
    res = solve(N, a)

    # Write the output
    write_output(res)


# Execute the main function
if __name__ == "__main__":
    main()
