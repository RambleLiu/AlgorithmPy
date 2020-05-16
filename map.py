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
