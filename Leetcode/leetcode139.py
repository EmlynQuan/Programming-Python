# coding=utf-8

def wordBreak(s, wordDict):
    """
    :type s: str
    :type wordDict: List[str]
    :rtype: bool
    """
    n = len(s)
    # 动态规划 子串是否能够分割为单词 1代表可以
    dp = [0 for _ in range(n+1)]
    # 空前缀表示可以
    dp[0] = 1

    # dp[i] 表示 字符串s[0:i]是否能够被分割成单词组
    for i in range(n):
        for j in range(i+1, n+1):
            # 子串的长度为l
            for l in range(0, j-i):
                # print s[i+l:j]
                if dp[i+l] == 1 and s[i+l:j] in wordDict:
                    dp[j] = 1
                    break
    if dp[n] == 1:
        return True
    else:
        return False

if __name__ == "__main__":
    s = "leetcode"
    wordDict = ["leet", "code"]
    print wordBreak(s, wordDict)
