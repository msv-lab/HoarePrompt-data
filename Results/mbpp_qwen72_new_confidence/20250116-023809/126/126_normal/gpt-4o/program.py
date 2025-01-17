def lateralsurface_cube(side_length):
    return 4 * side_length ** 2

# Testing the function with provided test cases
assert lateralsurface_cube(5) == 100
assert lateralsurface_cube(9) == 324
assert lateralsurface_cube(10) == 400
