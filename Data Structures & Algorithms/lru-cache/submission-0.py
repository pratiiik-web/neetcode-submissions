class DoubleLinkedList:
    def __init__(self, val = None, key = None, lastnode = None, nextnode = None):
        self.val = val
        self.key = key
        self.lastnode = lastnode
        self.nextnode = nextnode


class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.data = {}
        self.capacity = capacity
        self.size = 0
        self.head = DoubleLinkedList(None, None, None, None)
        self.tail = DoubleLinkedList(None, None, self.head, None)
        self.head.nextnode = self.tail
        

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.data:
            return -1
        self.setFirst(key)
        return self.data[key].val

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key in self.data:
            self.data[key].val = value
            self.setFirst(key)
        else:
            self.data[key] = DoubleLinkedList(value, key, self.head, self.head.nextnode)
            self.head.nextnode.lastnode = self.data[key]
            self.head.nextnode = self.data[key]
            self.size += 1
            if self.size > self.capacity:
                self.size -= 1
                topop = self.tail.lastnode
                topop.lastnode.nextnode = topop.nextnode
                topop.nextnode.lastnode = topop.lastnode
                del self.data[topop.key]


    def setFirst(self, key):
        tomove = self.data[key]
        lastnode = tomove.lastnode
        nextnode = tomove.nextnode
        lastnode.nextnode = nextnode
        nextnode.lastnode = lastnode
        tomove.lastnode = self.head
        tomove.nextnode = self.head.nextnode
        tomove.lastnode.nextnode = tomove
        tomove.nextnode.lastnode = tomove