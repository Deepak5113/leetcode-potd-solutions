class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n + 1))
        self.size = [1] * (n + 1)
        self.components = n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def unite(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX == rootY:
            return False
        if self.size[rootX] < self.size[rootY]:
            rootX, rootY = rootY, rootX
        self.parent[rootY] = rootX
        self.size[rootX] += self.size[rootY]
        self.components -= 1
        return True

    def is_connected(self):
        return self.components == 1

class Solution:
    def maxNumEdgesToRemove(self, n, edges):
        alice = UnionFind(n)
        bob = UnionFind(n)
        edges_required = 0

        # Process type 3 edges first
        for edge in edges:
            if edge[0] == 3:
                if alice.unite(edge[1], edge[2]) | bob.unite(edge[1], edge[2]):
                    edges_required += 1

        # Process type 1 and type 2 edges
        for edge in edges:
            if edge[0] == 1:
                if alice.unite(edge[1], edge[2]):
                    edges_required += 1
            elif edge[0] == 2:
                if bob.unite(edge[1], edge[2]):
                    edges_required += 1

        # Check if both are fully connected
        if alice.is_connected() and bob.is_connected():
            return len(edges) - edges_required

        return -1
