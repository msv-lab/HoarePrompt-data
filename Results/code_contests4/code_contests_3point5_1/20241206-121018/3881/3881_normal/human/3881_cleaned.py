def func_1():
    index = defaultdict(list)
    for line in stdin:
        (word, page) = line.split()
        index[word].append(int(page))
    for word in sorted(index):
        print(word)
        print(*sorted(index[word]))
    exit()
if __name__ == '__main__':
    func_1()