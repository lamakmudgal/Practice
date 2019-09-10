class ListNode:
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None


# Used double linked-list to maintain the node. O(1)
class LRUCache_linkedList:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cacheData = {}
        self.head: ListNode = None
        self.tail: ListNode = None

    def get(self, key: int) -> int:
        node = self.cacheData.get(key)
        if node:
            # move the current node to the front of the linked list
            self.__moveNodeToFront(node)
            return node.value
        return -1

    def put(self, key: int, value: int) -> None:
        node = self.cacheData.get(key)
        if node:
            # key already exsit in cache, update the value
            node.value = value
            # move the node to front since it has been updated
            self.__moveNodeToFront(node)
        else:
            newNode = ListNode(key, value)
            self.cacheData[key] = newNode
            self.__addNodeAtFront(newNode)
            if len(self.cacheData) > self.capacity:
                del self.cacheData[self.tail.key]
                self.__removeNode(self.tail)

    def __moveNodeToFront(self, node: ListNode):
        self.__removeNode(node)
        self.__addNodeAtFront(node)

    def __removeNode(self, node: ListNode):
        # This method needs to consider if the node you want to remove is the head or the tail.
        n = node.next  # if node is tail, then n will be None
        p = node.prev  # if node is head, then p will be None
        if not p:
            self.head = n
            node.next = None
            if n:
                n.prev = None
        else:
            p.next = n
            if n:
                n.prev = node.prev
            else:
                self.tail = node.prev
                node.prev = None

    def __addNodeAtFront(self, node: ListNode):
        if not self.head:
            # if the linked list does not exist yet
            self.head = node
            self.tail = node
            return
        node.next = self.head
        self.head.prev = node
        node.prev = None
        self.head = node