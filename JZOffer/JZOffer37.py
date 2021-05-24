# coding=utf-8

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        myQueue = []
        if root == None:
            return "[]"
        # 结果集
        ret = []
        myQueue.append(root)
        while len(myQueue) > 0:
            temp = myQueue[0]
            if temp == None:
                ret.append(None)
                myQueue.pop(0)
            else:
                if temp.left:
                    myQueue.append(temp.left)
                else:
                    myQueue.append(None)
                if temp.right:
                    myQueue.append(temp.right)
                else:
                    myQueue.append(None)
                ret.append(temp.val)
                myQueue.pop(0)

        for i in range(len(ret)-1, -1, -1):
            if ret[i] == None:
                ret.pop(i)
            else:
                break

        return self.toString(ret)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if data == "[]":
            return None
        # 去掉括号
        data = data[1:-1]
        # 用逗号分割成子串
        arr = data.split(",")
        for i in range(len(arr)):
            if arr[i] == "None":
                arr[i] = None
            else:
                arr[i] = int(arr[i])

        root = TreeNode(arr[0])
        myQueue = [root]
        arr.pop(0)
        flag = 0 # 0 left 1 right
        while len(myQueue) > 0 and len(arr) > 0:
            if myQueue[0] == None:
                myQueue.pop(0)
                continue
            if flag == 0:
                flag = 1
                if arr[0] != None:
                    myQueue[0].left = TreeNode(arr[0])
                myQueue.append(myQueue[0].left)
            elif flag == 1:
                flag = 0
                if arr[0] != None:
                    myQueue[0].right = TreeNode(arr[0])
                myQueue.append(myQueue[0].right)
                myQueue.pop(0)

            arr.pop(0)
        return root
    

    def toString(self, arr):
        ans = "[" + str(arr[0])
        for i in range(1,len(arr)):
            ans += ","
            if arr[i] == None:
                ans += "None"
            else:
                ans += str(arr[i])
        ans += "]"
        return ans


if __name__ == "__main__":
    ser = Codec()
    deser = Codec()

    ans = deser.deserialize("[1,2,3,None,None,4,5,6,7]")
    print ser.serialize(ans)