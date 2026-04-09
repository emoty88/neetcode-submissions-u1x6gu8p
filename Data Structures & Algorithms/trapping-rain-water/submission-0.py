from collections import defaultdict
class Solution:
    def trap(self, height: List[int]) -> int:
        
        wall = 0
        walls = defaultdict(lambda: [0,0])

        for i in range(len(height)):
            walls[i][0] = wall
            wall = max(wall, height[i])

        
        wall = 0
        for i in range(len(height)-1, -1, -1):
            walls[i][1] = wall
            wall = max(wall, height[i])

        
        res = 0
        for i in range(len(height)):
            h = min(walls[i])
            if height[i] < h:
                res+= h-height[i]
        
        return res