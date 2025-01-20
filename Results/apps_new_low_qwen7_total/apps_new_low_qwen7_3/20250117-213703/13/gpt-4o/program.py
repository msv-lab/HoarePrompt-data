def max_beauty_after_swap(n, trophies):
    segments = []
    i = 0
    
    while i < n:
        if trophies[i] == 'G':
            start = i
            while i < n and trophies[i] == 'G':
                i += 1
            segments.append((start, i - 1))
        else:
            i += 1
    
    if not segments:
        return 0
    
    max_length = max(end - start + 1 for start, end in segments)
    
    if len(segments) == 1:
        return max_length
    
    for i in range(1, len(segments)):
        prev_start, prev_end = segments[i - 1]
        curr_start, curr_end = segments[i]
        if curr_start - prev_end == 2:
            max_length = max(max_length, (curr_end - curr_start + 1) + (prev_end - prev_start + 1) + 1)
    
    return min(max_length + 1, n)

# Read input
import sys
input = sys.stdin.read
data = input().split()
n = int(data[0])
trophies = data[1]

# Print output
print(max_beauty_after_swap(n, trophies))
