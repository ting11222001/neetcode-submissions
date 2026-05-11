class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # Input: temperatures = [30,38,30,36,35,40,28]
        # Output: [1,4,1,2,1,0,0]
        # stack is going to be monotonic decreasing e.g. 73, 72, 71, 71, etc.

        stack = []   # saves the smaller temperature, and each element is a pair as this: [temperature, index]
        output = [0] * len(temperatures)

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                stackTemp, stackIndx = stack.pop()   # unpacks the list
                output[stackIndx] = i - stackIndx
            stack.append([t, i])
        
        return output
