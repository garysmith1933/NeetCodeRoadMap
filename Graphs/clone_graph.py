class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        oldToNew = {}

        def dfs(node):
            # if a copy already exists return it
            if node in oldToNew:
                return oldToNew[node]

           
            copyNode = Node(node.val)  # create copy
            oldToNew[node] = copyNode  # add node / copy to hashmap
            for neighbor in node.neighbors: # iterate over neighbors of current node
                copyNode.neighbors.append(dfs(neighbor)) # add neighbors of node to copy neighbors
            
            return copyNode
        
        return dfs(node) if node else None 
    
    # Time O(N) - # of edges Space O(N)