def min_colors(N, A):
    colors = []
    for num in A:
        # Find the minimum color that is still greater than the current number
        min_color = float('inf')
        i = -1
        for idx, color in enumerate(colors):
            if color > num:
                if color < min_color:
                    min_color = color
                    i = idx
        # If no color is greater than the current number, add a new color
        if min_color == float('inf'):
            colors.append(num)
        # If a color is greater than the current number, replace it with the current number
        else:
            colors[i] = num
    return len(colors)
    
N = int(input())
A = []
for _ in range(N):
    A.append(int(input()))

result = min_colors(N, A)
print(result)