from dataclasses import dataclass
from typing import Any


@dataclass
class Node:
    value: int = None
    nxt: Any = None  


@dataclass
class Deque:
    head: Node = None      
    tail: Node = None     
    size: int = 0

  
    def add_first(self, n):
        N = Node(n, Node)
        if self.head is None:
            self.head = N
            self.tail = N
        else:
            N.nxt = self.head
            self.head = N
        self.size += 1

    def to_string(self):
        if self.head is None:
            return "{"+" "+"}"
        else:
            s = "{ "
            node = self.head
            while node.value is not None:
                s += str(node.value) + " "
                node = node.nxt
                if node is not None:
                    continue
                else:
                    break
            s += "}"
            return s

    def add_last(self, n):
        N = Node(n, Node)
        if self.head is None:
            self.head = N
            self.tail = N
            N.nxt = None
        else:
            self.tail.nxt = N
            self.tail = N
            N.nxt = None
        self.size += 1
  
    def get_last(self):
        if self.tail is None:
            print("Can't access an empty queu")
            return None
        else:
            return self.tail.value
   
    def get_first(self):
        if self.head is None:
            print("can't access to an empty queue")
            return None
        else:
            return self.head.value

    def remove_first(self):
        if self.head is None:
            print("cant access an empty queu")
            return None
        elif self.size == 1:
            removed = self.size
            self.head = None
            self.tail = None
            self.size -= 1
            return removed.value
        else:
            removed = self.head
            self.head = self.head.nxt
            self.size -= 1
            return removed.value

    def remove_last(self):

        if self.head is None:
            print("cant access an empty queue")
            return None
        elif self.size == 1:
            removed = self.tail
            self.head = None
            self.tail = None
            self.size -= 1
            return removed.value
        else:
            removed = self.tail
            before = self.head
            for i in range(self.size-2):
                before = before.nxt
            before.nxt = None
            self.tail = before
            self.size -= 1
            return removed.value
