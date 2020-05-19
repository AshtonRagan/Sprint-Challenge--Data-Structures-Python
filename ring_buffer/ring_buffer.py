class RingBuffer:

    def __init__(self, capacity, data=[]):
        """Initialization"""
        self.index = 0
        self.capacity = capacity
        self._data = list(data)[-capacity:]

    def append(self, value):
        """Append an element"""
        if len(self._data) == self.capacity:
            self._data[self.index] = value
        else:
            self._data.append(value)
        self.index = (self.index + 1) % self.capacity

    def get(self):
        return(self._data)
