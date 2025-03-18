def count_beautiful_pairs(test_cases):
    results = []
 
    for n, x, y, arr in test_cases:
        count = 0
        mod_x_map = {}
        mod_y_map = {}
 
        for num in arr:
            # Calculate residues for current number
            mod_x = (-num) % x
            mod_y = num % y
 
            # Count pairs where conditions are satisfied
            count += mod_x_map.get(mod_x, 0) + mod_y_map.get(mod_y, 0)
 
            # Update hash maps with current number's residues
            mod_x_key = num % x
            mod_y_key = num % y
 
            mod_x_map[mod_x_key] = mod_x_map.get(mod_x_key, 0) + 1
            mod_y_map[mod_y_key] = mod_y_map.get(mod_y_key, 0) + 1
 
        results.append(count)
 
    return results
 
 
# Input Reading
import sys
input = sys.stdin.read
data = input().split()
 
# Parse input
t = int(data[0])
index = 1
test_cases = []
 
for _ in range(t):
    n, x, y = map(int, data[index:index+3])
    index += 3
    arr = list(map(int, data[index:index+n]))
    index += n
    test_cases.append((n, x, y, arr))
 
# Solve and output results
results = count_beautiful_pairs(test_cases)
print("\n".join(map(str, results)))