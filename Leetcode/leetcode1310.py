# coding=utf-8

def xorQueries(arr, queries):
    n = len(arr)
    prefix = [0 for i in range(n+1)]
    for i in range(1, n+1):
        prefix[i] = prefix[i-1]^arr[i-1]

    ret = []
    for temp in queries:
        ret.append(prefix[temp[0]]^prefix[temp[1]+1])
    return ret

if __name__ == "__main__":
    arr = [1, 3, 4, 8]
    queries = [[0, 1], [1, 2], [0, 3], [3, 3]]
    print xorQueries(arr, queries)