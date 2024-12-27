import random

class TreapNode:
  def __init__(self, key, value, parent=None):
    self.priority = random.randrange(1000000000)
    self.key = key
    self.value = value
    self.parent = parent
    self.left_child, self.right_child = None, None

class Treap:
  def __init__(self):
    self.root = None
  
  def add(self, key, value):
    if self.root == None:
      self.root = TreapNode(key, value)
      return
    node = self.root
    # Descend the BST and insert a new node.
    while True:
      if node.key == key:
        return
      elif node.key > key:
        if node.left_child:
          node = node.left_child
          continue
        child = node.left_child = TreapNode(key, value, node)
        break
      else:
        if node.right_child:
          node = node.right_child
          continue
        child = node.right_child = TreapNode(key, value, node)
        break
    # Perform tree rotations until node priorities are min-heap-ordered.
    while node.priority > child.priority:
      if child == node.left_child:
        if child.right_child:
          child.right_child.parent = node
        node.left_child, child.right_child = child.right_child, node
      else:
        if child.left_child:
          child.left_child.parent = node
        node.right_child, child.left_child = child.left_child, node
      grandparent = node.parent
      child.parent, node.parent = grandparent, child
      if grandparent == None:
        self.root = child
        break
      if node == grandparent.left_child:
        grandparent.left_child = child
      else:
        grandparent.right_child = child
      node = grandparent

  def traverse(self, node, keys):
    if node == None:
      return
    self.traverse(node.left_child, keys)
    keys.append(node.key)
    self.traverse(node.right_child, keys)

  def display(self):
    keys = []
    self.traverse(self.root, keys)
    print('traversal: ' + ' '.join(map(str, keys)))

  def find(self, key):
    node = self.root
    while node != None:
      if node.key < key:
        node = node.right_child
      elif node.key > key:
        node = node.left_child
      else:
        return node
    return None

  def find_around(self, key):  # Assume that key is not in the treap.
    smaller, bigger = None, None
    node = self.root
    while node != None:
      if node.key < key:
        if smaller == None or smaller.key < node.key:
          smaller = node
        node = node.right_child
      else:
        if bigger == None or bigger.key > node.key:
          bigger = node
        node = node.left_child
    return (smaller, bigger)

class BSTNode:
  def __init__(self, key):
    self.key = key
    self.left_child, self.right_child = None, None


n = int(raw_input())
data = list(map(int, raw_input().split()))
bst_root = BSTNode(data[0])
treap = Treap()
treap.add(data[0], bst_root)
result = []
sorted_keys = [ data[0] ]
for key in data[1:n]:
  smaller, bigger = treap.find_around(key)
  #print('smaller %s, key %d, bigger %s' % (smaller.key if smaller else '_',
  #    key, bigger.key if bigger else '_'))
  #print(sorted_keys)
  if bigger == None or bigger.value.left_child != None:
    result.append(smaller.key)
    bst_node = smaller.value.right_child = BSTNode(key)
  else:
    result.append(bigger.key)
    bst_node = bigger.value.left_child = BSTNode(key)
  treap.add(key, bst_node)
  #sorted_keys = sorted(sorted_keys + [ key ])
print(' '.join(map(str, result)))
#treap.display()
