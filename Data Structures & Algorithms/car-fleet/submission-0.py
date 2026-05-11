class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # time to reach target = (target position - curr position) / curr speed
        # keep the slow car and see it as a fleet
        # start from the right i.e. start from the car that's closest to the target

        # Input: target = 10, position = [1,4], speed = [3,2] Output: 1 
        # Input: target = 10, position = [4,1,0,7], speed = [2,2,1,1] Output: 3

        stack = []      # note each car's time
        pairs = list(zip(position, speed))
        sorted_pairs = sorted(pairs, reverse=True)

        for position, speed in sorted_pairs:                # [(7, 1), (4, 2), (1, 2), (0, 1)]
            stack.append((target - position) / speed)       # 3 / 1 = 3, 6 / 2 = 3, so stack: 3, 3 -> 3, 4.5, 10
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()                                 # stack: 3

        return len(stack)


        