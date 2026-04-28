class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        speedMap = {}

        for i in range(len(speed)):
            speedMap[position[i]] = speed[i]
        
        position = sorted(position)[::-1]

        fleets = []
        for p in position:
            t = (target - p) / speedMap[p]
            # print(fleets,t, p, speedMap[p])
            if not fleets or fleets[-1] < t:
                fleets.append(t)
        
        return len(fleets)