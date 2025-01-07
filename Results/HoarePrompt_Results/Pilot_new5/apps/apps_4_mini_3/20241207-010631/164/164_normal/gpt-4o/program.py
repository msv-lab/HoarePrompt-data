# Read input values
n, k = map(int, input().split())
line = input()

# Find positions of 'G' and 'T'
G_pos = line.index('G')
T_pos = line.index('T')

# Ensure G_pos is less than T_pos for consistency
if G_pos > T_pos:
    G_pos, T_pos = T_pos, G_pos

# Check every k-th position from G_pos to T_pos
reachable = False
for pos in range(G_pos, T_pos + 1, k):
    if line[pos] == '#':
        break
    if pos == T_pos:
        reachable = True
        break

# Output the result
if reachable:
    print("YES")
else:
    print("NO")
