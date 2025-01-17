n, a, b = map(int, input().split())
if (a + b - 1) & (a + b - 2):
    print("Final!")
else:
    print(((a ^ b).bit_length() - 1))
