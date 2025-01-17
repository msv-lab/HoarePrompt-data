# Read the input
n = int(input())
a = list(map(int, input().split()))

# Initialize counters for each muscle group
chest = 0
biceps = 0
back = 0

# Iterate over the exercises
for i in range(n):
    if i % 3 == 0:
        chest += a[i]
    elif i % 3 == 1:
        biceps += a[i]
    elif i % 3 == 2:
        back += a[i]

# Determine which muscle group gets the most exercise
if chest > biceps and chest > back:
    print("chest")
elif biceps > chest and biceps > back:
    print("biceps")
else:
    print("back")
