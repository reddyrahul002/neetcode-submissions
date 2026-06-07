class Node :
     def __init__(self,key=0,val=0):  
        self.key=key
        self.val=val
        self.prev=None
        self.next=None
class LRUCache:
    def __init__(self, cap: int):
        self.cap=cap
        self.cache={}
        self.head=Node(0,0)
        self.tail=Node(0,0)
        self.head.next=self.tail
        self.tail.prev=self.head
    def insert_head(self,node):
        right=self.head.next
        node.next=right
        right.prev=node
        self.head.next=node
        node.prev= self.head
    def delete_node(self,node):
        left=node.prev
        right=node.next
        left.next=right
        right.prev=left
    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self.delete_node(node)
        self.insert_head(node)
        return node.val
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            self.delete_node(node)
            del self.cache[key]
        node=Node(key,value)
        self.cache[key]=node
        self.insert_head(node)
        if len(self.cache)>self.cap:
            lru=self.tail.prev
            self.delete_node(lru)
            del self.cache[lru.key]


            
        
