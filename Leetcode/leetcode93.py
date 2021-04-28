# coding=utf-8


def restoreIpAddresses(s):
    '''
     复原 IP 地址 ： 给定一个只包含数字的字符串，用以表示一个 IP 地址
     返回所有可能从 s 获得的 有效 IP 地址 。你可以按任何顺序返回答案。
    :param s: 给定的字符串
    :return: 所有可能从 s 获得的有效的IP地址
    '''

    ans = []
    counter = 4
    segments = [0 for _ in range(counter)]

    dfs(s, 0, 0, ans, segments, counter)
    print ans


def dfs(s, segId, strStartPos, ans, segments, counter):
    # 到末尾
    if segId == counter:
        if strStartPos == len(s):
            ans.append('.'.join(str(seg) for seg in segments))
        return

    if strStartPos == len(s):
            return

    if s[strStartPos] == '0':
        segments[segId] = 0
        dfs(s, segId + 1, strStartPos + 1, ans, segments, counter)
    else:
        addr = 0
        for i in range(strStartPos, len(s)):
            addr = addr * 10 + ord(s[i]) - ord('0')
            if addr <= 255:
                segments[segId] = addr
                dfs(s, segId + 1, i + 1, ans, segments, counter)
            else:
                break

if __name__ == "__main__":
    restoreIpAddresses("00011")