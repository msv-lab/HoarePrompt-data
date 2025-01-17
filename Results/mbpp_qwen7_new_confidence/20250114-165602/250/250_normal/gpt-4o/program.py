import math

def perfect_squares(start, end):
    result = []
    # Start with the smallest integer whose square is >= start
    current = math.ceil(math.sqrt(start))
    # Continue until the square of current exceeds end
    while current * current <= end:
        result.append(current * current)
        current += 1
    return result

# Test cases
assert perfect_squares(1, 30) == [1, 4, 9, 16, 25]
assert perfect_squares(50, 100) == [64, 81, 100]
assert perfect_squares(100, 200) == [100, 121, 144, 169, 196]
