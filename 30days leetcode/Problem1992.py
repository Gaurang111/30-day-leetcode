class Solution(object):
    def solve(self, r, c, max_coordinates, land, vis):
        m = len(land)
        n = len(land[0])

        vis[r][c] = True

        dr = [-1, 1, 0, 0]
        dc = [0, 0, -1, 1]

        for i in range(4):
            nr = dr[i] + r
            nc = dc[i] + c

            if 0 <= nr < m and 0 <= nc < n and land[nr][nc] == 1 and not vis[nr][nc]:
                max_coordinates[0] = max(max_coordinates[0], nr)
                max_coordinates[1] = max(max_coordinates[1], nc)

                self.solve(nr, nc, max_coordinates, land, vis)

    def findFarmland(self, land):
        m = len(land)
        n = len(land[0])

        vis = [[False] * n for _ in range(m)]

        ans_list = []

        for i in range(m):
            for j in range(n):
                if not vis[i][j] and land[i][j] == 1:
                    max_coordinates = [i, j]

                    self.solve(i, j, max_coordinates, land, vis)

                    ans_list.append([i, j, max_coordinates[0], max_coordinates[1]])

        return ans_list