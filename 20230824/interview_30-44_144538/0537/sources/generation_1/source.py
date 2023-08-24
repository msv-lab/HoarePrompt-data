n, k = map(int, input().split())

# Calculate the maximum number of winners
max_winners = min(n // 2, n // (2 * k))

# Calculate the number of students with diplomas
diplomas = max_winners

# Calculate the number of students with certificates
certificates = k * max_winners

# Calculate the number of students who are not winners
non_winners = n - diplomas - certificates

print(diplomas, certificates, non_winners)