import sys
 
def read_input():
    t = int(sys.stdin.readline().strip())
    cases = []
    for _ in range(t):
        n = int(sys.stdin.readline().strip())
        s = sys.stdin.readline().strip()
        cases.append((n, s))
    return cases
 
def find_winner(case):
    # Count the number of 'U's initially facing up
    ups = sum(1 for c in case[1] if c == 'U')
    
    # If there are an odd number of 'U's, Alice wins; otherwise, Bob wins
    return "YES" if ups % 2 else "NO"
 
# Read input
cases = read_input()
 
# Process each case and output results
for case in cases:
    print(find_winner(case))