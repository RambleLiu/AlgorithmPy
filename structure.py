# 链式队列结点
class Node:
    data = None
    next = None


# 队列
class Queue:
    front = Node()
    rear = front
    length = 0

    # 入队
    def enQueue(self, data):
        node = Node()
        node.data = data
        self.rear.next = node
        self.rear = node
        self.length += 1

    # 出队
    def deQueue(self):
        if self.isEmpty():
            return None
        rs = self.front.next
        self.front = self.front.next
        self.length -= 1
        return rs

    # 队列判空
    def isEmpty(self):
        if self.length > 0:
            return 0
        else:
            return 1

    # 输出队列
    def __str__(self):
        rs = ''
        index = self.front.next
        while index is not None:
            rs += str(index.data) + ','
            index = index.next
        return rs[0:-1]
