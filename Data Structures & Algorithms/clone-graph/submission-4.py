"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        visited = dict()
        def dfs(curNode,dcNode):
            for nxt in curNode.neighbors:
                if nxt.val not in visited:
                    newN = Node(nxt.val)
                    dcNode.neighbors.append(newN)
                    visited[nxt.val] = newN
                    dfs(nxt,newN)
                else:
                    dcNode.neighbors.append(visited[nxt.val])

            return dcNode
        if not node:
            return None
        startingNode = Node(node.val)
        visited[node.val] = startingNode
        return dfs(node,startingNode)