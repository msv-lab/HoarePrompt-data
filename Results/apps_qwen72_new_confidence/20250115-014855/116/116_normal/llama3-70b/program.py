r, s, p = map(int, input().split())
total = r + s + p

# Calculate the probability of each species to be the only one surviving
rock_prob = 0
scissor_prob = 0
paper_prob = 0

if r > s and r > p:
    rock_prob = 1
elif s > r and s > p:
    scissor_prob = 1
elif p > r and p > s:
    paper_prob = 1
else:
    # Calculate the probability when no species has a clear advantage
    rock_prob = (r * (r - 1) + r * s + r * p) / (total * (total - 1))
    scissor_prob = (s * (s - 1) + s * p + s * r) / (total * (total - 1))
    paper_prob = (p * (p - 1) + p * r + p * s) / (total * (total - 1))

print("{:.9f} {:.9f} {:.9f}".format(rock_prob, scissor_prob, paper_prob))
