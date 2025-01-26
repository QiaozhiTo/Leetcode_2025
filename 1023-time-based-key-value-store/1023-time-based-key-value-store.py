class TimeMap(object):

    def __init__(self):
        self.store = {}
        

    def set(self, key, value, timestamp):
        """
        :type key: str
        :type value: str
        :type timestamp: int
        :rtype: None
        """
        if key not in self.store:
            self.store[key] = []
        self.store[key].append([value, timestamp])
        

    def get(self, key, timestamp):
        """
        :type key: str
        :type timestamp: int
        :rtype: str
        """
        value = self.store.get(key, [])
        res = ""
        l, r = 0, len(value)-1
        while l <= r:
            m = (l+r) // 2
            if value[m][1] <= timestamp:                    
                l = m + 1
                res = value[m][0]
            else:
                r = m - 1
        return res


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)