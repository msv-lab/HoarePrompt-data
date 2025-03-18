def recoverString(n, a):
    s = ""
    char_count = [0] * 26  # Initialize a count for each lowercase letter
    for i in range(n):
        # Find the (a[i] + 1)-th unique character and append it to the string
        for j in range(26):
            if char_count[j] == a[i]:
                s += chr(j + ord('a'))
                char_count[j] += 1
                break
    return s
 
# Read the input and solve the test cases
t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    print(recoverString(n, a))