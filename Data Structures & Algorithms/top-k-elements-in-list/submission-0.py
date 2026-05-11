class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # nums=[1,3,3,3,3,2,2]
        # k=2
        counts = {}

        for num in nums:
            counts[num] = counts.get(num, 0) + 1

        arr = []
        for num, count  in counts.items():
            arr.append([count, num])
        arr.sort()  # [[1, 1], [2, 2], [4, 3]]

        result = []

        while len(result) < k:
            result.append(arr.pop()[1]) # pop the index 1 element in the inner list

        return result
        

        