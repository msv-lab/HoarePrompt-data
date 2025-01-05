# Read input
T = input
for _ in [0] * int(T()):
    # Read n, k, m for each test case
    n, k, m = map(int, T().split())
    
    # Create a set of the first k lowercase alphabets
    a = t = {*map(chr, range(97, 97 + k))}
    
    # Initialize result as 'NO ' (we'll append the string if needed)
    r = 'NO '
    
    # Read the string s
    for x in T():
        # Remove the character from the set t if it exists
        t = t - {x} or a
        
        # Append the character to result if t is less than a
        r += x[t < a:]
    
    # Print 'YES' if all strings are subsequences, otherwise print 'NO' and the string
    print(('YES', t := (r + t.pop() * n)[:n + 3])[t > r])