class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        track = []
        for n in nums:
            if n in track:
                return True
            else:
                track.append(n)
        return False