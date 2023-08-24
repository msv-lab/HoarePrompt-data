def count_ways_to_cry(n, heights):
    count = 0
    max_height = max(heights)   # height of the tallest mountain
    max_height_indexes = [i for i, h in enumerate(heights) if h >= max_height]   # indexes of the tallest mountains
    
    for i in range(n-1):
        for j in range(i+1, n):
            h1 = heights[i]
            h2 = heights[j]
            if h1 | h2 > max_height and i < j:   # if bitwise OR of heights is larger than the tallest mountain
                count += 1
    
    return count

n = int(input())
heights = list(map(int, input().split()))

result = count_ways_to_cry(n, heights)
print(result)