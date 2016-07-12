class ZigzagIterator(object):

    def __init__(self, v1, v2):
        """
        Initialize your data structure here.
        :type v1: List[int]
        :type v2: List[int]
        """
        self.v1 = v1
        self.v2 = v2
        self.v2_len = len(self.v2)
        self.v1_len = len(self.v1)
        self.index_v1 = 0
        self.index_v2 = 0
        self.next_list = self.v1
        
        

    def next(self):
        """
        :rtype: int
        """
        if self.next_list is self.v1 and self.v1:
            value = self.v1[self.index_v1]
            self.index_v1 += 1
            self.next_list = self.v2
            if self.index_v2 >= self.v2_len:
                self.next_list = self.v1
            return value
        else:
            value = self.v2[self.index_v2]
            self.index_v2 += 1
            self.next_list = self.v1
            if self.index_v1 >= self.v1_len:
                self.next_list = self.v2
            return value
            

    def hasNext(self):
        """
        :rtype: bool
        """
        if self.index_v1 < self.v1_len or self.index_v2 < self.v2_len:
            return True
        else:
            return False
        

# Your ZigzagIterator object will be instantiated and called as such:
# i, v = ZigzagIterator(v1, v2), []
# while i.hasNext(): v.append(i.next())