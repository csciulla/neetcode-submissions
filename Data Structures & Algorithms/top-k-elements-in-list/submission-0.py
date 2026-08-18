class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        types = {}
        for num in nums:
            if num not in types:
                types[num] = 1
            else:
                types[num] += 1

        values = list(types.values())
        freq = []
        while k:
            top = max(values)
            freq.append(top)
            values.remove(top)
            k -= 1

        res = []
        for num, f in list(types.items()):
            if f in freq:
                res.append(num)
        return res

        
            