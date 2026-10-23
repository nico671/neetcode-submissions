class TimeMap:

    def __init__(self):
        self.storage = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.storage:
            self.storage[key].append((value, timestamp))
        else:
            self.storage[key] = [(value, timestamp)]

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.storage:
            return ""
        else:
            res = ""
            l, r = 0, len(self.storage[key]) - 1
            while l <= r:
                m = (l+r) // 2
                if self.storage[key][m][1] <= timestamp:
                    res = self.storage[key][m][0]
                    l = m+1
                elif self.storage[key][m][1] > timestamp:
                    r = m - 1
        return res