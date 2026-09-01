class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {} #key, pointer to node 

        self.Left = Node(0, 0)
        self.Right = Node(0, 0)
        self.Left.next, self.Right.prev = self.Right, self.Left

    def remove(self, node):
        nxt, prev = node.next, node.prev
        prev.next = nxt
        nxt.prev = prev
        

    def insert(self, node):
        prev, nxt = self.Right.prev, self.Right
        prev.next = node
        nxt.prev = node
        node.prev = prev
        node.next = nxt



    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        if len(self.cache) > self.cap:
            lru = self.Left.next
            self.remove(lru)
            del self.cache[lru.key]
        
