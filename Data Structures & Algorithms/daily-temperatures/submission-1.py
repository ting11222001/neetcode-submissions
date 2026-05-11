class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # Input: temperatures = [30,38,30,36,35,40,28]
        # Output: [1,4,1,2,1,0,0]
        # stack is going to be monotonic decreasing e.g. 73, 72, 71, 71, etc.

        stack = []   # saves the previous temperatures, and each element is a pair as this: [temperature, index]
        output = [0] * len(temperatures)

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                stackTemp, stackIndx = stack.pop()   # unpacks the list
                output[stackIndx] = i - stackIndx
            stack.append([t, i])
        
        return output

# output:           [1, 0, 0, 0, 0, 0, 0]       -> [1, 0, 1, 0, 0, 0, 0]                         -> [1, 0, 1, 0, 1, 0, 0] -> [1, 0, 1, 2, 1, 0, 0] -> [1, 4, 1, 2, 1, 0, 0] 
# stack: [30, 0] -> [38, 1] -> [38, 1], [30, 2] -> [38, 1], [36, 3] -> [38, 1], [36, 3], [35, 4] -> [38, 1], [36, 3]      -> [38, 1]               -> empty                 -> [40, 5] -> [40, 5], [28, 6]