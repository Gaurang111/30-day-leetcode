class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix:
            return 0

        row_count, column_count = len(matrix), len(matrix[0])
        height_array = [0] * (column_count + 1)
        maximum_area = 0

        for current_row in matrix:
            for column in range(column_count):
                height_array[column] = height_array[column] + 1 if current_row[column] == '1' else 0

            stack = []
            for index in range(len(height_array)):
                while stack and height_array[index] < height_array[stack[-1]]:
                    current_height = height_array[stack.pop()]
                    width = index if not stack else index - stack[-1] - 1
                    maximum_area = max(maximum_area, current_height * width)
                stack.append(index)

        return maximum_area