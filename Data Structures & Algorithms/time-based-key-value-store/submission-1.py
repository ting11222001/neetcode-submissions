class TimeMap:

    def __init__(self):
        self.store = {}
        # key: list of [value, timestamp]
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        # use a hashmap
        if key not in self.store:
            self.store[key] = []
        self.store[key].append([value, timestamp])

        
    def get(self, key: str, timestamp: int) -> str:
        res = ""
        values = self.store.get(key, [])

        # do binary search in the list of [value, timestamp]
        # because the timestamps will be in the asc order
        l, r = 0, len(values) - 1

        while l <= r:
            m = (l + r) // 2

            # always retrieves the most recent timestamp ≤ the requested timestamp
            if values[m][1] <= timestamp:
                res = values[m][0]  # update the res 
                l = m + 1           # continue to search to the closest
            else:
                r = m - 1           # invalid cases, so ignore
        
        return res
        
