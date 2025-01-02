# from typing import List, Set, Dict, Tuple, Text, Optional
from collections import deque
from types import GeneratorType
import os
import sys
from atexit import register
import math
from io import BytesIO
import __pypy__  # type: ignore

#########
# INPUT #
#########


class Input(object):
  def __init__(self):
    if 'CPH' not in os.environ:
      sys.stdin = BytesIO(os.read(0, os.fstat(0).st_size))
      sys.stdout = BytesIO()
      register(lambda: os.write(1, sys.stdout.getvalue()))

  def rawInput(self):
    # type: () -> str
    return sys.stdin.readline().rstrip('\r\n')

  def readInt(self):
    return int(self.rawInput())

##########
# OUTPUT #
##########


class Output(object):
  def __init__(self):
    self.out = __pypy__.builders.StringBuilder()

  def write(self, text):
    # type: (str) -> None
    self.out.append(str(text))

  def writeLine(self, text):
    # type: (str) -> None
    self.write(str(text) + '\n')

  def finalize(self):
    if sys.version_info[0] < 3:
      os.write(1, self.out.build())
    else:
      os.write(1, self.out.build().encode())

###########
# LIBRARY #
###########


def bootstrap(f, stack=[]):
  # Deep Recursion helper.
  # From: https://github.com/cheran-senthil/PyRival/blob/c1972da95d102d95b9fea7c5c8e0474d61a54378/docs/bootstrap.rst
  # Usage:

  # @bootstrap
  # def recur(n):
  #   if n == 0:
  #     yield 1
  #   yield (yield recur(n-1)) * n
  def wrappedfunc(*args, **kwargs):
    if stack:
      return f(*args, **kwargs)
    else:
      to = f(*args, **kwargs)
      while True:
        if type(to) is GeneratorType:
          stack.append(to)
          to = next(to)
        else:
          stack.pop()
          if not stack:
            break
          to = stack[-1].send(to)
      return to

  return wrappedfunc


class Vector(object):
  # Faster implementation of dynamic array
  def __init__(self, init_size=0, initial_value=0):
    # type: (int, Any) -> None
    power_of_two = 1 << (init_size).bit_length()
    self.arr = [initial_value] * power_of_two
    self.n = init_size
    self.init = initial_value

  def __len__(self):
    return self.n

  def __getitem__(self, index):
    assert 0 <= index < self.n
    return self.arr[index]

  def __setitem__(self, index, value):
    assert 0 <= index < self.n
    self.arr[index] = value

  def append(self, value):
    if self.n == len(self.arr):
      new_arr = [self.init] * (self.n * 2)
      for i in range(self.n):
        new_arr[i] = self.arr[i]
      self.arr = new_arr

    self.arr[self.n] = value
    self.n += 1

    return value


