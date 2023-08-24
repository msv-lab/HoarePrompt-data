
n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()
b.sort()

# Tommy hides the lantern with the maximum brightness
a_hidden = a[:-1]

max_brightness = float('-inf')

for i in range(n-1):
    # Banban chooses the lantern with maximum brightness from Tommy and himself
    pair_brightness = a_hidden[i] * b[-1]
    # Update the maximum brightness
    max_brightness = max(max_brightness, pair_brightness)

print(max_brightness)
