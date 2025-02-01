class TimeMap:
    def __init__(self):
        self.store = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ""

        arr = self.store[key]
        left, right = 0, len(arr) - 1
        best_idx = -1 

        while left <= right:
            mid = (left + right) // 2
            if arr[mid][0] <= timestamp:
                best_idx = mid 
                left = mid + 1 
            else:
                right = mid - 1  
        
        return arr[best_idx][1] if best_idx != -1 else ""
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)