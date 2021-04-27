# coding=utf-8

# 1。 交换0，1位置，计算最多交换次数
def exchangePos0_1(arr):
    counter = 0
    left = 0
    right = len(arr)-1
    while left < right:
        if arr[left] == 1 and arr[right] == 0:
            arr[left] = 0
            arr[right] = 1
            left += 1
            right -= 1
            counter += 1
        elif arr[left] == 1:
            right -= 1
        else:
            left += 1
    return counter

# 2。 字符替换和复制，删除一个字符串所有的a，并且复制所有的b，复制的要紧跟在b之后
def delAndCopyChar(testString):
    arr = list(testString)
    idx = 0
    pos = len(arr)
    b_num = 0

    # 删除a的同时 记录了b的个数
    while idx < pos:
        if arr[idx] == 'a':
            arr.pop(idx)
            pos -= 1
            idx -= 1
        if arr[idx] == 'b':
            b_num += 1
        idx += 1
    # 复制b
    temp = [0 for i in range(b_num)]
    arr.extend(temp)
    # 倒着找
    idx = len(arr)-1
    pos -= 1
    while pos > 0:
        arr[idx] = arr[pos]
        idx -= 1
        # 如果是'b'需要标记为复制的内容
        if arr[pos] == 'b':
            arr[idx] = arr[pos]
            idx -= 1
        pos -= 1
    return ''.join(arr)

# 3。 交换星号 给定一个字符串只包含*和数字，请把它的*号都放在开头
# 如果对数字顺序无要求，则直接快排
# 如果对数字顺序要求按照之前的，则只能倒着往回找

# 4。 子串变位词 给定两个串a,b, 问b是否为a的子串的变位词 a=hello b=lel true  b=elo flase
# 滑动窗口的思想，动态维护一个"窗口" 窗口的大小就是字符串b的长度，然后从字符串a中去找符合长度的子串
def judgeSubStringExchangePos(string, subString):
    strArr = list(string)
    subStrArr = list(subString)

    window = len(subStrArr)
    if len(strArr) < window:
        return False
    else:
        # 动态维护窗口
        num = [0 for _ in range(26)]

        # 记录当前窗口的字符数
        for j in range(0, window):
            num[ord(subStrArr[j]) - ord('a')] += 1

        flag = False
        # 滑动窗口
        for i in range(0, len(strArr)-window+1):
            flag = True
            # 记录当前窗口的字符数
            for j in range(0, window):
                num[ord(strArr[i+j]) - ord('a')] -= 1

            for pos in range(0, window):
                if num[pos] != 0:
                    flag = False
                    break

            if flag == True:
                return flag

            # 还原
            for j in range(0, window):
                num[ord(strArr[i + j]) - ord('a')] += 1

        return False


# 5。 单词翻转 翻转句子中全部的单词，单词内容不变
def reverseSentence(sentence):
    words = sentence.split(' ')
    result = ""
    for i in range(0, len(words)):
        if i != 0:
            result += " "
        result += reverseWord(words[i])
    return result

def reverseWord(word):
    if len(word) < 2:
        return word
    else:
        arr = list(word)
        left = 0
        right = len(arr)-1
        while left < right:
            temp = arr[left]
            arr[left] = arr[right]
            arr[right] = temp
            left += 1
            right -= 1

        return ''.join(arr)

# 6。 字符串循环移位
# 结论 长度为n的字符串，移动m次，相当于移动了m%n次
# 通过对前m%n位翻转，后n-m%n位翻转，总体再翻转一次就达到了题目的目的

if __name__ == "__main__":
    '''
    # 交换0，1位置
    arr = [0,0,1,0,1,1,0,0,0,1,1,0,1,1,0,0,0]
    print (exchangePos0_1(arr))
    '''

    '''
    # 字符的删除和复制
    testS = "aq129absbebbweb1a1ab"
    print(testS)
    print(delAndCopyChar(testS))
    '''

    '''
    # 判断子串变位词
    print (judgeSubStringExchangePos('mynameislily', 'iisl'))
    '''

    '''
    print('aqksfklde')
    print(reverseWord('aqksfklde'))
    

    print(reverseSentence('I ma a .tneduts'))
    '''


