"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

        if not node:
            return None
        m = {node:Node(val = node.val)}
        q = [node]
        v = set()
        while len(q):
            ele = q.pop()
            v.add(ele)
            for n in ele.neighbors:
                if n not in v:
                    if n not in m.keys():
                        copy = Node(val = n.val, neighbors = [])
                        m[n] = copy
                        q.append(n)

                    m[n].neighbors.append(m[ele])
                    m[ele].neighbors.append(m[n])
        print(m)
        return m[node]
