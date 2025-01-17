# Define the full set of gems with their corresponding colors
gems = {
    'purple': 'Power',
    'green': 'Time',
    'blue': 'Space',
    'orange': 'Soul',
    'red': 'Reality',
    'yellow': 'Mind'
}

# Read the input
n = int(input())
present_colors = {input().strip() for _ in range(n)}

# Determine the absent gems
absent_gems = [gem for color, gem in gems.items() if color not in present_colors]

# Output the result
print(len(absent_gems))
for gem in absent_gems:
    print(gem)
