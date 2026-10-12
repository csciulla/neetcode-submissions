class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        output = []

        for n in nums:
            d[n] = 1 + d.get(n, 0)

        for _ in range(k):
            most_freq = max(d, key=d.get)
            output.append(most_freq)
            d.pop(most_freq, None)

        return output