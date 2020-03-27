from collections import deque
from queue import LifoQueue

# Type 1 Stack & Queue

class Stack:

    def __init__(self):
        self.stack = []

    def pop(self):
        if len(self.stack) < 1:
            return None
        return self.stack.pop()

    def push(self, item):
        self.stack.append(item)

    def size(self):
        return len(self.stack)

class Queue:

    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if len(self.queue) < 1:
            return None
        return self.queue.pop(0)

    def size(self):
        return len(self.queue)

test1 = Stack()
test1.push(10)
test1.push(11)
test1.push(12)

test2 = Queue()
test2.enqueue(10)
test2.enqueue(11)
test2.enqueue(12)

print(test1.pop())
print(test2.dequeue())

# Type 2 Stack & Queue with module collection and method deque
test3 = deque()
test3.append(10)
test3.append(11)
test3.append(12)

while 0 < len(test3):
    print(test3.pop())

# # Type 3 Queue with class LifoQueue
test4 = LifoQueue()

test4.put(10)
test4.put(11)
test4.put(12)

print(test4.get())
print(test4.get())
print(test4.get())
