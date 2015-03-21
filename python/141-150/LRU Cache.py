class LRUCache:
    _heap=[]
    _capacity=0
    _dic={}
    # @param capacity, an integer
    def __init__(self, capacity):
        self._capacity=capacity
        self._heap=[]
        self._dic={}
        
    # @return an integer
    def get(self, key):
        if key in self._heap:
            self._heap.remove(key)
            self._heap.insert(0,key)
            return self._dic[key]
        else:
            return -1
    # @param key, an integer
    # @param value, an integer
    # @return nothing
    def set(self, key, value):
        if key in self._heap:
            self._heap.remove(key)
            self._heap.insert(0,key)
            self._dic[key]=value
        else:
            if len(self._heap)<self._capacity:
                self._heap.insert(0,key)
                self._dic[key]=value
            else:
                tempkey=self._heap[-1]
                del self._heap[-1]
                del self._dic[tempkey]
                self._heap.insert(0,key)
                self._dic[key]=value
        return
