# coding=utf-8

def canCompleteCircuit(gas, cost):
    n = len(gas)
    # 索引
    for idx in range(n):
        sum = 0
        flag = True
        t = 0
        while True:
            # 跳出循环
            if t >= n:
                break
            sum += gas[(t + idx) % n] - cost[(t + idx) % n]
            if sum < 0:
                flag = False
                break
            t += 1

        if flag:
            return idx
    return -1


if __name__ == "__main__":
    gasArr = [1, 2, 3, 4, 5]
    costArr = [3, 4, 5, 1, 2]
    print canCompleteCircuit(gasArr, costArr)