import structure as stru

# 最小生成树

# 邻接矩阵规模
MAX_SIZE = 10


# 邻接矩阵，元素为顶点
class AdjMatrix:
    edge = [([0] * MAX_SIZE) for i in range(MAX_SIZE)]


# 邻接表
class AdjLink:
    class edge:
        adj_vex = -1
        next = None

    # 顶点表,元素为edge
    vTable = []


# 邻接矩阵的广度优先遍历
# 针对无向图，可按照上三角压缩存储，故此只遍历上三角区域
def bfs(data):
    if data is None:
        print('图不能为空！')
        return None
    # 结果队列
    result = stru.Rqueue()

    # 辅助队列
    q = stru.Rqueue()
    # 初始化辅助队列
    q.enQueue(0)
    while not q.isEmpty():
        # 出队时访问节点
        row = q.deQueue().data
        result.enQueue(row)
        # 遍历一层
        for i in range(row + 1, MAX_SIZE):
            if data.edge[row][i] > 0:
                q.enQueue(i)
    print(result)


# 邻接矩阵的深度优先遍历
# 由于是无向图，因此采用可以采用压缩存储的遍历方式
def dfs(data):
    if data is None:
        print('图不能为空！')
        return None
    # 结果队列
    result = stru.Rqueue()

    # 辅助栈
    stack = stru.Rstack()

    # 初始化辅助栈
    stack.push(0)
    while not stack.isEmpty():
        row = stack.pop().data
        result.enQueue(row)
        for i in range(row + 1, MAX_SIZE):
            # 入栈时访问节点
            if data.edge[row][i] > 0:
                stack.push(i)
    print(result)
