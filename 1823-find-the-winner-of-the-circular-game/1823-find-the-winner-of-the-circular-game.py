class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        friends_list = list(range(1, n + 1))
        index = 0
        
        while len(friends_list) > 1:
            # Calculate the next index to pop
            index = (index + k - 1) % len(friends_list)
            friends_list.pop(index)
        
        return friends_list[0]
