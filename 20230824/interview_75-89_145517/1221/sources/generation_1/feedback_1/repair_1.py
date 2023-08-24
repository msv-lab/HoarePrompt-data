n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort(reverse=True)
b.sort(reverse=True)

# Tommy hides the lantern with the maximum brightness
a_hidden = a[1:]

max_brightness = max(a[0] * b[0], a_hidden[0] * b[0])

print(max_brightness)