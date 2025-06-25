from collections import deque

class MessageQueue:
    def __init__(self):
        self.queue = deque()

    def enqueue(self, msg):
        self.queue.append(msg)

    def dequeue(self):
        if self.queue:
            return self.queue.popleft()
        return "Queue is empty"
