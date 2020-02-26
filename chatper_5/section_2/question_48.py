# coding=utf-8
"""
最长不含重复字符的子字符串
"""


def lengthOfLongestSubstring(s):
    head = 0
    tail = 0
    if len(s) < 2: return len(s) # 边界条件
    res = 1
    
    while tail < len(s) - 1:
        tail += 1
        if s[tail] not in s[head: tail]:
            res = max(tail - head + 1, res)
        else:
            while s[tail] in s[head: tail]:
                head += 1
    return res

if __name__ == '__main__':
    s = 'abcabcbb'
    print(lengthOfLongestSubstring(s))
