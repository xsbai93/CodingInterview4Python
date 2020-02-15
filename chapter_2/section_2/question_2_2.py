# coding=utf-8
"""
问题：使用python实现单例模式
方法2:使用装饰器实现单例模式

"""

def single_ton(cls):
    _instance = {}
    def single(*args, **kwargs):
        if cls not in _instance:
            _instance[cls] = cls(*args, **kwargs)
        return _instance[cls]
    return single


@single_ton
class SingleTon(object):
    def __init__(self, val):
        self.val = val


if __name__ == '__main__':
    obj1 = SingleTon(1)
    obj2 = SingleTon(2)
    print(obj2 is obj2)