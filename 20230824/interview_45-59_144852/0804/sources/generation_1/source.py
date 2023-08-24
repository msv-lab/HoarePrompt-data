s = input()
k = int(input())

if len(s) < k:
    print("impossible")
else:
    existing_letters = set(s)
    num_changes = k - len(existing_letters)
    print(max(0, num_changes))