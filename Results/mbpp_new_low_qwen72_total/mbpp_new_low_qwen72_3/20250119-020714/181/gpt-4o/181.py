def find_Average_Of_Cube(n):
    # Generate the first n natural numbers
    natural_numbers = range(1, n + 1)
    # Compute the cubes of these numbers
    cubes = [x ** 3 for x in natural_numbers]
    # Calculate the sum of the cubes
    sum_of_cubes = sum(cubes)
    # Calculate the average
    average = sum_of_cubes / n
    return average

# Test cases to validate the solution
assert find_Average_Of_Cube(2) == 4.5
assert find_Average_Of_Cube(3) == 12
assert find_Average_Of_Cube(1) == 1
