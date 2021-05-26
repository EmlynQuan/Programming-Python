# coding=utf-8

def minArray(numbers):
    """
    :type numbers: List[int]
    :rtype: int
    """
    left, right = 0, len(numbers)-1
    if numbers[right] > numbers[left]:
        return numbers[left]
    while left < right:
        mid = (left + right) // 2
        if numbers[mid] > numbers[right]:
            left = mid + 1
        elif numbers[mid] < numbers[right]:
            right = mid
        else:
            right -= 1
    return numbers[right]


if __name__ == "__main__":
    minArray([3,1,3])