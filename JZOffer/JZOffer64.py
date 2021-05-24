# coding=utf-8

def quickMul(self, A, B):
    return B and (B & 1 and A) + self.quickMul(A << 1, B >> 1)


def sumNums(self, n):
    return self.quickMul(n, n + 1) >> 1