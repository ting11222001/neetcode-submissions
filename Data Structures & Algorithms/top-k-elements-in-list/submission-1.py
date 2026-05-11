class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # nums=[1,2,2,3,3,3]
        # k=2
        # frequency: [[], [], ..., []] where i (count) -> values
        # max count is the length of nums i.e. 6, range(7), which will be 0, 1, ..., 6

        counts = {}

        for num in nums:
            counts[num] = counts.get(num, 0) + 1 # num -> count {1: 1, 2: 2, 3: 3}
        
        size = len(nums)
        frequency = [[] for _ in range(size + 1)]

        for num, count in counts.items():
            frequency[count].append(num)  # frequency: [[], [1], [2], [3], [], [], []]
        
        print(frequency)

        result = []
        for i in range(len(frequency) - 1, 0, -1):
            for num in frequency[i]:
                result.append(num)
                if len(result) == k:
                    return result
                




        

        