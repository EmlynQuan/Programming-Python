# coding=utf-8

def swapNumbers(numbers):
    # a = a^b
    numbers[0] = numbers[0] ^ numbers[1]
    # b = b ^ a ^ b = a
    numbers[1] = numbers[1] ^ numbers[0]
    # a = b ^ a ^ b ^ a ^ b = b
    numbers[0] = numbers[0] ^ numbers[1]
    return numbers