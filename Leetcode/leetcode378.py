# coding=utf-8

def kthSmallest_simple(matrix, k):
    '''
    超出时间限制
    '''
    n = len(matrix)
    arr = [0 for _ in range(k)]
    num = 0
    for i in range(n):
        for j in range(n):
            # counter
            counter = i*(j+1)+j
            # 计算当前单元格一定比这个值小的数量
            if counter >= k:
                break
            elif num == 0:
                arr[0] = matrix[0][0]
                num += 1
            else:
                idx = num-1
                while idx >= 0:
                    if arr[idx] > matrix[i][j]:
                        if idx < k-1:
                            arr[idx + 1] = arr[idx]
                        idx -= 1
                    else:
                        break
                if num < k:
                    num += 1
                if idx < k-1:
                    arr[idx+1] = matrix[i][j]
                elif matrix[i][j] < arr[idx]:
                    arr[idx] = matrix[i][j]
    return arr[k-1]


def kthSmallest(matrix, k):
    '''
    优化版本 二分查找
    '''




if __name__ == "__main__":
    matrix = [[1,5,7,9],[6,10,11,13],[11,12,13,15],[12,12,13,15]]
    k = 8
    print kthSmallest(matrix, k)
