from collections import deque, defaultdict

class Solution:
    def secondMinimum(self, n: int, edges: List[List[int]], time: int, change: int) -> int:
        # Build the adjacency list
        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        # BFS setup
        q = deque([(1, 1)])  # (current_node, frequency)
        dist1 = [-1] * (n + 1)  # Distance of the first minimum
        dist2 = [-1] * (n + 1)  # Distance of the second minimum
        dist1[1] = 0

        while q:
            node, freq = q.popleft()
            time_taken = dist1[node] if freq == 1 else dist2[node]

            # If the timeTaken falls under the red bracket, wait till the path turns green.
            if (time_taken // change) % 2:
                time_taken = change * (time_taken // change + 1) + time
            else:
                time_taken += time

            for neighbor in adj[node]:
                if dist1[neighbor] == -1:
                    dist1[neighbor] = time_taken
                    q.append((neighbor, 1))
                elif dist2[neighbor] == -1 and dist1[neighbor] != time_taken:
                    if neighbor == n:
                        return time_taken
                    dist2[neighbor] = time_taken
                    q.append((neighbor, 2))

        return 0