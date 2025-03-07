def count_beautiful_pairs(test_cases):
    results = []
 
    for n, x, y, arr in test_cases:
        count = 0
        residue_map = {}
 
        for num in arr:
            # Calculate the required residues for the current number
            r_x = (-num) % x
            r_y = num % y
 
            # Count the pairs that satisfy both conditions
            count += residue_map.get((r_x, r_y), 0)
 
            # Update the residue map with the current number's residues
            current_key = (num % x, num % y)
            residue_map[current_key] = residue_map.get(current_key, 0) + 1
 
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