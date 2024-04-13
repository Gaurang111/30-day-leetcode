class Solution(object):
    def trap(self, height):
        if len(height) <= 2:
            return 0
        amount, left, right, left_max, right_max = 0, 0, len(height)-1, 0, 0
        while left <= right:
            if height[left] <= height[right]:
                if left_max < height[left]:
                    left_max = height[left]
                else:
                    amount += left_max - height[left]
                left += 1
            else:
                if right_max < height[right]:
                    right_max = height[right]
                else:
                    amount += right_max - height[right]
                right -= 1
        return amount