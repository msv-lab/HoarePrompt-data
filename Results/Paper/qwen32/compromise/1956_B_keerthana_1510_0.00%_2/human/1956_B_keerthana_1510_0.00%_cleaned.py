for line in [*open(0)][2::2]:
    elements = line.split()
    print(sum((elements.count(item) // 3 for item in {*elements})))