# coding=utf-8
"""
问题：使用python实现单例模式
方法3:使用类方法实现单例模式

简单实现instance方法，因为如果在init方法中有一些IO操作，就会发现并行问题-->对线程加锁
未加锁部分并发执行,加锁部分串行执行,速度降低,但是保证了数据安全-->
当程序执行时，执行了time.sleep(20)后，下面实例化对象时，此时已经是单例模式了，但我们还是加了锁，
进行一些优化，把intance方法添加上下文
"""

import time
import threading
class Singleton(object):
    _instance_lock = threading.Lock() # 必须要加锁，否则存在IO时会失效

    def __init__(self):
        time.sleep(1) # 模拟IO操作

    @classmethod
    def instance(cls, *args, **kwargs):
        if not hasattr(Singleton, "_instance"):
            with Singleton._instance_lock:
                if not hasattr(Singleton, "_instance"):
                    Singleton._instance = Singleton(*args, **kwargs)
        return Singleton._instance

if __name__ == '__main__':
    obj1 = Singleton.instance() # 必须通过方法实例化
    time.sleep(5) # 时间间隔，模拟一直加锁问题
    obj2 = Singleton.instance()
    print(obj1 is obj2)