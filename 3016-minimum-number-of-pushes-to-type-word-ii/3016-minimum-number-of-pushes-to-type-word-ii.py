class Solution:
    def minimumPushes(self, word: str) -> int:
        # Step 1: Count the frequency of each character
        freq = Counter(word)
        
        # Step 2: Get the frequencies in a list and sort in descending order
        frequencies = sorted(freq.values(), reverse=True)
        
        # Step 3: Priority queue to manage key assignments
        # Each key can take up to 9 presses (1 through 9 times)
        key_presses = [0] * 8  # Since we have keys 2 through 9 (8 keys)
        
        # Min-heap to keep track of the current minimum press for each key
        heap = []
        for i in range(8):  # Keys from 2 to 9 (index 0 to 7 in the heap)
            heapq.heappush(heap, (0, i))  # (total presses for this key, key index)
        
        # Step 4: Assign frequencies to keys
        total_presses = 0
        for frequency in frequencies:
            # Get the key with the current minimum total presses
            presses, key = heapq.heappop(heap)
            presses += 1
            total_presses += presses * frequency
            # Increment the press count for this key and push back to heap
            heapq.heappush(heap, (presses, key))
        
        return total_presses