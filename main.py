import structure as stru
import map


# 邻接矩阵的广度优先遍历
# 针对无向图，可按照上三角压缩存储，故此只遍历上三角区域
def bfs(data):
    # 结果队列
    result = stru.Queue()

    # 辅助队列
    q = stru.Queue()
    q.enQueue(0)
    result.enQueue(0)
    length = map.MAX_SIZE
    while not q.isEmpty():
        row = q.deQueue().data
        # 遍历一层
        for i in range(row + 1, length):
            # 路径<=0表示Vrow与Vi路径不通
            if data.edge[row][i] <= 0:
                continue
            q.enQueue(i)
            result.enQueue(i)
    print(result)


# 定义图的邻接矩阵
adj_matrix = map.AdjMatrix()
adj_matrix.edge[0][1] = 1
adj_matrix.edge[0][2] = 0
adj_matrix.edge[0][3] = 1
adj_matrix.edge[0][4] = 1
adj_matrix.edge[1][2] = 1
adj_matrix.edge[1][3] = 0
adj_matrix.edge[2][3] = 0
adj_matrix.edge[2][5] = 1

bfs(adj_matrix)

