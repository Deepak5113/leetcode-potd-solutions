class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        def topological_sort(conditions: List[Tuple[int, int]]) -> List[int]:
            graph = defaultdict(list)
            in_degree = {i: 0 for i in range(1, k + 1)}
            
            for u, v in conditions:
                graph[u].append(v)
                in_degree[v] += 1
            
            queue = deque([node for node in in_degree if in_degree[node] == 0])
            topo_order = []
            
            while queue:
                node = queue.popleft()
                topo_order.append(node)
                for neighbor in graph[node]:
                    in_degree[neighbor] -= 1
                    if in_degree[neighbor] == 0:
                        queue.append(neighbor)
            
            if len(topo_order) == k:
                return topo_order
            else:
                return []
        
        row_order = topological_sort(rowConditions)
        col_order = topological_sort(colConditions)
        
        if not row_order or not col_order:
            return []
        
        pos_in_row = {num: i for i, num in enumerate(row_order)}
        pos_in_col = {num: i for i, num in enumerate(col_order)}
        
        matrix = [[0] * k for _ in range(k)]
        for num in range(1, k + 1):
            matrix[pos_in_row[num]][pos_in_col[num]] = num
        
        return matrix