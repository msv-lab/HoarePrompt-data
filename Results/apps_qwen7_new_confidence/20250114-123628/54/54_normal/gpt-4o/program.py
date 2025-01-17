# Read input
n = int(input())
s = input().strip()
beauty = list(map(int, input().strip().split()))

# Sort the string and beauty values
s_sorted = sorted(s)
beauty_sorted = sorted(beauty, reverse=True)

# Calculate maximum possible beauty
max_beauty = 0
for i in range(n):
    max_beauty += beauty_sorted[i]

print(max_beauty)
