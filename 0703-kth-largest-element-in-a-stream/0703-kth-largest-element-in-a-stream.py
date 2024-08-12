class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.min_heap = []
        
        # Build the initial heap with up to k elements
        for num in nums:
            self.add(num)

    def add(self, val: int) -> int:
        # If the heap has fewer than k elements, add the new value
        if len(self.min_heap) < self.k:
            heapq.heappush(self.min_heap, val)
        # If the new value is greater than the smallest in the heap, replace the smallest
        elif val > self.min_heap[0]:
            heapq.heapreplace(self.min_heap, val)
        
        # The root of the heap is the k-th largest element
        return self.min_heap[0]



# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)