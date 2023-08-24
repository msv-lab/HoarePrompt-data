n = int(input())
text = input().split()

max_volume = 0
for word in text:
    volume = sum(1 for letter in word if letter.isupper())
    max_volume = max(max_volume, volume)

print(max_volume)