# 链式队列
class Rqueue:
    # 链式队列结点
    class Node:
        data = None
        next = None

    front = Node()
    rear = front
    length = 0

    # 入队
    def enQueue(self, data):
        node = self.Node()
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


# 链式栈
class Rstack:
    class Node:
        data = None
        pre = None

    # 带有头结点，使出栈、入栈操作一致
    top = Node()
    length = 0

    # 出栈
    def pop(self):
        if self.length <= 0:
            print('空栈不支持pop操作！')
            return None
        rs = self.top
        self.top = self.top.pre
        self.length -= 1
        return rs

    # 入栈
    def push(self, data):
        node = self.Node()
        node.data = data
        node.pre = self.top
        self.top = node
        self.length += 1

    # 队列判空
    def isEmpty(self):
        if self.length > 0:
            return 0
        else:
            return 1
