class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        inf = float('inf')
        # Step 1: Initialize the distance matrix with inf
        dist = [[inf] * n for _ in range(n)]
        
        # Distance from a city to itself is 0
        for i in range(n):
            dist[i][i] = 0
        
        # Step 2: Fill the initial distances from the edges
        for u, v, w in edges:
            dist[u][v] = w
            dist[v][u] = w
        
        # Step 3: Apply Floyd-Warshall Algorithm to find shortest paths between all pairs of cities
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if dist[i][j] > dist[i][k] + dist[k][j]:
                        dist[i][j] = dist[i][k] + dist[k][j]
        
        # Step 4: Count reachable cities within distance threshold for each city
        min_count = inf
        result_city = -1
        
        for i in range(n):
            count = sum(1 for j in range(n) if dist[i][j] <= distanceThreshold)
            
            # Choose the city with the smallest count, and in case of ties, the city with the greatest index
            if count < min_count or (count == min_count and i > result_city):
                min_count = count
                result_city = i
        
        return result_city