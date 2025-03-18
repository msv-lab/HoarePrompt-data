for line in [*open(0)][2::2]:
    print(len((tokens := line.split())) - len({*tokens}))