class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = sorted(zip(position, speed), reverse=True)
        stack = []

        for pos, s in pair:
            time_current = (target - pos) / s
            if not stack or time_current > stack[-1]:
                stack.append(time_current)

        return len(stack)
