class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map = {}

        for n in nums:
            map[n] = 1 + map.get(n, 0)
        
        output = []
        for j in range(k):
            mfreq = max(map, key=map.get)
            output.append(mfreq)
            map.pop(mfreq)

        return output
