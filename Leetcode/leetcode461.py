# coding = utf-8

def hammingDistance(x, y):
    """
    :type x: int
    :type y: int
    :rtype: int
    """
    bitNum = 31
    counter = 0
    for i in range(bitNum):
        if ((x >> i) & 1) ^ ((y >> i) & 1) == 1:
            counter += 1

    return counter