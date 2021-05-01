# coding=utf-8

class Employee:
    def __init__(self, id, importance, subordinates):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates


def getImportance(employees, id):
    myDict = {}
    # 遍历员工列表
    for e in employees:
        myDict[e.id] = e

    # 答案
    ans = myDict[id].importance
    # 队列
    queue = [i for i in myDict[id].subordinates]
    # 给定员工的直系下属
    while len(queue) > 0:
        # 队头
        ans += myDict[queue[0]].importance
        queue.extend(myDict[queue[0]].subordinates)
        queue.pop(0)

    return ans


if __name__ == "__main__":
    e1 = Employee(1, 2, [2])
    e2 = Employee(2, 3, [])
    arr = [e1, e2]
    id = 2
    print getImportance(arr,id)