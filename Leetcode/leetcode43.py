# coding=utf-8

def multiply(num1, num2):
    num1Arr = [int(num1[i:i+1]) for i in range(len(num1))]
    ret = 0
    # 遍历i
    for i in range(len(num2)):
        j = len(num2) - i - 1
        right = int(num2[j])
        sum = 0
        c = 0
        t = 0
        while t < len(num1):
            idx = len(num1)-t-1
            temp = num1Arr[idx] * right
            sum += (10**t) * (temp % 10 + c)
            c = temp // 10
            t += 1
        # 如果还有进位
        if c != 0:
            sum += (10**t) * c

        ret += 10**i * sum

    return ret


if __name__ == "__main__":
    print multiply("123", "456")


