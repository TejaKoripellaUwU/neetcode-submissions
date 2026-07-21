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
        def dfs(curNode):
            if curNode in visited:
                return visited[curNode]
            if not curNode:
                return None
            
            newNode = Node(curNode.val)
            visited[curNode] = newNode
            for node in curNode.neighbors:
                newNode.neighbors.append(dfs(node))
            
            return newNode
        
        return dfs(node)