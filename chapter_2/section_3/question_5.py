# coding=utf-8
"""
问题：替换空格
方法1:用python字符串的replace方法。
方法2.对空格split得到list，用‘%20’连接（join）这个list
方法3.由于替换空格后，字符串长度需要增大。先扫描空格个数，计算字符串应有的长度，从后向前一个个字符复制（需要两个指针）。这样避免了替换空格后，需要移动的操作。
"""
def replaceSpace1(s):
    return s.replace(' ', '%20')

def replaceSpace2(s):
    num_space = 0
    for i in s:
        if i == ' ':
            num_space += 1

    new_length = len(s) + 2 * num_space
    index_origin = len(s) - 1
    index_new = new_length - 1
    new_string = [None for i in range(new_length)]

    while index_origin >= 0 & (index_new > index_origin):
        if s[index_origin] == ' ':
            new_string[index_new] = '0'
            index_new -= 1
            new_string[index_new] = '2'
            index_new -= 1
            new_string[index_new] = '%'
            index_new -= 1
        else:
            new_string[index_new] = s[index_origin]
            index_new -= 1
        index_origin -= 1
    return ''.join(new_string)

def replaceSpace3(s):
    return '%20'.join(s.split(' '))
    
if __name__ == '__main__':
    s = 'I like you'
    print(replaceSpace1(s))
    print(replaceSpace2(s))
    print(replaceSpace3(s))