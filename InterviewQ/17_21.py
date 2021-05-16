
def trap(height):
    """
    :type height: List[int]
    :rtype: int
    """
    maxLeftValue = float('-inf')
    maxRightValue = float('-inf')

    sumWater, left, right = 0, 0, len(height) - 1

    while left < right:
        maxLeftValue = max(maxLeftValue, height[left])
        maxRightValue = max(maxRightValue, height[right])
        # 左边的最大值决定下界
        if maxLeftValue <= height[right]:
            sumWater += maxLeftValue - height[left]
            left += 1
        if maxRightValue <= height[left]:
            sumWater += maxRightValue - height[right]
            right -= 1

    return sumWater