 
class TrieNode:
    def __init__(self):
        self.childs = dict()
        self.isWord = False
        #self.firstwin = False
        #self.firstlose = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for letter in word:
            child = node.childs.get(letter)

            if child is None:
                child = TrieNode()
                node.childs[letter] = child
            else:
                if child.isWord == True:
                    child.isWord = False
            node = child
        node.isWord = True



    def searh(self, word):
        node = self.root
        for letter in word:
            node = node.childs.get(letter)
            if node is None:
                return False
        return node.isWord

    def startsWith(self, prefix):
        node = self.root
        for letter in prefix:
            node = node.childs.get(letter)
            if node is None:
                return False
        return True

def DFS(node, level):
    if node is not None and node.isWord:
        if level % 2 == 1:
            return True, False
        else:
            return False, True
    nodes = node.childs
    odd_ret = False
    even_ret = False
    for it in nodes:
        #print(it)
        child = nodes.get(it)
        odd_w, even_w = DFS(child, level+1)
        if odd_w == True:
            odd_ret = True
        if even_w == True:
            even_ret = True
    return odd_ret, even_ret
    
def firstWinOrLose(ttree):
    canloss = False
    canwin = False
    node = ttree.root.childs
    for it in node: 
        #print(it)
        child = node.get(it)
        odd_w, even_w = DFS(child, 0)
        #print(odd_w, even_w)
        if odd_w == True:
            odd_w = True
        if even_w == True:
            even_w = True

        if even_w:
            canwin = True
        if odd_w:
            canloss = True

    if canloss and canwin:
        return 3
    if canloss:
        return 1
    return 2

n, k = [int(s) for s in raw_input().split(" ")]
tree =Trie() 
for i in xrange(0,n):
    #print(i)
    tree.insert(raw_input())

ret_type = firstWinOrLose(tree)
#print(ret_type)
if ret_type == 1: 
    print('Second')

if ret_type == 2:
    if k%2 == 1:
        print('First')
    else:
        print('Second')

if ret_type == 3:
    print('First')


#tree.printDFS()
#tree.dfs( tree.root, 'origin' ) 
#tree.sol(k) 


