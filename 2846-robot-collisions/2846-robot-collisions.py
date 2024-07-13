class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        robots = sorted(zip(positions, healths, directions, range(len(positions))))
    
        stack = []  # Stack to keep track of right-moving robots
        survivors = [None] * len(positions)  # To keep final healths of survivors in original order
        
        for pos, health, direction, index in robots:
            if direction == 'R':
                stack.append((health, index))
            else:  # direction == 'L'
                while stack:
                    r_health, r_index = stack[-1]
                    if r_health < health:
                        stack.pop()
                        health -= 1
                    elif r_health > health:
                        stack[-1] = (r_health - 1, r_index)
                        health = 0
                        break
                    else:
                        stack.pop()
                        health = 0
                        break
                if health > 0:
                    survivors[index] = health
        
        for health, index in stack:
            survivors[index] = health
        
        # Filter out None values which represent robots that were removed
        return [health for health in survivors if health is not None]
