n = int(input())
a = list(map(int, input().split()))

# Check if the whole sequence length is odd, starts with an odd number, and ends with an odd number
if n % 2 == 1 and a[0] % 2 == 1 and a[-1] % 2 == 1:
    print("Yes")
else:
    print("No")
