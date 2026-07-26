class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        for _ in range(4):
            if mat == target:
                return True

            nga = len(mat)

            for i in range(nga):
                for j in range(i + 1, nga):
                    mat[i][j], mat[j][i] = mat[j][i], mat[i][j]

            for row in mat:
                row.reverse()

        return False
        #return False will only return after checking each rotation by 90 degree is equal to the target matrix