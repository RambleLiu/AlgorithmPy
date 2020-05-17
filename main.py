import map

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

map.bfs(adj_matrix)
map.dfs(adj_matrix)