class Dinic(object):
  '''
  >>> x = Dinic(5)
  >>> x.add_edge(3, 0, 5)
  >>> x.add_edge(3, 2, 3)
  >>> x.add_edge(2, 0, 5)
  >>> x.add_edge(3, 1, 7)
  >>> x.add_edge(1, 0, 1)
  >>> x.add_edge(1, 2, 3)
  >>> x.add_edge(2, 1, 3)
  >>> x.add_edge(0, 3, 10)
  >>> x.max_flow(3, 0)
  11
  >>> len(x.get_positive_flow_edges())
  6
  >>> y = Dinic(2)
  >>> y.max_flow(0, 1)
  0
  >>> y.get_positive_flow_edges()
  []
  >>> z = Dinic(3)
  >>> z.add_edge(1, 0, 3)
  >>> z.add_edge(1, 0, 5)
  >>> z.add_edge(0, 2, 6)
  >>> z.max_flow(1, 2)
  6
  >>> len(z.get_positive_flow_edges())
  3
  '''
  class Edge(object):
    def __init__(self, u, v, capacity):
      self.u = u
      self.v = v
      self.capacity = capacity
      self.flow = 0

      # Opposite edge in the residual graph
      self.opposite = None  # type: Dinic.Edge

    def get_remaining_capacity(self):
      return self.capacity - self.flow

    def __repr__(self):
      return '%d %d: %d/%d' % (self.u, self.v, self.flow, self.capacity)

  def __init__(self, n):
    # Adjacency list
    self.n = n
    self.adj_list = [[] for _ in range(n)]  # type: List[List[Dinic.Edge]]

    # For computations
    self.distance_label = [-1] * self.n
    self.adj_list_current = [0] * self.n
    self.is_flow_computed = False

  def add_edge(self, u, v, capacity):
    # type: (int, int, int) -> None
    assert 0 <= u < self.n
    assert 0 <= v < self.n
    assert capacity >= 0

    edge_forwards = Dinic.Edge(u, v, capacity)
    edge_backwards = Dinic.Edge(v, u, capacity=0)

    edge_forwards.opposite = edge_backwards
    edge_backwards.opposite = edge_forwards

    self.adj_list[u].append(edge_forwards)
    self.adj_list[v].append(edge_backwards)

  def _compute_distance_labels(self, source):
    # type: (int) -> None
    self.distance_label = [-1] * self.n
    self.distance_label[source] = 0
    queue = deque([source])
    while queue:
      node = queue.popleft()
      for edge in self.adj_list[node]:
        if self.distance_label[edge.v] == -1 and edge.get_remaining_capacity() > 0:
          self.distance_label[edge.v] = self.distance_label[node] + 1
          queue.append(edge.v)

  @bootstrap
  def blocking_flow_dfs(self, node, sink, flow_pushed):
    # type: (int, int, int) -> int
    if flow_pushed == 0:
      yield 0

    if node == sink:
      yield flow_pushed

    while self.adj_list_current[node] < len(self.adj_list[node]):
      edge = self.adj_list[node][self.adj_list_current[node]]

      if self.distance_label[edge.v] == self.distance_label[node]+1:
        recursed = (yield self.blocking_flow_dfs(
            edge.v,
            sink,
            min(flow_pushed, edge.get_remaining_capacity())
        ))
        if recursed:
          edge.flow += recursed
          edge.opposite.flow -= recursed
          yield recursed

      self.adj_list_current[node] += 1

    yield 0

  def max_flow(self, source, sink):
    # type: (int, int) -> Union[int, float]
    # Computes max flow, return it.

    assert 0 <= source < self.n
    assert 0 <= sink < self.n
    assert source != sink
    assert not self.is_flow_computed

    result = 0

    # Compute flow_infinity
    flow_infinity = 0  # type: int
    for node in range(self.n):
      for edge in self.adj_list[node]:
        flow_infinity += edge.capacity

    while True:
      # Compute distance labels
      self._compute_distance_labels(source)

      if self.distance_label[sink] == -1:
        # Sink no longer reachable, so done
        break

      # Compute blocking flow, using dfs
      self.adj_list_current = [0] * self.n
      while True:
        flow = self.blocking_flow_dfs(source, sink, flow_infinity)
        result += flow
        if not flow:
          break

    self.is_flow_computed = True

    return result

  def get_positive_flow_edges(self):
    # type: () -> List[Dinic.Edge]
    # Must be called after max_flow
    # Return all used edges
    assert self.is_flow_computed

    edges = []  # type: List[Dinic.Edge]
    for node in range(self.n):
      for edge in self.adj_list[node]:
        if edge.flow > 0:
          edges.append(edge)

    return edges


class TwoDArray(object):
  # Faster implementation of 2d array, using a single array math.
  '''
  >>> x = TwoDArray((2, 3), 5)
  >>> x.get([1, 2])
  5
  >>> x.get([0, 1])
  5
  >>> x.set([0, 1], 3)
  3
  >>> x.get([0, 1])
  3
  >>> x.get([1, 1])
  5
  >>> x.get([0, 0])
  5
  >>> x.set([1, 1], 2)
  2
  >>> x.get([1, 1])
  2
  '''

  def __init__(self, dimensions, initial_value=0):
    # type: (Tuple[int, int], Any) -> None
    self.dimensions = dimensions
    self.arr = [initial_value] * self.dimensions[0] * self.dimensions[1]

  def get(self, indexes):
    # type: (Iterable[int]) -> Any
    return self.arr[indexes[0] * self.dimensions[1] + indexes[1]]

  def set(self, indexes, value):
    # type: (Iterable[int], Any) -> Any
    self.arr[indexes[0] * self.dimensions[1] + indexes[1]] = value
    return value


#########
# LOGIC #
#########


def main(inp, out):
  # type: (Input, Output) -> any
  n, m = map(int, inp.rawInput().split())

  nodes = 2 * n + 2
  source = 2 * n
  sink = 2 * n + 1

  dinic = Dinic(nodes)

  inits = map(int, inp.rawInput().split())

  for i in range(n):
    dinic.add_edge(source, i, inits[i])

  targets = map(int, inp.rawInput().split())

  for i in range(n):
    dinic.add_edge(n+i, sink, targets[i])

  infin = sum(inits)

  for _ in range(m):
    u, v = map(int, inp.rawInput().split())
    u -= 1
    v -= 1
    dinic.add_edge(u, n+v, infin)
    dinic.add_edge(v, n+u, infin)

  for u in range(n):
    dinic.add_edge(u, n+u, infin)

  flow = dinic.max_flow(source, sink)
  if flow != sum(targets):
    out.writeLine('NO')
  else:
    out.writeLine('YES')

    travel = TwoDArray([n, n], 0)
    for edge in dinic.get_positive_flow_edges():
      if edge.u != source and edge.v != sink:
        travel.set((edge.u, edge.v-n),
                   travel.get((edge.u, edge.v-n)) + edge.flow)

    for i in range(n):
      flows = [travel.get((i, j)) for j in range(n)]
      out.writeLine(' '.join(map(str, flows)))


###############
# BOILERPLATE #
###############

output_obj = Output()
main(Input(), output_obj)
output_obj.finalize()
