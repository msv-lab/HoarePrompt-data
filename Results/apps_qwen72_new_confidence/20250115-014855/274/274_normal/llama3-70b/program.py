first_name, last_name = input().split()
login = ''
for i in range(1, len(first_name) + 1):
    for j in range(1, len(last_name) + 1):
        login = min(login, first_name[:i] + last_name[:j]) if login else first_name[:i] + last_name[:j]
print(login)
